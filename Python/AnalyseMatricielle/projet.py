#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:36:34 2018

@author: janik
"""

import numpy as np

def Grad(M,P,b):
    (n,m) = np.shape(P)
    x = np.zeros(n)
    for i in range(n): # car Px = x (hypothèse)
        if(P[i,i] == 1):
            x[i] = 1

    ro = P.dot(b)- P.dot(M.dot(P.dot(x)))
    g = np.copy(ro)
    iteracja=0
    while(ro.any() != 0):
        a = P.dot(M.dot(P.dot(g)))
        h = ro.dot(ro)
        alfa = h/np.dot(a,g)
        newx = x+alfa*g
        newro = ro-alfa*a
        beta = np.dot(newro,newro)/h
        newg = newro+beta*g
        x = newx
        ro = newro
        g = newg
        iteracja+=1
    return(iteracja,ro,x)

M = np.array([[2.,-1.,0.,0.,0.],[-1.,2.,-1.,0.,0.],[0.,-1.,2.,-1.,0.],[0.,0.,-1.,2.,-1.],[0.,0.,0.,-1.,2.]])
P = np.array([[1.,0.,0.,0.,0.],[0.,0.,0.,0.,0.],[0.,0.,1.,0.,0.],[0.,0.,0.,1.,0.],[0.,0.,0.,0.,0.]])
b = np.array([2.,3.,5.,1.,1.]) 