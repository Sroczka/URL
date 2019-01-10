#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:28:29 2019

@author: janik
"""

import random

class Asic :
  def __init__(self, id, min=0, max=100):
    self.id = id
    self.min = min
    self.max = max

  def getVal(self):
    """
    retourne la mesure sous forme d'un entier
    on simule ici la mesure en renvoyant une valeur aléatoire
    """
    return random.randint(self.min, self.max)

  def getLabel(self):
    """
    retourne la signification de la mesure sous forme d'une string
    """
    raise NotImplementedError("cette méthode doit être définie au niveau des sous-classes")
    
    
if __name__ ==  "__main__":
    a = Asic(id=5)
    a.getVal()