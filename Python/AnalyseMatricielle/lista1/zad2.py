#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:08:12 2018

@author: janik
"""

import numpy as np
import zad1

def Gauss1(A):
    (n,m) = np.shape(A)
    T = np.copy(A)
    for k in range(n-1):
        pivot = T[k,k]
        for i in range(k+1,n):
            t = - T[i,k]/pivot
            T[i,] = T[i,] + T[k,] * t
            #print(T)
    return T
        

A = np.array([[1.,1.,1.],[1.,2.,3.],[3.,2.,3.]])
b = np.array([1.,1.,1.])

##############################################
def Gauss2(A,b):
    T = np.c_[A,b]
    T = Gauss1(T)
    (x,y) = np.shape(T)
    B = T[:,y-1]
    T = np.delete(T, y-1,1)
    x = zad1.remontee(T,B)
    return (T,x)