#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:33:59 2018

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

# test
if __name__ == '__main__':
    mon_graphe = Graphe(False)
    mon_graphe.add_sommet("Paris","Capitale de la France")
    mon_graphe.add_sommet("Angers","la plus belle ville de France")
    mon_graphe.add_arete("A11","Paris","Angers","autoroute")
    print(mon_graphe)
    #mon_graphe.rm_arete("A11")
    mon_graphe.rm_sommet("Paris")
    print(mon_graphe)


#zadanie 3
    
if __name__ == '__main__':
    graf = Graphe(True)
    graf.add_sommet("7")
    graf.add_arete("a1","7","5")
    graf.add_arete("a2","7","8")
    graf.add_arete("a3","8","10")
    graf.add_arete("a4","8","9")
    graf.add_arete("a5","9","10")
    graf.add_arete("a6","9","6")
    graf.add_arete("a7","6","7")
    graf.add_arete("a8","6","5")
    graf.add_arete("a9","5","4")
    graf.add_arete("a10","4","2")
    graf.add_arete("a11","2","3")
    graf.add_arete("a12","2","1")
    graf.add_arete("a13","1","4")
    graf.add_arete("a14","3","2")
    graf.add_arete("a15","5","3")
    print(graf)