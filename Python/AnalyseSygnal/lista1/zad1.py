#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:35:44 2018
@author: janik
"""

#a

(1000).to_bytes(2,byteorder='little',signed = False)

#b

f = open('data.pcm','wb')
f.write((1000).to_bytes(2,byteorder='big'))
f.write((2000).to_bytes(2,byteorder='big'))
f.close()

#c

#terminal

#d
from math import sin,pi

def s(t):
    s = sin(440*2*pi*t)
    return s

def u(t):
    u = round(s(t))
    return (u).to_bytes(1,byteorder='big',signed = True)
    
#e

import numpy as np

echantillon = []
interval = np.linspace(0,1,44000)
for i in range (44000):
    echantillon.append(s(interval[i]))

#f


echantillon_la = []
for i in range (44000):
    echantillon_la.append(u(interval[i]))
#g
fn = open('la.pcm','wb')   #w - write, b - binary mode
for i in range(44000):
    fn.write(echantillon_la[i])
fn.close()


#h 
#command
# cvlc --demux=rawaud --rawaud-channels=1 --rawaud-samplerate=44000
#--rawaud-fourcc "u8  " la.pcm

#i

def do(t):
    do = round(sin(220*2**(1/4)*2*pi*t))
    return (do).to_bytes(1,byteorder='big',signed = True)

def re(t):
    re = round(sin(220*2**(5/12)*2*pi*t))
    return (re).to_bytes(1,byteorder='big',signed = True)

def mi(t):
    mi = round(sin(220*2**(7/12)*2*pi*t))
    return (mi).to_bytes(1,byteorder='big',signed = True)

def fa(t):
    fa = round(sin(220*2**(2/3)*2*pi*t))
    return (fa).to_bytes(1,byteorder='big',signed = True)

def sol(t):
    sol = round(sin(220*2**(5/6)*2*pi*t))
    return (sol).to_bytes(1,byteorder='big',signed = True)

def si(t):
    si = round(sin(440*2**(1/6)*2*pi*t))
    return (si).to_bytes(1,byteorder='big',signed = True)

def do2(t):
    do = round(sin(440*2**(1/4)*2*pi*t))
    return (do).to_bytes(1,byteorder='big',signed = True)

echantillon_do = []
for i in range (44000):
    echantillon_do.append(do(interval[i]))
    
echantillon_re = []
for i in range (44000):
    echantillon_re.append(re(interval[i]))
    
echantillon_mi = []
for i in range (44000):
    echantillon_mi.append(mi(interval[i]))
    
echantillon_fa = []
for i in range (44000):
    echantillon_fa.append(fa(interval[i]))
    
echantillon_sol = []
for i in range (44000):
    echantillon_sol.append(sol(interval[i]))

echantillon_si = []
for i in range (44000):
    echantillon_si.append(si(interval[i]))

echantillon_do2 = []
for i in range (44000):
    echantillon_do2.append(do2(interval[i]))

fdo = open('do.pcm','wb')
for i in range(44000):
    fdo.write(echantillon_do[i])
fdo.close()

fre = open('re.pcm','wb')
for i in range(44000):
    fre.write(echantillon_re[i])
fre.close()

fmi = open('mi.pcm','wb')
for i in range(44000):
    fmi.write(echantillon_mi[i])
fmi.close()

ffa = open('fa.pcm','wb')
for i in range(44000):
    ffa.write(echantillon_fa[i])
ffa.close()

fsol = open('sol.pcm','wb')
for i in range(44000):
    fsol.write(echantillon_sol[i])
fsol.close()

fsi = open('si.pcm','wb')
for i in range(44000):
    fsi.write(echantillon_si[i])
fsi.close()

fdo2 = open('do2.pcm','wb')
for i in range(44000):
    fdo2.write(echantillon_do2[i])
fdo2.close()

fgama = open('gama.pcm','wb')
for i in range(44000):
    fgama.write(echantillon_do[i])
for i in range(44000):
    fgama.write(echantillon_re[i])
for i in range(44000):
    fgama.write(echantillon_mi[i])
for i in range(44000):
    fgama.write(echantillon_fa[i])
for i in range(44000):
    fgama.write(echantillon_sol[i])
for i in range(44000):
    fgama.write(echantillon_la[i])
for i in range(44000):
    fgama.write(echantillon_si[i])
for i in range(44000):
    fgama.write(echantillon_do2[i])
fgama.close()
