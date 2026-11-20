# Planning prévisionnel du projet

Mise à jour du 20 novembre 2026. Le projet porte sur le diagnostic de
sous-extrusion et l’aide à la décision lors du contrôle de pièces imprimées en 3D.
Le **vendredi 15 janvier 2027** sert de date de travail, à confirmer avec
l’encadrant.

```mermaid
gantt
    title Réseaux bayésiens pour le contrôle qualité en impression 3D
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    tickInterval 1week
    todayMarker off

    section Travaux réalisés
    Notes sur les supports Stanford                  :done, stanford, 2026-11-12, 1d
    Choix du diagnostic de sous-extrusion             :milestone, done, sujet, 2026-11-20, 0d
    Graphe à six variables et CPT fictives            :done, modele, 2026-11-20, 1d
    Premier générateur de pièces synthétiques         :done, generateur, 2026-11-20, 1d

    section Cadrage et prototype
    Préciser les mesures et les critères d’évaluation :cadrage, 2026-11-23, 2026-11-28
    Définir les seuils et le contrôle de confirmation :seuils, 2026-11-23, 2026-11-28
    Vérifier l’inférence exacte sur les cas de référence :inference, 2026-11-30, 2026-12-05
    Estimer les CPT à partir des données synthétiques :apprentissage, 2026-12-07, 2026-12-11
    Démonstration minimale reproductible             :milestone, demo, 2026-12-11, 0d

    section Évaluation et rendu
    Évaluer indices manquants et données rares        :evaluation, 2026-12-14, 2026-12-19
    Rédiger le rapport pédagogique                   :rapport, 2026-11-23, 2027-01-09
    Marge de fin d’année                             :marge, 2026-12-21, 2027-01-04
    Relecture et reproduction de la démonstration    :relecture, 2027-01-04, 2027-01-15
    Rendu final prévisionnel                         :milestone, crit, rendu, 2027-01-15, 0d
```

Le [graphe](GRAPH.md) décrit le diagnostic et les trois actions possibles.
Les [CPT](CPT.md) servent de référence pour simuler les pièces et vérifier
l’apprentissage. L’évaluation compare les paramètres estimés aux paramètres
de simulation et vérifie le calcul du diagnostic lorsque certains indices
sont indisponibles. Gibbs et EM restent des extensions possibles pour
l’inférence approchée et l’apprentissage sur données incomplètes.

## Priorités proposées

| Niveau | Objectif | Preuve d'achèvement envisagée |
| --- | --- | --- |
| Nécessaire | Formaliser un cas d'usage limité et ses hypothèses | Question, variables, utilisateurs et exclusions explicités |
| Nécessaire | Documenter les réseaux bayésiens et les méthodes retenues | Ressources annotées et explications reliées au cas |
| Nécessaire | Implémenter inférence et apprentissage des paramètres dans le périmètre convenu | Exemple reproductible et vérifications de cohérence |
| Nécessaire | Évaluer le prototype et ses limites | Critères définis au cadrage, expériences traçables |
| Nécessaire | Assurer suivi et versionnement | Journal, comptes rendus, dépôt public et historique lisible |
| Nécessaire | Rédiger un rapport pédagogique | Fil conducteur du besoin jusqu'aux résultats et limites |
| Intéressante | Étudier la sensibilité aux paramètres et aux données rares | Comparaisons sur scénarios contrôlés |
| Intéressante | Comparer plusieurs méthodes pertinentes | Protocole commun et discussion des écarts |
| Optionnelle | Ajouter une interface de démonstration | Parcours illustrant les résultats du prototype |
| Optionnelle | Étendre à la structure du graphe ou à un second cas | Seulement après stabilisation du socle |
