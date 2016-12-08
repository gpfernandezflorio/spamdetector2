#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

from variables import *

def cargarModelo(gs, metodo, max_iter):
  if metodo == 'Dtree':
    clf = DecisionTreeClassifier()
  elif metodo == 'Rforest':
    clf = RandomForestClassifier()
  elif metodo == 'Knn':
    clf = KNeighborsClassifier()
  elif metodo == 'Nbayes':
    clf = GaussianNB()
  elif metodo == 'Svc':
    clf = SVC(max_iter=maxiter)

  if (gs):
    # print clf.get_params().keys()
    # exit()
    param_grid = {}
    if metodo == 'Dtree':
      # max_depth: 14 16 o None, min_samples_split: 3, criterion: entropy
      param_grid = {"max_depth": [14,15,16,None],
        "max_features": [164,166,168,170,None],
        "min_samples_split": [3],
        "criterion": ["gini", "entropy"]}
    elif metodo == 'Rforest':
      # max_depth: None, min_smaples_split: 4,5, criterion: entropy, max_features: 95
      # , n_estimators: 80 (y si le sigo aumentado sigue agarrando el maximo)
      param_grid = {"max_depth": [14,16,None],
        "max_features": [90,95,100,105,None],
        "min_samples_split": [3,4,5],
        "criterion": ["gini","entropy"],
        "n_estimators": [20,30,40,80]}
    elif metodo == 'Knn':
      # n_neighbors: 4, weights: distance
      param_grid = {"n_neighbors": [3,4,5],
        "weights": ["uniform", "distance"]}
    elif metodo == 'Nbayes':
      param_grid = {"max_depth": [1,2],
        "max_features": [10,15],
        "min_samples_split": [1,3],
        "criterion": ["gini", "entropy"]}
    clf = GridSearchCV(clf, param_grid=param_grid,n_jobs=-1,verbose=2)
  return clf
