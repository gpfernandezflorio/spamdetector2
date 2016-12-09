#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

from variables import *

import os.path

def print_params(metodo,base):
  if base == None:
    f = 'gs/gs'+metodo+'.param'
  else:
    name = base.split('.')
    f = 'gs/gs'+metodo+'.'+name[0]+'.'+name[1]+'.param'
  if os.path.isfile(f):
    bp = np.load(f)
    print f,bp

for M in ["Dtree","Rforest","Knn","Svc"]:
  print_params(M, None)
  for B in ["PCA","ICA"]:
    for n in [1,2,3,4,5,10,20,40,60,80,100]:
      print_params(M, B + "." + str(n))


