#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:54:37 2019

@author: janik
"""
import numpy as np
import scipy.linalg as lg
from math import pi,exp


S = np.array([6,6.76,-6.94,4.47,-0.29])
t = np.zeros(5)
for i in range(5):
    t[i] = i/(200*pi)
    
w = exp(1/(2*pi))

P = np.array([[1,w*(-2),w*(-4),w*(-6),w*(-8)],[1,w*(-1),w*(-2),w*(-3),w*(-4)],\
               [1,1,1,1,1],[1,w*1,w*2,w*3,w*4],[1,w*2,w*4,w*6,w*8]])
    
P = P.transpose()
Q = lg.inv(P)

D = np.dot(Q,S)



