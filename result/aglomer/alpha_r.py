from matplotlib import pyplot as plt
with open('dendro_ward.txt','r') as file:
    StrF = file.read()
StrF1 = StrF[StrF.index('1-th'):StrF.index('2-th')]
StrF1 = StrF1[StrF1.index('['):]
StrF2 = StrF[StrF.index('2-th'):StrF.index('3-th')]
StrF2 = StrF2[StrF2.index('['):]
StrF3 = StrF[StrF.index('3-th'):]
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

print(r[2])
ch_alpha = [alpha[2][i] for i in range(len(r[2])) if r[2][i] < 1]
ch_r = [r[2][i] for i in range(len(r[2])) if r[2][i] < 1]

#plt.scatter(alpha[1], r[1], marker='o', color='r')
plt.scatter(ch_alpha, ch_r, marker='o', color='b')
#plt.scatter(alpha[0], r[0], marker='o', color='g')
plt.grid()
plt.show()
