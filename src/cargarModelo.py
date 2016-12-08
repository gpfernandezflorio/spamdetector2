#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

from variables import *

def cargarModelo(metodo):
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
  return clf
