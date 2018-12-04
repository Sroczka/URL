#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:43:13 2018

@author: janik
"""

from numpy import cos,sin,pi,exp,array,ones,dot

def s(t):
    s = 200 + 2*cos(500*pi*t)+10*cos(1000*pi*t)+3*sin(1500*pi*t)
    return(s)
    
p = 1/250

def s_exp(t):
    s = 200 + exp(1j*500*pi*t)+exp(-(1j*500*pi*t))+5*exp(1j*1000*pi*t)+5*exp(-(1j*1000*pi*t))+3/2*(-1j)*exp(1j*1500*pi*t)-3/2*(-1j)*exp(-(1j*1500*pi*t))
    return(s)

v = array([s_exp(0),s_exp(p/7),s_exp(2*p/7),s_exp(3*p/7),s_exp(4*p/7),s_exp(5*p/7),s_exp(6*p/7)])

v1 = array([s(0),s(p/7),s(2*p/7),s(3*p/7),s(4*p/7),s(5*p/7),s(6*p/7)])

w = exp(-(2*1j*pi/7))

A = array([w**3,w**4,w**5,w**7,w**8,w**9,w**10])

M = 1/7*array([ones(7),A,A**2,A**3,A**4,A**5,A**6]) #cos nie tak....

a = dot(M,v)
a1 = dot(M,v1)


########################
from scipy.linalg import dft

m = dft(7,scale='n')
b = dot(m,v) #ok
