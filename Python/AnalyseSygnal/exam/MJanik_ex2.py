#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:21:10 2019

@author: janik
"""
import numpy as np

def h(n):
    h = np.zeros(n)
    for i in range(10):
        h[i]=i
    return(h)
    
h = h(100)

n = np.convolve(h,h)

print(f"h*h = {n[0:19]} \n et aprés 0")