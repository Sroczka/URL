#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:01:20 2018

@author: janik
"""

f = lambda x: (3*x+1)/(2*x+1)

def iteration(x,f,n):
    a = 1
    liste = [a]
    for i in range(n):
        liste.append(f(liste[-1]))
    return liste 

import math
from math import sqrt

def est_premier(n):
    if(n>1):
        for i in range(2,math.floor(sqrt(n)+1)):
            if(n%i==0):
                return False
        return True
    else:
        return False
    
def liste_premier(n):
    l = []
    for i in range(n):
        if(est_premier(i)==True):
            l.append(i)
    return l

#def liste_premier2(n):
#    l=[]
#    for i in range(len(l)):
#        if(n%l[i] != 0):
#            if(est_premier(i)==True):
#                l.append(i)
#    return l


import numpy as np

x=[1,2,3]
x = np.array(x)
y=[4,5,7]
y= np.array(y)
x+y #dodawanie list

def square_root(l):
    newlist = []
    for i in l:
        newlist.append(math.sqrt(i))
    return newlist

# %timeit - zliczanie czasu
     
m = np.array([[1,2,3],[4,5,6],[7,8,9]]) # macierz
m.dot(m)