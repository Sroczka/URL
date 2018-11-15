#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:36:04 2018

@author: janik
"""

from graphe1 import *
            
graf = Graphe(True)

with open("/users/mmath/janik/Python/programmation_objet/graphe/citations-HepTh.txt","r") as fichier:
    i = 1
    for line in f:
        #print((line.split(" ")))
        #j += 1
        if(len(line.strip().split(" ")) == 2):  #co to strip???
            source, but = line.strip().split(" ")
            graf.add_arete(i, source, but)
            i += 1
    print(graf) #czyszczenie pamieci, jak sie pozbyc
    #inaczej
    
    #for i,ligne in enumerate(fichier):
        #if i>1:
             #article,citations = ligne.strip().split("")
             #graf.add_arete(i, article, citation)