#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:37:38 2018

@author: janik
"""

#rekurencja

def fact(n):  #silnia
    if n == 0:
        return 1
    return n * fact(n-1)
        