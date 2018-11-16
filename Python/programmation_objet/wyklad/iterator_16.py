#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:06:14 2018

@author: janik
"""

#szuka wszystkich wielokrotnosci

class A:
    def __init__(self,premier):
        self.premier = premier
        self.etat = 0
        
    def __iter__(self):
        return B(self)
    
    def multiple(self):
        self.etat += 1
        if( self.etat<100):
            if (self.etat%self.premier == 0): return self.etat
            else: return None
        else: raise StopIteration("fin d'itération")
        
class B:
    def __init__(self,a):
        self.a = a
    def __next__(self):
        return a.multiple()
    
a = A(29)

for i in a:
    if i is not None: #jak inaczej ominac wyswietlanie None
        print(i)
        
############inaczej
#mozna z while, try i except
        
#szuka wielokrotosci w liscie        
        
class Multiple:
    def __init__(self,l):
        self.l = l
        
    def __iter__(self):
        return It(self)
    
class It:
    def __init__(self,m):
        self.m = m
        self.i = -1
        
    def __next__(self):
        try:
            while True:
                self.i += 1
                if self.m.l[self.i] % self.m.l[0] == 0:
                    return(self.m.l[self.i])
                    
        except IndexError:
            raise StopIteration("fin d'itération")
            
m = Multiple([2,3,4,5,6,7])

for i in m:
    for j in m:
        print(f"{i} {j}")