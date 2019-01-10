#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:24:42 2019

@author: janik
"""

class ObjetConnecte:
  """
    Modélise un objet connecté
  """
  def __init__(self,ip,box):
    """Connecte l'objet au réseau domestique

    Explication :
        Pour se connecter à un réseau domestique, un objet connecté a besoin
        de posséder une adresse IP propre (unique sur le réseau domestique) :
        c’est l’argument ip.
        Et pour communiquer avec d’autres équipements sur Internet, il a besoin
        de connaitre l’adresse IP de sa box (qui joue le rôle de passerelle
        entre le réseau domestique et Internet) : c’est l’argument box.
    """
    try:
        self.ip = ip.tostr()
        self.box = box.tostr()
    except AttributeError as e:
        print("l'objet n'a pas de méthode tostr !")
        raise

  def _send(self,message):
    """envoie la chaine de caractères 'message' aux objets distants"""
    print(f"{self.ip} envoie [{message}]")  # on simule l'envoi du message