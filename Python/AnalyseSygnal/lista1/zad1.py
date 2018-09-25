#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:35:44 2018

@author: janik
"""

#a

(1000).to_bytes(2,byteorder='little',signed = False)

#b

f = open('data.pcm','wb')
f.write((1000).to_bytes(2,byteorder='big'))
f.write((2000).to_bytes(2,byteorder='big'))
f.close()

#c

#terminal

#d
from math import sin,pi

def s(t):
    s = (sin(440*2*pi*t)+1)*255/2
    return s

def u(t):
    u = round(s(t))
    return u.to_bytes(16,byteorder='big',signed = True)
    
#e

import numpy as np

#max_s = s(0)
#min_s = s(0)
#for t in range(0,100):
#    if (s(t)>max_s):
#        max_s = s(t)
#    elif (s(t)<min_s):
#        min_s1 = s(t)
#A = [max_s, min_s]
#print (A)

echantillon = []
interval = np.linspace(0,1,44000)
for i in range (44000):
    echantillon.append(interval[i])

#f

#u.max_s = u(max_s)
#u.min_s = u(min_s)
#print (u(max_s), u(min_s))

echantillon2 = []
for i in range (44000):
    echantillon2.append(u(echantillon[i]))
#g
fn = open('la.pcm','wb')
for i in range(len(echantillon2)):
    fn.write(echantillon2[i])
fn.close()
