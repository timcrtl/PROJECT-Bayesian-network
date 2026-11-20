from .piece_generator import P_INDICE, P_SOUS_EXTRUSION

def probabilite_sous_extrusion(observations: dict[str, int]) -> float:
    p_s_et_observations = P_SOUS_EXTRUSION
    p_non_s_et_observations = 1 - P_SOUS_EXTRUSION

    for indice, valeur in observations.items():
        if valeur not in (0,1):
            raise ValueError(f"Valeur de l'indice {indice} doit être 0 ou 1, mais a été {valeur}")