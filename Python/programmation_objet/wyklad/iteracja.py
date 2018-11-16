#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:00:33 2018

@author: janik
"""

class Sequentiel():
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i>1000:
            raise StopIteration("fin d'itération")
        return self.i*self.i

mon_seq = Sequentiel()
for i in mon_seq:
    print(i,end=" ")

mon_seq = Sequentiel()
it = mon_seq.__iter__(mon_seq)
try:
  i = it.__next__()
  while True:
    print(i,end=" ")
    i = it.__next__()
except StopIteration:
  pass

mon_seq = Sequentiel()
it = iter(mon_seq)
try:
  i = next(it)
  while True:
    print(i,end=" ")
    i = next(it)
except StopIteration:
  pass