#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:27:33 2019

@author: janik
"""

from asic import Asic


class Tcapteur:
    
    def __init__(self,id):
        self.id = id
        self.a = Asic(id)
        
    def getLabel(self):
        self.a.getLabel
    
    def getTemperature(self):
        return(self.a.getVal())
       
        
class Pcapteur:
    
    def __init__(self,id):
        self.id = id
        self.a = Asic(id)
        
    def getLabel(self):
        self.a.getLabel
    
    def getPression(self):
        return(self.a.getVal())
    

class Hcapteur:
    
    def __init__(self,id):
        self.id = id
        self.a = Asic(id)
        
    def getLabel(self):
        self.a.getLabel
    
    def getHygrometrie(self):
        return(self.a.getVal())
        
class Mcapteur:
        
    def __init__(self,id_1,id_2):
        self.id_1 = id_1
        self.id_2 = id_2
        self.a_1 = Asic(id_1)
        self.a_2 = Asic(id_2)
            
    def getTemperature(self):
        return(self.a_1.getVal())
        
    def getPression(self):
        return(self.a_2.getVal())

        
class MultiCapteur:
    
    def __init__(self,l):
        self.l = l
        
    #def getAsics(self):
     #   for i in self.l:
      #      if( i == Tcapteur(id))
                
            
        

if __name__ ==  "__main__":

    mon_capteur = Tcapteur(id=1)
    print(f"{mon_capteur.getLabel()}: {mon_capteur.getTemperature()}")
    mon_capteur = Pcapteur(id=2)
    print(f"{mon_capteur.getLabel()}: {mon_capteur.getPression()}")
    mon_capteur = Hcapteur(id=3)
    print(f"{mon_capteur.getLabel()}: {mon_capteur.getHygrometrie()}")
    mon_capteur = Mcapteur(1,2)
    print(mon_capteur.getTemperature(),mon_capteur.getPression ())
    
    mon_capteur = MultiCapteur([Tcapteur(1),Pcapteur(2),Hcapteur(3),Tcapteur(4)])
    #mon_capteur.getAsics()
    #for m in mon_capteur.getAsics():
     #   print(f"{m.getLabel()}: {m.getVal()}")  