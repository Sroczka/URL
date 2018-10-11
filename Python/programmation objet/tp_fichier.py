#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:55:33 2018

@author: janik
"""

f = open("ulysses.txt","r")
a = f.readline()
f.close()

import re

motif = re.compile("\w+")

#######################
dico = {}

motif = re.compile("\w{5,}") #slowo powyzej 5 liter

with open("/users/mmath/echange/ulysses.txt","r") as f:
    for line in f:
        lista = motif.findall(line)
        for mot in lista:
            if mot in dico:
                dico[mot] += 1
            else:
                dico[mot] = 1
l = [[x,y] for x,y in dico.items()]
l.sort(key = lambda x: x[1], reverse = True)
print(l[:10])