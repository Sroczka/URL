#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:04:11 2018

@author: janik
"""

x=1
y=1
z=1
def f():
  def g():
    z=3
    print(dir())
    print(x,y,z)

  y=2
  print(dir())
  print(x,y,z)

  g()

print(dir(),x,y,z)
f()
print(x,y,z)

#####################################################################

ma_tortue = { "x": 0, "y": 0 }

def avance(une_tortue,dx,dy):
  une_tortue["x"] += dx
  une_tortue["y"] += dy

def localise(une_tortue):
  print(une_tortue["x"],une_tortue["y"])

localise(ma_tortue)
avance(ma_tortue,10,10)
localise(ma_tortue)