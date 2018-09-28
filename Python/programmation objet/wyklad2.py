#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:09:34 2018

@author: janik
"""

import math

class Complex:
  def module(self):
    return math.sqrt(self.x**2 + self.y**2)

  def conjugue(self):
    c = Complex()
    c.x = self.x
    c.y = -self.y
    return c


class Complex:
    def __init__(self,x,y):
      self.x = x
      self.y = y

    def module(self):
      return math.sqrt(self.x**2 + self.y**2)

  z = Complex()     # TypeError: __init__() takes exactly 3 arguments (1 given)  

  z = Complex(1,2)
  print(z.module())


###########################
#ex 3
    
class Rationnel:
    def __init__(self,x,y):
      self.x = x
      self.y = y
      
    def val(self):
        return(round(self.x/self.y, 2))
        
    def inverse(self):
        r = Rationnel(self.x,self.y)
        r.x = self.x
        r.y = self.y
        return (round(1/(r.x/r.y), 2))
    
    