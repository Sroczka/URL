#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:09:34 2018

@author: janik
"""

import math

class Complex:
    def __init__(self,x,y):
      self.x = x
      self.y = y

    def module(self):
      return math.sqrt(self.x**2 + self.y**2)
  
    def __str__(self):
        if self.y>0:
            return f"{self.x}+{self.y}i"
        elif self.y<0:
            return f"{self.x}{self.y}i"
        else:
            return str(self.x)

  #z = Complex()     # TypeError: __init__() takes exactly 3 arguments (1 given)  

z = Complex(1,2)
print(z)
  #print(z.module())
  
#  def __eq__(self,z):
#      return self.x==z.x and self.y==z.y
#
#  def __add__(self,z):
#      return Complex(self.x+z.x, self.y+z.y)

#  def __mul__(self,z):
#      return Complex(self.x*z.x-self.y*z.y, self.x*z.y+self.y*z.x)

#def __add__(self,z):
#    if isinstance(z,Complex):c #sprawdza czy  jest tego samego typu
#      return Complex(self.x+z.x, self.y+z.y)
#    elsif isinstance(z,int) or isinstance(z,float):
#      return Complex(self.x+z, self.y)
#    else
#      raise RuntimeError("opération non prévue")


###########################
#ex 2
    
class Rationnel:
    def __init__(self,x,y):
        if y == 0:
            raise RuntimeError("mianownik 0")
        else:
            self.x = x
            self.y = y
      
    def val(self):
        return(round(self.x/self.y, 2))
        
    def inverse(self):
        #r = Rationnel(self.x,self.y)
        #r.x = self.x
        #r.y = self.y
        #return (round(1/(r.x/r.y), 2))
        return Rationnel(self.y,self.x)
    
    def __str__(self):
        if self.x == self.y:
            return "1"
        elif (self.y>0 and self.y != 1):
            return f"{self.x}/{self.y}"
        elif self.y == 1:
            return str(self.x)
        elif self.y == -1:
            return f"-{self.x}"
        else:
            return f"-{self.x}/{-self.y}"
    
    def __eq__(self,r):
        return self.x == r.x and self.y == r.y
    
    def __add__(self,r):
        if isinstance(r,Rationnel):
            if self.y == r.y:
                return Rationnel(self.x + r.x, self.y)
            else:
                return Rationnel(self.x*r.y + self.y*r.x, self.y*r.y)
        elif isinstance(r,int):
            return Rationnel(self.x + r*self.y, self.y)
        else:
            raise RuntimeError("opération non prévue")
    
    def __mul__(self,r):
        return Rationnel(self.x*r.x, self.y*r.y)
    
    def __truediv__(self,r):
        return Rationnel(self.x*r.y, self.y*r.x)
    
    def __sub__(self,r):
        if self.y == r.y:
            return Rationnel(self.x - r.x, self.y)
        else:
            return Rationnel(self.x*r.y - self.y*r.x, self.y*r.y)
    
a = Rationnel(1,-3)
print(a.val())
#b = a.inverse()
#print(b.val())

print((a.inverse()).val())
print(a)
print(a.inverse())

r1 = Rationnel(3,4)
r2 = Rationnel(3,5)
r3 = Rationnel(3,4)

print(r1==r3) 
print(r1+r3)
print(r1-r2)
print(r1*r2==r2*r3)
print(r1/r2)
print(r3/r1)
print(r1+1)