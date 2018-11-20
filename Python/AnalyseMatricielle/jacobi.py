#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 08:01:55 2018

@author: janik
"""

import numpy as np
from numpy import linalg as lg

def Jacobi1(A,b,n):
    (N,M) = np.shape(A)
    x = np.zeros(N)
    k = 1
    while(k<n):
        new_x = np.zeros(N)
        for i in range(N):
            new_x[i] = (b[i] - np.dot(A[i,:],x) + np.dot(A[i,i],x[i]))/A[i,i]
        x = new_x
        k+=1
    return(x)
    
A = np.array([[4.,-2.,1.],[1.,-3.,2.],[-1.,2.,6.]])
b = np.array([1.,2.,3.]) 

##########################################################################

def Jacobi(A,b,n,tol):
    (N,M) = np.shape(A)
    x = np.zeros(N)
    k = 1
    while(k<n):
        new_x = np.zeros(N)
        for i in range(N):
            new_x[i] = (b[i] - np.dot(A[i,:],x) + np.dot(A[i,i],x[i]))/A[i,i]
        a = lg.norm(new_x - x)
        if (a>tol):
            x = new_x
            k+=1
        else:
            break
    return(x,k)
    
    
#########################################################################
    
def Jacobi2(A,b,n,tol):
    (N,M) = np.shape(A)
    x = np.zeros(N)
    k = 1
    while(k<n):
        new_x = np.zeros(N)
        for i in range(N):
            new_x[i] = (b[i] - np.dot(A[i,:],x) + np.dot(A[i,i],x[i]))/A[i,i]
        r = np.dot(A,new_x) - b
        r = lg.norm(r)
        if (r>tol):
            x = new_x
            k+=1
        else:
            break
    return(x,k)