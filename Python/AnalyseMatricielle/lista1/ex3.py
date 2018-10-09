#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:20:44 2018

@author: janik
"""

import numpy as np
import zad2


def LU1(A):
    (n,m) = np.shape(A)
    T = zad2.Gauss1(A)
    U = np.triu(T)
    L = U-T+np.eye(n)
    return [L,U]

#################################
    
def LU2(A):
    (n,m) = np.shape(A)
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    for i in range (n):
        L[i,i] = 1
    for j in range(n):
        for k in range(j,n):
            U[j,k] = A[j,k]-np.dot(L[j,0:j],U[0:j,k])
        for k in range (j+1,n):
            L[k,j] = 1/U[j,j] * (A[k,j] - np.dot(L[k,0:j], U[0:j,j]))
    return [L,U]

A = np.array([[2.,1.,1.],[1.,2.,1.],[1.,1.,2.]])