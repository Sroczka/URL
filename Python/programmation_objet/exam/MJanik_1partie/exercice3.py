#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:20:33 2019

@author: janik
"""

import pandas as pd

def solde(idcompte):
    df = pd.read_csv("operations.csv")
    df.set_index("idop", inplace = True)
    compte = df[df["idcompte"] == idcompte]
    s = 0
    a,b = compte.shape
    for i in range(a):
        s += compte.iloc[i][1]
    return(s)
        