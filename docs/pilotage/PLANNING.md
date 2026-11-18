# Gantt prévisionnel du projet

Mise à jour du 18 novembre 2026. Le rendu est prévu à la mi-janvier 2027.
Le **vendredi 15 janvier 2027** .

```mermaid
gantt
    title Réseaux bayésiens appliqués à la maternité
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    tickInterval 1week
    todayMarker off

    section Travaux réalisés
    ✓ Stanford revu et notes sur les supports       :done, stanford, 2026-11-12, 1d
    ✓ Cadrage initial et inventaire des variables   :done, inventaire, 2026-11-12, 2d
    ✓ Modèle pédagogique à trois variables          :done, exemple, 2026-11-13, 1d
    ✓ Recherche de sources et sélection candidate   :done, sources, 2026-11-15, 3d
    ✓ Classeur ENP 2021 et CPT locales               :done, extraction, 2026-11-17, 1d
    ✓ Réseau à dix variables et module instruments  :done, reseau, 2026-11-17, 1d
    ✓ Premiers scripts Python repérés               :milestone, done, scripts, 2026-11-18, 0d

    section Cadrage et prototype
    Consolider le cas et arbitrer les données       :cadrage, 2026-11-18, 2026-11-28
    Compléter les exercices ciblés                  :formation, 2026-11-18, 2026-11-28
    Périmètre et critères à valider                 :milestone, validation, 2026-11-27, 0d
    Consolider le graphe et vérifier les CPT        :graphe, 2026-11-30, 2026-12-05
    Intégrer inférence et apprentissage             :prototype, 2026-12-01, 2026-12-12
    Démonstration minimale reproductible           :milestone, demo, 2026-12-11, 0d

    section Évaluation et rendu
    Expériences et analyse des limites              :evaluation, 2026-12-14, 2026-12-19
    Rédaction progressive du rapport pédagogique    :rapport, 2026-11-23, 2027-01-09
    Marge de fin d’année                            :marge, 2026-12-21, 2027-01-04
    Dépôt public et partage du lien                 :depot, 2026-11-23, 2026-11-28
    Suivi, documentation et versionnement          :suivi, 2026-11-18, 2027-01-15
    Relecture, reproduction et préparation de la démo :relecture, 2027-01-04, 2027-01-15
    Rendu final prévisionnel                        :milestone, crit, rendu, 2027-01-15, 0d
```

- Les travaux réalisés sont détaillés dans le journal de projet. Le 18 novembre
  correspond au constat de présence des scripts Python. Leur intégration et
  leur vérification font partie du prototype à consolider.
- Le jalon du 27 novembre sert de repère pour arbitrer le cas d'usage avec
  l'encadrant. Le calendrier sera ajusté après la première réunion et selon les
  disponibilités de fin d'année.
- La démonstration prévoit un jeu synthétique si les données publiques ne
  permettent pas d'estimer les probabilités nécessaires au graphe retenu.
  Les tableaux ENP et leurs CPT locales alimentent le travail descriptif.
- La période du 21 décembre au 3 janvier sert de marge. Les expériences
  nécessaires sont prévues avant cette période et la relecture finale débute le
  4 janvier.

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

EM et les données manquantes seront reclassés en nécessaires s'ils font partie
du cas retenu ; aucun algorithme n'est imposé par ce planning.
La rédaction et la documentation avancent dès le début, pas seulement en décembre.
