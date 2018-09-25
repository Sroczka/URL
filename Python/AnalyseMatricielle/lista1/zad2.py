#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 08:08:12 2018

@author: janik
"""

import numpy as np

def Gauss1(A):
    (n,m) = np.shape(A)
    T = np.copy(A)
    for k in range(n-1):
        pivot = T[k,k]
        for i in range(k+1,n):
            t = - T[i,k]/pivot
            T[i,] = T[i,] + T[k,] * t
            print(T)
    return T
        

A = np.array([[2.,1.,1.],[1.,2.,1.],[1.,1.,2.]])