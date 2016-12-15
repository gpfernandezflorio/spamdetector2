#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

from variables import *

def cargarModelo(metodo, base=None):
  bp = {}
  if base == None:
    f = 'gs/gs'+metodo+'.param'
  else:
    name = base.split('.')
    f = 'gs/gs'+metodo+'.'+name[0]+'.'+name[1]+'.param'
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
    clf = SVC()
  for k in bp:
    if not (metodo == 'Dtree' and k == 'max_features'):
      clf.set_params(**{k:bp[k]})
  return clf
