p_c = {0: 0.8, 1: 0.2}
p_s = {0: 0.90, 1: 0.10}
p_y_1 = {(0,0): 0.01, (0,1): 0.50, (1,0): 0.40, (1,1): 0.70}
p_y_0 = {(0,0): 0.99, (0,1): 0.50, (1,0): 0.60, (1,1): 0.30}

def joint_distribution(evidence):
    total = 0

    for (y,c,s), probability in p_y_c_s.items():
        configuration = {"Y": y, "C": c, "S": s}
        if all (configuration[key] == value for key, value in evidence.items()):
            total += probability

    return total


def conditional_probability(query, evidence):
    for name in query.keys() & evidence.keys():
        if query[name] != evidence[name]:
            raise ValueError("Contradictory query and evidence")

    denominator = joint_distribution(evidence)

    if denominator == 0:
        raise ValueError("Evidence has zero probability")

    combined = {**query, **evidence}
    numerator = joint_distribution(combined)

    return numerator / denominator


print(f"P(Y=1) from joint distribution = {joint_distribution({'Y': 1}):.4f}")
print(f"P(Y=1,C=1) from joint distribution = {joint_distribution({'Y': 1, 'C': 1}):.4f}")
print(f"P(C=1) from joint distribution = {joint_distribution({'C': 1}):.4f}")

result = conditional_probability({"C": 1}, {"Y": 1})
print(f"P(C=1|Y=1) from joint distribution = {result:.4f}")

result = conditional_probability({"Y": 1}, {"C": 0})
print(f"P(Y=1|C=0) = {result:.4f}")

result = conditional_probability({"Y": 1}, {"C": 1, "S": 1})
print(f"P(Y=1|C=1,S=1) = {result:.4f}")