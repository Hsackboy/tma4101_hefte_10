import numpy as np
import matplotlib.pyplot as plt
import nomeskodefallFunc as graf1
import func11019Func as graf2


x1,y1 = graf1.getVerdier()
x2,y2 = graf2.getVerdier()


plt.plot(x1,y1)
plt.plot(x2,y2)




plt.axvline(x=0, color="r", linestyle="--", label="x=0")
plt.axhline(y=0, color="b", linestyle="--", label="y=0")

plt.show()