# C = History of caesarean (0 = no, 1 = yes)
# S = Sitting position (0 = no, 1 = yes, no answer = we cannot determine) 
# Y = Caesarean at current delivery (0 = no, 1 = yes)

p_c = {0: 0.8, 1: 0.2}
p_s = {0: 0.90, 1: 0.10}
p_y_1 = {(0,0): 0.01, (0,1): 0.50, (1,0): 0.40, (1,1): 0.70}
p_y_0 = {(0,0): 0.99, (0,1): 0.50, (1,0): 0.60, (1,1): 0.30}

#The probability of a caesarean at the current delivery, given no previous caesarean, with the baby’s current presentation unknown.
p_y1_c0 = p_y_1[(0,0)]*p_s[0] + p_y_1[(0,1)]*p_s[1]
print(f"P(Y=1|C=0) = {p_y1_c0 :.4f}")

#The probability of a caesarean at the current delivery, given a previous caesarean, with the baby’s current presentation unknown.
p_y1_c1 = p_y_1[(1,0)]*p_s[0] + p_y_1[(1,1)]*p_s[1]
print(f"P(Y=1|C=1) = {p_y1_c1 :.4f}")

#The probability of a caesarean at the current delivery, regardless of previous caesarean status.
p_y1 = p_y1_c0*p_c[0] + p_y1_c1*p_c[1]
print(f"P(Y=1) = {p_y1 :.4f}")

#the probability of a natural birth at the current delivery, regardless of previous caesarean status.
p_y0 = 1 - p_y1
print(f"P(Y=0) = {p_y0 :.4f}")

#probability of a previous caesarean, given a caesarean at the current delivery.
p_c1_y1 = p_y1_c1*p_c[1]/p_y1
print(f"P(C=1|Y=1) = {p_c1_y1 :.4f}")


#Joint distribtion P(Y,C,S)
p_y_c_s = {}

for y in [0, 1]:
    for c in [0, 1]:
        for s in [0, 1]:
            if y == 1:
                p_y_c_s[(y, c, s)] = p_y_1[(c, s)] * p_c[c] * p_s[s]
            else:
                p_y_c_s[(y, c, s)] = p_y_0[(c, s)] * p_c[c] * p_s[s]

for configuration, probability in p_y_c_s.items():
    print(f"P(Y, C, S) = {configuration} : {probability:.4f}")

print(f"Somme = {sum(p_y_c_s.values()):.4f}")

#Now we can calculate the probability from the joint distribution P(Y,C,S) to get the conditional probability P(C=1|Y=1,S=1) or P(C=1|Y=1,S=0) or P(C=1|Y=0,S=1) or P(C=1|Y=0,S=0)
#Lets calculate P(Y=1)
p_y1_joint = 0
for (y, c, s), probability in p_y_c_s.items():
    if y == 1:
        p_y1_joint += probability

print(f"P(Y=1) from joint distribution = {p_y1_joint:.4f}")

#Lets calculate P(C=1|Y=1)
# Calculate P(C=1, Y=1).
p_c1_and_y1 = 0

for (y, c, s), probability in p_y_c_s.items():
    if y == 1 and c == 1:
        p_c1_and_y1 += probability

# Calculate P(C=1 | Y=1).
p_c1_given_y1 = p_c1_and_y1 / p_y1_joint

print(f"P(C=1|Y=1) from joint distribution = {p_c1_given_y1:.4f}")