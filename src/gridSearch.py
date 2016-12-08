#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [5] Grid Search.

  Descripción: Ejecuta Grid Search para determinar los mejores parámetros para un modelo.

  Uso: python predecir.py METODO [BASE=trainX.npy]
  * Siendo METODO alguno de los siguientes: Dtree, Rforest, Nbayes, Knn o Svc.
  * Siendo BASE la base contra la que validar (debe ser un archivo .npy existente) (trainX.npy por defecto).

  Output: Imprime por pantalla los mejores parámetros
"""

from variables import *

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    if metodo != 'Dtree' and metodo != 'Rforest' and metodo != 'Knn' and metodo != 'Nbayes' and metodo != 'Svc':
      print u'Método inválido'
      exit()
    base = "trainX.npy"
    n = 2
    if len(sys.argv) > n:
      base = sys.argv[n]
      n = n + 1
  else:
    print u'¿Qué método querés?'
    exit()

  X = np.load(path + base)
  y = np.load(path + 'trainy.npy')

  N = 201
  if base == "trainX.npy":
    f = 'gs'+metodo+'.param'
  else:
    name = base.split('.')
    N = int(name[1])
    f = 'gs'+metodo+'.'+name[0]+'.'+name[1]+'.param'

  # print clf.get_params().keys()
  # exit()
  param_grid = {}
  if metodo == 'Dtree':
    # max_depth: 14 16 o None, min_samples_split: 3, criterion: entropy
    param_grid = {"max_depth": [14,15,16,None],
      "max_features": filter (lambda x: x < N, [164,166,168,170,None]),
      "min_samples_split": [3],
      "criterion": ["gini", "entropy"]}
  elif metodo == 'Rforest':
    # max_depth: None, min_smaples_split: 4,5, criterion: entropy, max_features: 95
    # , n_estimators: 80 (y si le sigo aumentado sigue agarrando el maximo)
    param_grid = {"max_depth": [14,16,None],
      "max_features": filter (lambda x: x < N, [90,95,100,105,None]),
      "min_samples_split": [3,4,5],
      "criterion": ["gini","entropy"],
      "n_estimators": [20,30,40,80]}
  elif metodo == 'Knn':
    # n_neighbors: 4, weights: distance
    param_grid = {"n_neighbors": [3,4,5],
      "weights": ["uniform", "distance"]}
  elif metodo == 'Nbayes':
    param_grid = {"max_depth": [1,2],
      "max_features": filter (lambda x: x < N, [10,15]),
      "min_samples_split": [1,3],
      "criterion": ["gini", "entropy"]}
  clf = cargarModelo(metodo)
  clf = GridSearchCV(clf, param_grid=param_grid,n_jobs=-1,verbose=0)
  clf.fit(X, y)
  bp = clf.best_params_
  fout = open(f,'w')
  pickle.dump(bp,fout)
  print metodo, base, bp
