# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:56:40 2019

@author: Marta
"""

from math import exp
import numpy as np

#DANE
S0 = 100.
K = 100.
r1 = 0.05
r2 = 0.1
T=1
n=2
b=3

S = np.ones([b**n,n+1])
(a,b) = np.shape(S)
for i in range (a):
    S[i,0] = S0
for i in range (b):
    S[i,1] = 115.
    S[i+b,1] = 100.
    S[i+b+b,1] = 90.
S[0,2] = 120.
S[1,2] = 105.
S[2,2] = 90.
S[3,2] = 110.
S[4,2] = 85.
S[5,2] = 97.
S[6,2] = 99.
S[7,2] = 95.
S[8,2] = 80.

#print(S)

for i in range(a):
    x = K-S[i,2]
    if (x>0):
        S[i,2] = x
    else:
        S[i,2] = 0

#oprocentowanie dl funkcji wypłaty (K-S)
def omega(S):
    r=0
    if(S<5):
        r = r2
    else:
        r = r1
    return r

#estymator gorny
def Theta(x):
    #for i in range(n):
    Theta = np.zeros(b**(n-1))
    for j in range(n+1):
        theta = 0
        for k in range(j*b,j*b+b):
            theta = theta + S[k,x+1]*exp(-omega(S[k,x+1])/n)
            #print(omega(S[i,x+1])) 
            y = K-S[k,x]
            #print (S[i,x],y,theta)
        if (y>theta/b):
            Theta[j] =  y
        else:
            Theta[j]=1/b*theta
    print(Theta)
    c = 0
    for i in range(3):
        c = c + Theta[i]*exp(-omega((K-S[i*b,1]))/n)
    h = K-S[0,0]
        #print(c,h)
    if(h>c/b):
        return h
    else:
        return round(c/b,2)
    #return Theta

print(S)
print(Theta(1))

def Phi(x):
    Phi=np.zeros(b**(n-1))
    vect = np.zeros(b)
    for j in range(b):
        suma = 0
        vect = np.zeros(b)
        for k in range(b):
            if (j != k):
                suma = suma+(S[k,x+1]*exp(-omega(S[k,x+1])))
            suma = suma/2
        f=K-S[j,x]
        if(suma>f):
            