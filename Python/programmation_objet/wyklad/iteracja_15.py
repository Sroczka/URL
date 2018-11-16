#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:10:23 2018

@author: janik
"""

class SerieGeom():
    def __init__(self,i,r,m):
        self.i = i
        self.r = r
        self.m = m
        self.somme = 0
        
    def __iter__(self):
        return self
    
    def __next__(self): #m = suma
        self.i = self.i * self.r
        self.somme += self.i
        if self.somme>self.m:
            raise StopIteration("fin d'itération")
        return self.somme
    
ma_serie = SerieGeom(1,2,100)
for s in ma_serie:
    print(s)