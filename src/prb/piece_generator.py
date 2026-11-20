"""Génère une population fictive de pièces imprimées en 3D."""

import argparse
import csv
from collections.abc import Iterator
from pathlib import Path
from random import Random

# CPT.md : chaque couple suit l’ordre (sous-extrusion absente, présente).
# E = Sous extrusion présente ou absente
# M = Masse trop faible 
# T = Paroie trop mince
# D = Détail trop aux mauvaises dimensions
# F = Fléchissement excéssif
P_SOUS_EXTRUSION = 0.08
P_INDICE = {
    "E": (0.08, 0.75), # P(E∣S=0) = 0.08, P(E∣S=1) = 0.75 
    "M": (0.10, 0.80), # P(M∣S=0) = 0.10, P(M∣S=1) = 0.80
    "T": (0.12, 0.65), # P(T∣S=0) = 0.12, P(T∣S=1) = 0.65
    "D": (0.15, 0.55), # P(D∣S=0) = 0.15, P(D∣S=1) = 0.55
    "F": (0.12, 0.70), # P(F∣S=0) = 0.12, P(F∣S=1) = 0.70
}


def generate_pieces(
    size: int, seed: int | None = None, missing_rate: float = 0.0
) -> Iterator[tuple[list[str | int], list[str | int]]]:
    """Produit les lignes complètes et observées, reliées par le même ID."""
    if size < 0:
        raise ValueError("La taille doit être positive ou nulle.")
    if not 0 <= missing_rate <= 1:
        raise ValueError("Le taux de masquage doit être compris entre 0 et 1.")

    population_rng = Random(seed)
    mask_rng = Random(population_rng.getrandbits(64))

    for index in range(1, size + 1):
        piece_id = f"PIECE-{index:06d}"
        defect = int(population_rng.random() < P_SOUS_EXTRUSION)
        indicators = [
            int(population_rng.random() < probabilities[defect])
            for probabilities in P_INDICE.values()
        ]
        observed = [
            "" if mask_rng.random() < missing_rate else value
            for value in indicators
        ]
        yield [piece_id, defect, *indicators], [piece_id, *observed]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sortie", type=Path, help="Nouveau dossier pour les deux CSV")
    parser.add_argument("--taille", type=int, required=True, help="Nombre de pièces")
    parser.add_argument("--graine", type=int, help="Graine des tirages")
    parser.add_argument(
        "--taux-manquants", type=float, default=0.0,
        help="Probabilité de masquer chaque indice (entre 0 et 1)",
    )
    args = parser.parse_args()
    if args.taille < 0:
        parser.error("--taille doit être positive ou nulle")
    if not 0 <= args.taux_manquants <= 1:
        parser.error("--taux-manquants doit être compris entre 0 et 1")

    try:
        args.sortie.mkdir()
        with (
            (args.sortie / "verite.csv").open("x", encoding="utf-8", newline="") as truth,
            (args.sortie / "observations.csv").open(
                "x", encoding="utf-8", newline=""
            ) as observations,
        ):
            truth_writer = csv.writer(truth)
            observations_writer = csv.writer(observations)
            truth_writer.writerow(("id_piece", "S", *P_INDICE))
            observations_writer.writerow(("id_piece", *P_INDICE))
            for complete, observed in generate_pieces(
                args.taille, args.graine, args.taux_manquants
            ):
                truth_writer.writerow(complete)
                observations_writer.writerow(observed)
    except OSError as error:
        parser.exit(1, f"Impossible de produire les fichiers CSV ({error}).\n")


if __name__ == "__main__":
    main()
