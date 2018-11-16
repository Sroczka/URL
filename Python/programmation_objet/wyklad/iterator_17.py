#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:11:33 2018

@author: janik
"""

class Somme:
    def __init__(self,l):
        self.l = l
        
    def __iter__(self):
        return It(self)
    
class It:
    def __init__(self,liste):
        self.liste = liste
        self.i = 0
        self.somme = 0
        
    def __next__(self):
        
        try:
            self.somme += self.liste.l[self.i]
                    
        except IndexError:
            raise StopIteration("fin d'itération")
        
        self.i += 1
        return(self.somme)
        
s = Somme([2,3,4,5,6,7])
for i in s:
    for j in s:
        print(f"{i} {j}")