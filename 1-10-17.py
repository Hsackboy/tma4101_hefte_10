"""
symplektisk
"""


import numpy as np
import matplotlib.pyplot as plt

def xDerivert(x,y):
    return y



def yDerivert(x,y):
    return -2*(x**2 -1)*y -x



T = 20 #toppen av definisjonsområdet -> x:[0,T]
N = 2000 #iterasjoner
h = T / N #lengde pr steg
t = np.linspace(0, T, N + 1) # definisjonsområde som liste med N+1 antall elementer
x = np.zeros(N + 1) #tomme x verdier
y = np.zeros(N + 1) #tomme y verdier
x[0] = -1.097 #starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
y[0] = 0.82 #starter på y0 = 2 
# x[0] = 1.44 #starter på x0 = 2 valgt tilfeldig? gir andre grafer fra start punkt
# y[0] = -0.530 #starter på y0 = 2 
##justerte startverdier siden den trengte tid til å stabilisere seg

for n in range(N):
    x[n + 1] = x[n] + h * xDerivert(x[n],y[n])
    y[n + 1] = y[n] + h * yDerivert(x[n+1],y[n])


plt.xlabel("t")
plt.ylabel("x/y")
plt.plot(t, x) #plotter t som horisontal-akse og x som vertikal-akse
plt.plot(t, y)#plotter t som horisontal-akse og y som vertikal-akse

plt.axvline(x=0, color='r', linestyle='--', label='x=0')


print(x[1000])
print(y[1000])

# Add horizontal line at y = 0
plt.axhline(y=0, color='b', linestyle='--', label='y=0')
plt.show()

plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(x=0, color='r', linestyle='--', label='x=0')

# Add horizontal line at y = 0
plt.axhline(y=0, color='b', linestyle='--', label='y=0')
plt.plot(x, y) # plotter x på horisontal akse og y på vertikal akse
plt.show()
