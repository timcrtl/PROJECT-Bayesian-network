### Probabilité initiale du défaut

| Probabilité | Valeur |
|---|---:|
| `P(S)` | 8 % |
| `P(¬S)` | 92 % |

### Tables de probabilités conditionnelles des cinq indices

| Indice | Probabilité si `S` est présent | Valeur | Probabilité si `S` est absent | Valeur |
|---|---|---:|---|---:|
| `E` · Espaces visibles | `P(E ∣ S)` | 75 % | `P(E ∣ ¬S)` | 8 % |
| `M` · Masse trop faible | `P(M ∣ S)` | 80 % | `P(M ∣ ¬S)` | 10 % |
| `T` · Paroi trop mince | `P(T ∣ S)` | 65 % | `P(T ∣ ¬S)` | 12 % |
| `D` · Détail trop étroit | `P(D ∣ S)` | 55 % | `P(D ∣ ¬S)` | 15 % |
| `F` · Fléchissement excessif | `P(F ∣ S)` | 70 % | `P(F ∣ ¬S)` | 12 % |

### Probabilité du défaut sachant les indices

| Observations | Probabilité calculée | Valeur |
|---|---|---:|
| Espaces visibles | `P(S ∣ E)` | 44,9 % |
| Espaces visibles et masse trop faible | `P(S ∣ E,M)` | 86,7 % |
| Aucun espace visible et masse trop faible | `P(S ∣ ¬E,M)` | 15,9 % |
| Espaces visibles, masse trop faible et paroi trop mince | `P(S ∣ E,M,T)` | 97,2 % |
