#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:06:14 2018

@author: janik
"""

#szuka wszystkich wielokrotnosci

class A:
    def __init__(self,liste):
        self.liste = liste
        
    def __iter__(self):
        return B(self)
        
class B:
    def __init__(self,a):
        self.a = a
        self.i = -1
        
    def __next__(self):
        try:
            while True:
                self.i += 1
                if (self.a.liste[self.i]%self.a.liste[0] == 0):
                    return (self.a.liste[self.i])
            
        except IndexError:
            raise StopIteration("fin d'itération")
    
            
a = Multiple([2,3,4,5,6,7])

for i in a:
    for j in a:
        print(f"{i} {j}")