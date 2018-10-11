#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:55:33 2018

@author: janik
"""

import re

#######################
#ex 1

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

###################
#ex 2
slownik = {}

with open("/users/mmath/echange/liste","r") as f:
    for i in range(1,10):
        suma = 0
        for line in f:
            if( int(line.split(" ")[4][0]) == i):
                suma += 1
            slownik[i] = suma
print(slownik)

#1 zlicza dobrze, osobno dla kazdej liczby dziala ale po kolei nie, cos nie tak z for

############################
#ex 3

#with open("/users/mmath/echange/logMail","r") as f:
    