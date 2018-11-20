#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:39:46 2018

@author: janik
"""

from math import sin,pi,exp,log
import numpy as np

def son(freq,t):
    son = round(sin(freq*2*pi*t))
    return (son.to_bytes(1,byteorder='big',signed = True))

interval = np.linspace(0,1,44000)

echantillon_la = []
for i in range (44000):
    echantillon_la.append(son(440,interval[i]))

fn = open('la.pcm','wb')   #w - write, b - binary mode
for i in range(44000):
    fn.write(echantillon_la[i])
fn.close()


def audition(a,b):
    
    x = log(b-a)/6
    
    f = lambda y : exp(y*x) + a
    
    fichier = open('a_b.pcm','wb')

    echantillon = []
    for j in range (44000):
        echantillon.append(son(f(interval[j]),interval[j]))
    for j in range (44000):
        fichier.write(echantillon[j])
        
    fichier.close()
            
    return fichier

audition(100,1000)
