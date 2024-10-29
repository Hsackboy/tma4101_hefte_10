"""
symplektisk
"""

import numpy as np



def xDer(x):
    return 1 - x**2


def approxXkPluss1(xk_1, xk_0, h, tolorance=0.0005):
    prevXk_1 = 100
    iterations = 0
    while abs(prevXk_1 - xk_1) > tolorance:
        prevXk_1 = xk_1
        # xk_1 = xk_0 + (h / 2) * (xDer(xk_0)+xDer(xk_0+h*xDer(xk_0)))
        # xk_1 = xk_0 + (h / 2) * (xDer(xk_0)+xDer(xk_1))
        xk_1 = xk_0 + h*xDer((xk_1+xk_0)/2)
        iterations+=1
    return xk_1,iterations

def getVerdier():
    T=5
    N=100
    h = T / N  # lengde pr steg
    t = np.linspace(0, T, N + 1)  # definisjonsområde som liste med N+1 antall elementer
    x = np.zeros(N + 1)  # tomme x verdier


    x[0] = 0  # starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
    # y[0] = -0.530 #starter på y0 = 2
    ##justerte startverdier siden den trengte tid til å stabilisere seg
    iterationSUm = 0
    for n in range(N):
        x[n + 1] = x[n] + h * xDer(x[n])
        x[n + 1],iterationReturn = approxXkPluss1(x[n+1],x[n],h)
        iterationSUm+=iterationReturn
    print(iterationSUm/N)
    return t,x
