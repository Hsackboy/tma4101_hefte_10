"""
symplektisk
"""

import numpy as np
import matplotlib.pyplot as plt


def xDer(x):
    return 2-x

def approxXkPluss1(xk_1, xk_0, h, tolorance=0.0005):
    prevXk_1 = 100
    iterations = 0
    while abs(prevXk_1 - xk_1) > tolorance:
        prevXk_1 = xk_1
        xk_1 = xk_0 + (h / 2) * (xDer(xk_0)+xDer(xk_1))
        iterations+=1
    return xk_1,iterations

T=5
N=50
h = T / N  # lengde pr steg
t = np.linspace(0, T, N + 1)  # definisjonsområde som liste med N+1 antall elementer
x = np.zeros(N + 1)  # tomme x verdier
y = np.zeros(N + 1)  # tomme x verdier


x[0] = 1/10  # starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
y[0] = 1/10  # starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
# y[0] = -0.530 #starter på y0 = 2
##justerte startverdier siden den trengte tid til å stabilisere seg
iterationSUm = 0
for n in range(N):
    x[n + 1] = x[n] + h * xDer(x[n])
    x[n + 1],iterationReturn = approxXkPluss1(x[n+1],x[n],h)
    iterationSUm+=iterationReturn
    y[n+1] = y[n]+h*xDer(y[n])

plt.xlabel("t")
plt.ylabel("x")
plt.plot(t, x,label="implisitt")  # plotter t som horisontal-akse og x som vertikal-akse
plt.plot(t, y,label="explisitt")  # plotter t som horisontal-akse og x som vertikal-akse


plt.axvline(x=0, color="r", linestyle="--", label="x=0")


# print(x[1000])
print(iterationSUm/N)


# Add horizontal line at y = 0
plt.axhline(y=0, color="b", linestyle="--", label="y=0")

funk = -(19/10)*np.exp((-1)*t) +2
plt.plot(t,funk,label="Rett")
plt.legend()
plt.show()