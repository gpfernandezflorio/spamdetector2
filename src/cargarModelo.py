#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

from variables import *

import os.path

def cargarModelo(metodo, base=None):
  bp = {}
  if base == None:
    f = 'gs'+metodo+'.param'
  else:
    name = base.split('.')
    f = 'gs'+metodo+'.'+name[0]+'.'+name[1]+'.param'
  if os.path.isfile(f):
    bp = np.load(f)
  if metodo == 'Dtree':
    clf = DecisionTreeClassifier()
  elif metodo == 'Rforest':
    clf = RandomForestClassifier()
  elif metodo == 'Knn':
    clf = KNeighborsClassifier()
  elif metodo == 'Nbayes':
    clf = GaussianNB()
  elif metodo == 'Svc':
    clf = SVC(max_iter=100)
  for k in bp:
    clf.set_params(**{k:bp[k]})
  return clf
