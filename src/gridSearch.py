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

  Requiere el archivo trainX.npy (o el pasado por parámetro).
  * si estoy_en_los_labos lo va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: gs/NAME.param
  * Siendo NAME el nombre del archivo, compuesto por el nombre del método y la base.
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
    f = 'gs/gs'+metodo+'.param'
  else:
    name = base.split('.')
    N = int(name[1])
    f = 'gs/gs'+metodo+'.'+name[0]+'.'+name[1]+'.param'

  param_grid = {}
  if metodo == 'Dtree':
    param_grid = {"max_depth": [1,5,10,15,20,None],
      "max_features": filter (lambda x: x < N, [1,50,100,150,None]),
      "min_samples_split": [1,2,3,4,5],
      "criterion": ["gini", "entropy"]}
  elif metodo == 'Rforest':
    param_grid = {"max_depth": [1,5,10,15,20,None],
      "max_features": filter (lambda x: x < N, [1,50,100,150,None]),
      "min_samples_split": [1,2,3,4,5],
      "criterion": ["gini","entropy"],
      "n_estimators": [10,50,100,150]}
  elif metodo == 'Knn':
    param_grid = {"n_neighbors": [1,2,3,4,5],
      "weights": ["uniform", "distance"]}
  elif metodo == 'Nbayes':
    print "Sorry, no puedo hacer grid search con Naive Bayes."
  elif metodo == 'Svc':
    param_grid = {"kernel": ["linear","poly","rbf","sigmoid"],
      "max_iter": [10,50,100,500,1000]}
  clf = cargarModelo(metodo)
  clf = GridSearchCV(clf, param_grid=param_grid,n_jobs=-1,verbose=0)
  clf.fit(X, y)
  bp = clf.best_params_
  fout = open(f,'w')
  pickle.dump(bp,fout)
  print metodo, base, bp
