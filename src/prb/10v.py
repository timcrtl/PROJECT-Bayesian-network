states = {
    "A": ["under_35", "35_or_more"],
    "P": ["0", "1", "2", "3_or_more"],
    "C": ["no", "yes"],
    "G": ["singleton", "twins"],
    "S": ["cephalic", "breech", "other"],
    "M": ["no", "yes"],
    "K": ["no", "yes"],
    "D": ["spontaneous", "induced", "caesarean_before_labour"],
    "Y": ["vaginal_non_instrumental", "vaginal_instrumental", "caesarean"],
    "I": ["not_applicable", "forceps", "spatulas", "vacuum"],
}

#for variable, possible_states in states.items():
    #print(f"{variable}: {possible_states}")

print(f"number of variables : {len(states)}")

parents = {
    "A": [],
    "P": [],
    "C": ["P"],
    "G": ["A"],
    "S": ["G"],
    "M": ["G"],
    "K": ["M"],
    "D": ["C", "S"],
    "Y": ["C", "S", "D"],
    "I": ["Y"],
}

for variable, parent_list in parents.items():
    print(f"list of parents for {variable} : {parent_list}")

# P(I | Y) p I given Y
p_i_given_y = {
    "normal_non_instrumental": {
        "not_applicable": 1.0,
        "forceps": 0.0,
        "spatulas": 0.0,
        "vacuum": 0.0,
    },

    "normal_instrumental": {
        "not_applicable": 0.0,
        "forceps": 318 / 1524,
        "spatulas": 289 / 1524,
        "vacuum": 917 / 1524,
    },

    "caesarean": {
        "not_applicable": 1.0,
        "forceps": 0.0,
        "spatulas": 0.0,
        "vacuum": 0.0,
    },
}

#print(f"P(I | Y) = {p_i_given_y['normal_instrumental']['forceps']}")
#print(f"P(I | Y) = {p_i_given_y['normal_instrumental']['spatulas']}")

for delivery_mode, probabilities in p_i_given_y.items():
    total =sum(probabilities.values())
    print(f"Total probability for {delivery_mode} = {total}")


#P(G | A) p G given A
p_g_given_a = {
    "under_35": {
        "singleton": 8983 / 9111,
        "twins": 128 / 9111,
    },

    "35_or_more":{
        "singleton": 2900/2968,
        "twins": 68/2968,
    },
    }

for age_group, probabilities in p_g_given_a.items():
    total =sum(probabilities.values())
    print(f"Total probability for {age_group} = {total}")

# P(A) 
p_a = {
    "under_35": 9111 / 12079,
    "35_or_more": 2968 / 12079
}

#print(f"P(G | A) = {p_g_given_a["under_35"]["singleton"]}")

# P(M | G)
p_m_given_g = {
    "singleton": {
        "no": (11803-503)/11803,
        "yes": 503/11803,
    },
    "twins":{
        "no": (195-66)/195,
        "yes": 66/195,  
    },
}

for pregnancy_type, probabilities in p_m_given_g.items():
    total = sum(probabilities.values())
    print(f"Total probability for {pregnancy_type} = {total}")

#print(f"P(M | G) = {p_m_given_g['singleton']['yes']}")
#print(f"P(M | G) = {p_m_given_g['singleton']['no']}")

#P(M=yes | A=under_35) 
p_m_yes_given_under_35 = (
    p_m_given_g["singleton"]["yes"]
    * p_g_given_a["under_35"]["singleton"]
    + p_m_given_g["twins"]["yes"]
    * p_g_given_a["under_35"]["twins"]
)

#print(f"P(M=yes | A=under_35) = {p_m_yes_given_under_35:.2%}")

p_m_yes_given_35_or_more = (
    p_m_given_g["singleton"]["yes"]
    * p_g_given_a["35_or_more"]["singleton"]
    + p_m_given_g["twins"]["yes"]
    * p_g_given_a["35_or_more"]["twins"]
)
#print(f"P(M=yes | A=35_or_more) = {p_m_yes_given_35_or_more:.2%}")

p_m_yes = (
    p_m_yes_given_under_35 * p_a["under_35"]
    + p_m_yes_given_35_or_more * p_a["35_or_more"]
)

p_m = {
    "no": 1 - p_m_yes,
    "yes": p_m_yes,
}

#print(f"P(M=yes) = {p_m['yes']:.2%}")
#print(f"P(M=no) = {p_m['no']:.2%}")
#print(f"Sum = {sum(p_m.values()):.6f}")

p_g_twins = (
    p_g_given_a["under_35"]["twins"] * p_a["under_35"]
    +
    p_g_given_a["35_or_more"]["twins"] * p_a["35_or_more"]
)

#print(f"P(G=twins) = {p_g_twins:.2%}")

p_g_twins_given_m_yes = (
    p_m_given_g["twins"]["yes"]
    * p_g_twins
    / p_m_yes
)

#print(f"P(G=twins | M=yes) = {p_g_twins_given_m_yes:.2%}")

p_g_twins_given_m_yes_under_35 = (
    p_m_given_g["twins"]["yes"]
    * p_g_given_a["under_35"]["twins"]
    / p_m_yes_given_under_35
)

def twins_given_map(age_group):
    # P(G=twins | M=yes, A=age_group)
    numerator = (
        p_m_given_g["twins"]["yes"]
        * p_g_given_a[age_group]["twins"]
    )

    denominator = (
        p_m_given_g["singleton"]["yes"]
        * p_g_given_a[age_group]["singleton"]
        + numerator
    )

    return numerator / denominator

for age_group in states["A"]:
    result = twins_given_map(age_group)
    print(f"P(G=twins | M=yes, A={age_group}) = {result:.2%}")


joint_a_g_m = {}

for a in states["A"]:
    for g in states["G"]:
        for m in states["M"]:
            joint_a_g_m[(a, g, m)] = (
                p_a[a]
                * p_g_given_a[a][g]
                * p_m_given_g[g][m]
            )

for configuration, probability in joint_a_g_m.items():
    print(f"{configuration}: {probability:.6f}")

print(f"Configurations: {len(joint_a_g_m)}")
print(f"Sum: {sum(joint_a_g_m.values()):.6f}")

def probability_a_g_m(evidence):
    total = 0

    for (a, g, m), probability in joint_a_g_m.items():
        configuration = {"A": a, "G": g, "M": m}

        if all(
            configuration[name] == value
            for name, value in evidence.items()
        ):
            total += probability

    return total

result = probability_a_g_m({"M": "yes"})
print(f"P(M=yes) = {result:.2%}")