#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:09:01 2018

@author: janik
"""

def remontee(A,b):
    n = len(b)
    B = np.copy(b)
    #b[n-1] = b[n-1]/A[n-1,n-1]
    for i in range(n-1,-1,-1):
        for k in range(i+1,n):
            B[i] = B[i] - A[i,k] * B[k]
           #B[i] =  B[i] - np.dot(A[i,i+1:n],B[i+1,n])
        B[i] = B[i]/A[i,i]
    return B

def descente(A,b):
    # resout le systeme triangulaire inferieur Ax=b
    (n,m)=np.shape(A)
    B=np.copy(b)
    for i in range (0,n):# attention 
        B[i]=B[i]-np.dot(A[i,0:i],B[0:i])# attention 
        B[i]=B[i]/A[i,i]
    return B


###########essai

import numpy as np
import scipy.linalg as lg

A = np.array([[1.,2.,3.],[0.,5.,6.],[0.,0.,9.]])  #kropki, zeby nie zaokraglac
b = np.array([0.,2.,3.])
x = remontee(A,b)
#print(np.dot(A,x)-b)
np.allclose(np.dot(A,x),b)
lg.norm(np.dot(A,x)-b)

n = 10        
A = n*np.random.rand(n,n)
A = np.triu(A)
b = np.random.rand(n,1)
x = remontee(A,b)
#print(np.dot(A,x)-b)
np.allclose(np.dot(A,x),b) #porownuje dwa elementy

x = lg.solve(A,b) #rozwiazuje

#######################