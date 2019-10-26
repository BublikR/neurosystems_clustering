from matplotlib import pyplot as plt
with open('new_results_lok.txt','r') as file:
    StrF = file.read()
StrF1 = StrF[StrF.index('1-й'):StrF.index('2-й')]
StrF1 = StrF1[StrF1.index('['):]
StrF2 = StrF[StrF.index('2-й'):StrF.index('3-й')]
StrF2 = StrF2[StrF2.index('['):]
StrF3 = StrF[StrF.index('3-й'):]
StrF3 = StrF3[StrF3.index('['):]
L1 = eval(StrF1)
L2 = eval(StrF2)
L3 = eval(StrF3)

alpha = []
r = []

for i in [L1,L2,L3]:
    alpha_temp = []
    r_temp = []
    for j in i:
        alphat = j.index('alpha=')
        rt = j.index('-r=')
        temp_a = j[alphat+6:rt]
        temp_r = j[rt+3:j.index('-epsilon=')]
        try:
            alpha_temp.append(float(temp_a))
        except:
            continue
        r_temp.append(float(temp_r))
    alpha.append(alpha_temp)
    r.append(r_temp)

plt.scatter(alpha[0], r[0], marker='o', color='g')
plt.scatter(alpha[1], r[1], marker='o', color='r')
plt.scatter(alpha[2], r[2], marker='o', color='b')
plt.grid()
plt.show()
