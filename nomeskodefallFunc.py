#denne koden lÃ¸ser fallskjermlikningen numerisk med eksplisitt og implisitt euler

import numpy as np
def getVerdier():
    #t-aksen
    T=5
    N=100
    h=T/N
    t=np.linspace(0,T,N+1)

    #v er farten til en fallskjermhopper
    v=np.zeros(N+1)
    v[0]=0

    #velg metode her, 1 er EE og 2 er IE 
    metode=2
    iterasjonSum = 0
    for k in range(N):

        #eksplisitt
        if metode==1:
            v[k+1]=v[k]+h*(1-v[k]**2)
        
        #implisitt
        if metode==2:
            #eksplisitt euler er initialgjetning for fikspunktiterasjonen
            v[k+1]=v[k]+h*(1-v[k]**2)        
            z=100 # variabel som holder styr pÃ¥ konvergens til numerisk likningslÃ¸ser

            #newtons metode, se neste ukes Ã¸kt
            while np.abs(v[k+1]-z)>.0005:
                z=v[k+1]
                v[k+1]=v[k+1]-(v[k+1]-v[k]-h*(1-v[k+1]**2))/(1+2*h*(1-v[k+1])) 
                iterasjonSum+=1

    print(iterasjonSum/N)
    return t,v
