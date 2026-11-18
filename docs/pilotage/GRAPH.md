# Graphes des réseaux bayésiens

Les flèches représentent les dépendances probabilistes retenues dans chaque modèle.

## Réseau à 3 variables

```mermaid
flowchart LR
    C["C · Antécédent de césarienne"] --> Y["Y · Césarienne actuelle"]
    S["S · Présentation du siège"] --> Y
```

## Réseau à 10 variables

flowchart LR
    A["A · Âge maternel"] --> G["G · Type de grossesse"]
    P["P · Parité"] --> C["C · Antécédent de césarienne"]
    G --> S["S · Présentation fœtale"]
    G --> M["M · Menace d’accouchement prématuré avec hospitalisation"]
    M --> K["K · Corticothérapie anténatale"]
    C --> D["D · Mode de début du travail"]
    S --> D
    C --> Y["Y · Mode d’accouchement effectif"]
    S --> Y
    D --> Y
    Y --> I["I · Instrument utilisé"]
```
