#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:09:18 2019

@author: janik
"""

class IP:
    def __init__(self,x,y,z,t):
        if(x>255 or y>255 or z>255 or t>255): raise ValueError
        elif(x<0 or y<0 or z<0 or t<0): raise ValueError
        else:
            self.x = x
            self.y = y
            self.z = z
            self.t = t
        
    def tostr(self):
        print(f"{self.x}.{self.y}.{self.z}.{self.t}")