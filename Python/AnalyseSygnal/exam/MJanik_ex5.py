#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:11:38 2019

@author: janik
"""
from cmath import exp
from math import pi
import numpy as np

def valeurSignal(c,f,t):
    signal = 0
    for i in range(-3,4):
        signal += c[i+3]*exp(2j*pi*i*f*t)
    return(signal)
    
c = np.array([0,0,0,1,1,0,0,0])
t = 1
f = 100    
    
print(valeurSignal(c,f,t))