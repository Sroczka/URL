#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:41:59 2019

@author: janik
"""
import numpy as np

def f(n):
    l = list(np.linspace(0,n,n))
    for i in range(len(l)):
        l[i] = int(l[i])
    for i in range(round(n)):
        if (len(l)>1):
            noir = l[i]
            l.remove(noir)
            print(noir)
    #return(l[0])
    
        