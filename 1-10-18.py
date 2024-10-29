"""
symplektisk
"""

import numpy as np
import matplotlib.pyplot as plt


def xDer(x):
    return x


def approxXkPluss1(xk_1, xk_0, h, tolorance=0.0005):
    prevXk_1 = 100
    iterations = 0
    while abs(prevXk_1 - xk_1) > tolorance:
        prevXk_1 = xk_1
        xk_1 = xk_0 + (h / 2) * (xDer(xk_0)+xDer(xk_1))
        iterations+=1
    return xk_1,iterations

T=5
N=100
h = T / N  # lengde pr steg
t = np.linspace(0, T, N + 1)  # definisjonsområde som liste med N+1 antall elementer
x = np.zeros(N + 1)  # tomme x verdier


x[0] = 1  # starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
# y[0] = -0.530 #starter på y0 = 2
##justerte startverdier siden den trengte tid til å stabilisere seg
iterationSUm = 0
for n in range(N):
    x[n + 1] = x[n] + h * xDer(x[n])
    x[n + 1],iterationReturn = approxXkPluss1(x[n+1],x[n],h)
    iterationSUm+=iterationReturn

plt.xlabel("t")
plt.ylabel("x")
plt.plot(t, x,label ="numerisk")  # plotter t som horisontal-akse og x som vertikal-akse


plt.axvline(x=0, color="r", linestyle="--", label="x=0")


# print(x[1000])
print(iterationSUm/N)


# Add horizontal line at y = 0
plt.axhline(y=0, color="b", linestyle="--", label="y=0")




#denne koden lÃ¸ser ecoliproblemet med forskjellige numeriske metoder og sammenlikner med analytisk lÃ¸sning

#x er analytisk lÃ¸sning 
T=5
N=1000
h=T/N
t=np.linspace(0,T,N+1)
x=np.exp(t)

#plotte analytisk lÃ¸sning
plt.plot(t,x,label ="fasit")

# #nytt gitter med fÃ¦rre punkter
# N=20
# h=T/N
# t=np.linspace(0,T,N+1)

# #y er eksplisitt euler
# y=np.zeros(N+1)
# y[0]=1

# #z er implisitt euler
# z=np.zeros(N+1)
# z[0]=1

# #v er trapesmetoden
# v=np.zeros(N+1)
# v[0]=1

# for k in range(N):
#     y[k+1]=(1+h)*y[k]
#     z[k+1]=z[k]/(1-h)
#     v[k+1]=(2+h)*v[k]/(2-h)
      
# plt.plot(t, y)
# plt.plot(t, z)
# plt.plot(t, v)

plt.legend()
plt.show()