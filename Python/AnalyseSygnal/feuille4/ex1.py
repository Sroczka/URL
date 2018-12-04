#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:43:13 2018

@author: janik
"""

from numpy import cos,sin,pi,exp,array

def s(t):
    s = 200 + 2*cos(500*pi*t)+10*cos(1000*pi*t)+3*sin(1500*pi*t)
    return(s)
    
p = 1/250

def s_exp(t):
    s = 200 + exp(1j*500*pi*t)+exp(-(1j*500*pi*t))+5*exp(1j*1000*pi*t)+5*exp(-(1j*1000*pi*t))+3/2j*exp(1j*1500*pi*t)-3/2j*exp(-(1j*1500*pi*t))
    return(s)

v = array([s_exp(0),s_exp(p/7),s_exp(2*p/7),s_exp(3*p/7),s_exp(4*p/7),s_exp(5*p/7),s_exp(6*p/7)])

from scipy.linalg import dft

m = dft(7)
A = m.dot(v) #liczy dft x
