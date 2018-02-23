from sympy import sqrt, Rational
from copy import deepcopy

j = 1 #Rational(1,2)
n = 3
initial = [-j]*n
c = [1]
psi = [initial]
def raising(states, coef):
    out_psi = []
    out_c = []
    for k in range(len(states)):
        for i in range(n):
            m = states[k][i]
            c = sqrt(j*(j+1)-m*(m+1))
            if c != 0:
                c = c*coef[k]
                temp = deepcopy(states[k])
                temp[i] = m + 1
                exist = False
                for found in range(len(out_psi)):
                    if temp == out_psi[found]:
                        out_c[found] = out_c[found] + c
                        exist = True
                        break
                if not exist:
                    out_psi.append(temp)
                    out_c.append(c)
    return [out_psi, out_c]
def lowering(states, coef):
    out_psi = []
    out_c = []
    for k in range(len(states)):
        for i in range(n):
            m = states[k][i]
            c = sqrt(j*(j+1)-m*(m-1))
            if c != 0:
                c = c*coef[k]
                temp = deepcopy(states[k])
                temp[i] = m - 1
                exist = False
                for found in range(len(out_psi)):
                    if temp == out_psi[found]:
                        out_c[found] = out_c[found] + c
                        exist = True
                        break
                if not exist:
                    out_psi.append(temp)
                    out_c.append(c)
    return [out_psi, out_c]
for i in range(3):
    [new_psi, new_c] = raising(psi, c)
    psi = new_psi
    c = new_c

for k in range(len(psi)):
    print c[k], psi[k]