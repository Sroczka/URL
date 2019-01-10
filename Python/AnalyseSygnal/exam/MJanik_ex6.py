#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:24:36 2019

@author: janik
"""

import numpy as np

def filtre(S):
    a = np.zeros(100)
    for i in range(50):
        a[i]=1
    T = a*S
    return(T)

S = np.ones(100)
    
print(f"pour S = [1,1,1,...,1,1] \n filtre(S) et égal à \n {filtre(S)}")