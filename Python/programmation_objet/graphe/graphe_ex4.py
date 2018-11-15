#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:36:04 2018

@author: janik
"""

class Sommet:
    def __init__(self,info=None):
        self.info = info
        
    def set_into(self,info):
        self.info = info
        
class Arete:
    def __init__(self,source,but,info=None):
        self.s1 = source
        self.s2 = but
        self.info = info
        
    def set_info(self,info):
        self.info = info
    # Juste un test pour savoir si l'objet est détruit
    def __del__(self):
        print("une arete de moins")



class Graphe:
    def __init__(self,oriented):
        self.oriented = oriented #bool
        self.sommets = {} #na poczatku 0 wierzcholkow
        self.aretes = {} #i 0 polaczen
             
    def __str__(self):
        chaine = f"Graphe à {len(self.sommets)} sommets et {len(self.aretes)} arêtes "
        return chaine
        
    def add_sommet(self,nom,info=None): #dodawanie
        if nom not in self.sommets:
            new = Sommet(info)
            self.sommets[nom] = new
    
    def add_arete(self,nom,source,but,info=None):
        if nom not in self.aretes:
            if source not in self.sommets:
                self.add_sommet(source)
            if but not in self.sommets:
                self.add_sommet(but)
            new = Arete(source,but,info)
            self.aretes[nom] = new
    
    def rm_arete(self,nom):  #usuwanie
        if nom in self.aretes:
            del self.aretes[nom]
    
    def rm_sommet(self,nom):
        if nom in self.sommets:
            usun = [] 
            # lista do usuniecia, bo inaczej zmiana rozmiaru slownika w czasie iteracji
            for nom_arete in self.aretes:
                if nom in [self.aretes[nom_arete].s1, self.aretes[nom_arete].s2]: #zczytuje nazwe
                    usun.append(nom_arete)
            for nom_arete in usun:
                self.rm_arete(nom_arete)
            del self.sommets[nom]
            
            
if __name__ == '__main__':
    with open("/users/mmath/janik/Python/programmation_objet/graphe/citations-HepTh.txt","r") as f:
        graf = Graphe(True)
        i = 1
        for line in f:
            #print((line.split(" ")))
            #j += 1
            if(len(line.strip().split(" ")) == 2):  #co to strip???
                source, but = line.strip().split(" ")
                graf.add_arete(i, source, but)
                i += 1
        print(graf) #czyszczenie pamieci, jak sie pozbyc