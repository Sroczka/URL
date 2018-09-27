#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:30:41 2018

@author: janik
"""

#ex 1

def sum_div(n):
    dzielniki=[]
    for i in range(1,n//2 + 1):
        if(n%i == 0):
            dzielniki.append(i)
    s = sum(dzielniki)
    return s

def parfait(n):
#    if(sum_div(n) == n):
#        return True
#    else:
#        return False
    return sum_div(n) == n
    
def list_parfait(n):
    lista = []
    for i in range(n):
        if(parfait(i)):
            lista.append(i)
    return lista

def amicaux(n,m):
#    if (sum_div(n) == m and sum_div(m) == n):
#        return True
#    else:
#        return False
    return (sum_div(n) == m and sum_div(m) == n)
    

def list_amicaux(n):
    lista = []
    for i in range(1,n):
        for j in range(i+1,n):
            if (amicaux(i,j)):
                lista.append((i,j))
    return lista

def amicaux2(n):
    lista = []
    for i in range(1,n):
        s = sum_div(i)
        if (sum_div(s) == i and i<s<n):
            lista.append([i,s])
    return lista

############################################################################
#ex 2
    
import math

#from zajecia2 import est_premier 
#zamiast drugi raz pisac funkcje, mozna wykorzystac poprzednio napisane programy

def est_premier(n):
    if(n>1):
        for i in range(2,math.floor(math.sqrt(n)+1)):
            if(n%i==0):
                return False
        return True
    else:
        return False
    
def chanceux(n):
    for k in range(n-1):
        if not (est_premier(n+k+k**2)):
            return False
    return True

def liste_chanceux(n):
    lista=[]
    for i in range(1,n):
        if(chanceux(i)):
            lista.append(i)
    return lista

################################################################################
#ex 3

def sum_cubes(n):
    lista=[]
    for i in range(1,math.ceil(n**1/3)):
        a = i**3
        for j in range(i,math.ceil(n**1/3)):
            if(a + j**3 == n):
                lista.append([i,j])
    if (len(lista)>1):
        print(lista)
        return True
                           
def taxicub(n):
    lista = []
    for i in range(1,n):
        if(sum_cubes(i)):
            lista.append(i)
    return lista

#moj program działa bardzo dlugo, lepiej jedna funckja
    
def taxicub2(N):
    n = int(N**1/3 + 0.1) #bo blad obliczeniowy, bo int to czesc calkowita
    lista=[]
    for i in range(1,n+1):
        icube = i**3
        for j in range(i,n+1):
            s = j**3 + icube
            if s<=N:
                for k in range(i+1,n+1):
                    kcube = k**3
                    for l in range(k+1,n+1):
                        if s == kcube + l**3:
                            print(f"le nombre {s} s'écrit {i}**3+{j}**3 et aussi s'écrit {k}**3+{l}**3")
                            lista.append(s)
    return lista

##############################################################################
#ex 4
def suivant_conoway(x):
    mot = str(x)
    mot_suivant = ""
    i = 0
    while i < len(mot):
        j = 1
        compte = 1
        while i+j < len(mot) and mot[i+j] == mot[i]:
            compte +=1
            j += 1
        mot_suivant = mot_suivant +str(compte) + mot[i]
        i = i+j
    return int(mot_suivant)
    

##############################################################
#ex 5
    
def fib(n):
    l=[1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l[n-1]
    
def fib_list(n):
    l=[1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l

#rekurencyjnie

def fib2(n):
    if n == 0 or n == 1: #f n in [0,1]
        result = 1
    else:
        result = fib2(n-1)+fib2(n-2)
    return result

def fib2_list(n):
    l=[]
    for i in range(0,n+1):
        l.append(fib2(i))
    return l

#rekurencyjnie 2, bardziej wydajny
    
def fib3(n): #zwraca dwie zmienne
    if n == 0:
        return [1,1]
    x = fib3(n-1)
    return [x[1], x[0]+x[1]]

def fib3_1(n): #zwraca tylko jedna potrzebna liczbe
    return fib3(n)[0]

def list_fib(n):
    l=[]
    for i in range(n+1):
        l.append(fib3_1(i))
    return l

def list_fib2(n):
    return [fib3_1(i) for i in range(n+1)]
#######################################################################
# rekurencja
    
def fact(n):  #silnia
    print(f"appel de fact({n})") #f podmienia wartosc n 
    if n == 0:
        print(f"fin de l'appel de fact({n})")
        return 1
    else:
        resultat = n * fact(n-1)
    print(f"fin de l'appel de fact({n})")
    return resultat


########################################################################
# ex6 --- skoncz sama
    
def suivants(n):
    l=[]
    if n == 1:
        l.append(0)
    elif n == 2:
        l.append(0)
        l.append(1)
    elif n>2:
        l.append(n-3)
        l.append(n-2)
        l.append(n-1)
    return l

