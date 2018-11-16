#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:42:30 2018

@author: janik
"""

class A:
    def __init__(self):
        self.etat = 0
        
    def __iter__(self):
        return B(self)

    def mb(self):
       self.etat += 1
       if (self.etat==1): return 'Chico'
       elif (self.etat==2): return 'Harpo'
       elif (self.etat==3): return 'Groucho'
       elif (self.etat==4): return 'Gummo'
       elif (self.etat==5): return 'Zeppo'
       else: raise StopIteration("fin d'itération")
       
class B:
    def __init__(self,a):
        self.a = a
    def __next__(self):
        return a.mb()

a = A()

for i in a:
    print(i)