#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:10:20 2018

@author: janik
"""

from math import sin,pi
import numpy as np

interval = np.linspace(0,1,44000)

#a

def do(t):
    do = round(sin(220*2**(1/4)*2*pi*t))
    return (do).to_bytes(1,byteorder='big',signed = True)

def mi(t):
    mi = round(sin(220*2**(7/12)*2*pi*t))
    return (mi).to_bytes(1,byteorder='big',signed = True)

echantillon_do = []
for i in range (44000):
    echantillon_do.append(do(interval[i]))
    
echantillon_mi = []
for i in range (44000):
    echantillon_mi.append(mi(interval[i]))
    
ftierce = open('tierce.pcm','wb')
for i in range(44000):
    ftierce.write(echantillon_do[i])
    ftierce.write(echantillon_mi[i])
ftierce.close()

def accord(t):
    acc = sin(220*2**(1/4)*2*pi*t)+sin(220*2**(7/12)*2*pi*t)
    return (round(acc)).to_bytes(1,byteorder='big',signed = True)

echantillon_acc = []
for i in range (44000):
    echantillon_acc.append(accord(interval[i]))
    
f = open('accord.pcm','wb')
for i in range(44000):
    f.write(echantillon_acc[i])
f.close()



#b
def re(t):
    re = round(sin(220*2**(5/12)*2*pi*t))
    return (re).to_bytes(1,byteorder='big',signed = True)

def fa(t):
    fa = round(sin(220*2**(2/3)*2*pi*t))
    return (fa).to_bytes(1,byteorder='big',signed = True)

echantillon_re = []
for i in range (44000):
    echantillon_re.append(re(interval[i]))
    
echantillon_fa = []
for i in range (44000):
    echantillon_fa.append(fa(interval[i]))
    
ftierce2 = open('tierce2.pcm','wb')
for i in range(44000):
    ftierce2.write(echantillon_re[i])
    ftierce2.write(echantillon_fa[i])
ftierce2.close()