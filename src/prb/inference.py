from .piece_generator import P_INDICE, P_SOUS_EXTRUSION

def probabilite_sous_extrusion(observations: dict[str, int]) -> float:
    p_s_et_observations = P_SOUS_EXTRUSION
    p_non_s_et_observations = 1 - P_SOUS_EXTRUSION

    for indice, valeur in observations.items():
        if valeur not in (0,1):
            raise ValueError(f"Valeur de l'indice {indice} doit être 0 ou 1, mais a été {valeur}")

        p_x_sachant_non_s, p_x_sachant_s = P_INDICE[indice] #cette ligne récupère les probabilités conditionnelles de l'indice donné en fonction de la présence ou de l'absence de sous-extrusion.
        if valeur == 0: 
            p_non_x_sachant_non_s = 1 - p_x_sachant_non_s
            p_non_x_sachant_s = 1 - p_x_sachant_s
            p_s_et_observations *= p_non_x_sachant_s
            p_non_s_et_observations *= p_non_x_sachant_non_s
            #ces lignes mettent à jour les probabilités jointes en multipliant par la probabilité de l'indice donné étant absent, conditionnellement à la présence ou à l'absence de sous-extrusion. 

        else: 
            p_s_et_observations *= p_x_sachant_s
            p_non_s_et_observations *= p_x_sachant_non_s
            #ces lignes mettent à jour les probabilités jointes en multipliant par la probabilité de l'indice donné étant présent, conditionnellement à la présence ou à l'absence de sous-extrusion.

    p_observations = p_s_et_observations + p_non_s_et_observations
    p_s_et_observations /= p_observations
    return p_s_et_observations

if __name__ == "__main__":

    print(f"P(S=1) = {P_SOUS_EXTRUSION:.2%}")
    print(f"P(S=0) = {1 - P_SOUS_EXTRUSION:.2%}")
    
    observations = {"E": 1, "M": 1, "T": 1, "D": 1, "F": 1}
    p_s_sachant_observations = probabilite_sous_extrusion(observations)
    print(f"P(S=1 | E=1, M=1, T=1, D=1, F=1) = {p_s_sachant_observations:.2%}")

    observations = {"E": 0, "M": 0, "T": 0, "D": 0, "F": 0}
    p_s_sachant_observations = probabilite_sous_extrusion(observations)
    print(f"P(S=1 | E=0, M=0, T=0 , D=0, F=0) = {p_s_sachant_observations:.2%}")

    observations = {"E": 1, "M": 1}
    p_s_sachant_observations = probabilite_sous_extrusion(observations)
    print(f"P(S=1 | E=1, M=1) = {p_s_sachant_observations:.2%}")
    
