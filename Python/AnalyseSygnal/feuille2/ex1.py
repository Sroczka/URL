#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:19:29 2018

@author: janik
"""

from math import sin,pi
import numpy as np

def do(t):
    do = round(sin(220*2**(1/4)*2*pi*t))
    return (do).to_bytes(1,byteorder='big',signed = True)

def re(t):
    re = round(sin(220*2**(5/12)*2*pi*t))
    return (re).to_bytes(1,byteorder='big',signed = True)

interval = np.linspace(0,1,44000)

echantillon_do = []
for i in range (44000):
    echantillon_do.append(do(interval[i]))    
for i in range (44000*2):
    if (i%2 != 0):
        echantillon_do.insert(i,(0).to_bytes(1,byteorder='big',signed = True))
    
echantillon_re = []
for i in range (44000):
    echantillon_re.append(re(interval[i]))    
for i in range (44000*2):
    if (i%2 == 0):
        echantillon_re.insert(i,(0).to_bytes(1,byteorder='big',signed = True))
        
fdo_re = open('do_re.pcm','wb')
for i in range(44000*2):
    fdo_re.write(echantillon_do[i])
for i in range(44000*2): #bez tej linijki odtwarza w tym samym czasie
    fdo_re.write(echantillon_re[i])
fdo_re.close()
    

#do odtworzenia:
#cvlc --demux=rawaud --rawaud-channels=2 --rawaud-salerate=44000
#--rawaud-fourcc "u8  " do_re.pcm
