#
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
    s = sin(440*2*pi*t)
    return s

def u(t):
    u = round(s(t))
    return (u).to_bytes(1,byteorder='big',signed = True)
    
#e

import numpy as np

echantillon = []
interval = np.linspace(0,1,44000)
for i in range (44000):
    echantillon.append(s(interval[i]))

#f


echantillon2 = []
for i in range (44000):
    echantillon2.append(u(interval[i]))
#g
fn = open('la.pcm','wb')
for i in range(44000):
    fn.write(echantillon2[i])
fn.close()