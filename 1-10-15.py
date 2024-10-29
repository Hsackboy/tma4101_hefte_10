""""""

import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x + y - np.log(x) - np.log(y)


T = 20  # toppen av definisjonsområdet -> x:[0,T]
N = 2000  # iterasjoner
h = T / N  # lengde pr steg
t = np.linspace(0, T, N + 1)  # definisjonsområde som liste med N+1 antall elementer
x = np.zeros(N + 1)  # tomme x verdier
y = np.zeros(N + 1)  # tomme y verdier
x[0] = 2  # starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
y[0] = 2  # starter på y0 = 2

for n in range(N):
    x[n + 1] = x[n] + h * x[n] * (1 - y[n])
    y[n + 1] = y[n] + h * y[n] * (x[n+1] - 1)


fVerdier = f(x,y)

plt.xlabel("t")
plt.ylabel("x/y")
plt.plot(t, fVerdier)  # plotter t som horisontal-akse og x som vertikal-akse
plt.plot(t, y)  # plotter t som horisontal-akse og x som vertikal-akse
plt.plot(t, x)  # plotter t som horisontal-akse og x som vertikal-akse
plt.axvline(x=0, color="r", linestyle="--", label="x=0")

# Add horizontal line at y = 0
plt.axhline(y=0, color="b", linestyle="--", label="y=0")
plt.show()

plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(x=0, color="r", linestyle="--", label="x=0")

# Add horizontal line at y = 0
plt.axhline(y=0, color="b", linestyle="--", label="y=0")
plt.plot(x, y)  # plotter x på horisontal akse og y på vertikal akse
plt.show()
