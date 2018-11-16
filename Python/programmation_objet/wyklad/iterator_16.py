#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:06:14 2018

@author: janik
"""

class A:
    def __init__(self,premier):
        self.premier = premier
        self.etat = premier
        
    def __iter__(self):
        return B(self)
    
    def multiple(self):
        self.etat += 1
        if (self.etat%self.premier == 0 and self.etat<50): return self.etat
        if ((self.etat%self.premier == 1 or self.etat%self.premier == 2) and self.etat<50): return None
        else: raise StopIteration("fin d'itération")
        
class B:
    def __init__(self,a):
        self.a = a
    def __next__(self):
        return a.multiple()
    
a = A(3)

for i in a:
    print(i)