#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector.

*Reducir Dimensiones:
  python tp.py Red dimension [n=10]
  Ej:
  python tp.py Red PCA 5

*Entrenar un modelo:
  python tp.py [Gsearch] metodo [base=full]
  Ej:
  python tp.py Dtree
  python tp.py Gsearch Dtree trainX_PCA5.npy

*Cross Validation:
  python tp.py CV metodo base [cv=10]
  Ej:
  python tp.py CV Dtree trainX_PCA5.npy 20

*Predecir:
  python tp.py Test metodo base
  Ej:
  python tp.py Test Dtree testX_PCA5.npy

  metodos = Dtree, Rforest, Etree, Knn, Nbayes, Svc
  dimensiones = PCA, ICA
"""

import sys
import time, datetime
import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import (cross_val_score, train_test_split)
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import (RFE,RFECV)
from sklearn.ensemble import ( RandomForestClassifier , ExtraTreesClassifier )
from sklearn.metrics import ( accuracy_score, precision_score, recall_score, f1_score,roc_auc_score )
from sklearn.decomposition import PCA, IncrementalPCA, FastICA
import pickle

reload(sys)
sys.setdefaultencoding('utf-8')
from attributes import dnames
from attributes import *

estoy_en_los_labos = True

if estoy_en_los_labos:
  path = "/media/libre/aa/"
else:
  path = ""

def guardar_modelo(metodo, base):
  str_file = path + metodo + base + '.pickle'
  fout = open(str_file,'w')
  pickle.dump(clf,fout)
  fout.close()
  return

def red_dim(metodo, n):
  trainX = np.load(path + 'trainX.npy')
  testX = np.load(path + 'testX.npy')
  if metodo == "PCA":
    pca = IncrementalPCA(n_components=n)
    pca.fit(trainX)
    trainX = pca.transform(trainX)
    testX = pca.transform(testX)
  elif metodo == "ICA":
    ica = FastICA(n_components=n)
    ica.fit(trainX)
    trainX = ica.transform(trainX)
    testX = ica.transform(testX)
  else:
    print u'Dimensión inválida'
    exit()
  np.save(path + 'trainX_' + metodo + str(n) , trainX)
  np.save(path + 'testX_' + metodo + str(n), testX)

def predecir(metodo, base):
  # TODO: Esto no va acá! debería estar al final, con la parte de cross validation
  testX = np.load(path + base)
  clf = pickle.load(open(path + metodo + base.replace("test","train") + '.pickle'))
  start = time.time()
  predy = list(clf.predict(testX))
  end = time.time()
  testy = np.load(path + 'testy.npy')
  testn = map(lambda x : ( 1 if x == 'ham' else 0 ), testy)
  predn = map(lambda x : ( 1 if x == 'ham' else 0 ), predy)
  d = datetime.datetime.now()
  f = open("data.txt",'a')
  #f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + " " + str(d.hour) + "hs>\n")
  #f.write(metodo + " " + base + "\n")
  #TODO: obtener RedDim y cant_comp a partir del nombre de la base
  f.write(metodo + " " + redDim + " " + cant_comp + " ")
  f.write(str(end - start) + " ")
  #TODO: calcular prec, acc, roc, f1, recall... promedio y varianza con CV
  f.write(str(precision_score(testn, predn)) + " ")
  f.write(str(recall_score(testn, predn)) + " ")
  f.write(str(f1_score(testn, predn)) + " ")
  f.write(str(accuracy_score(testn, predn)) + " ")
  f.write(str(roc_auc_score(testn, predn)) + "\n")
  f.close()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    n = 2
    # RED
    if metodo == 'Red':
      metodo = "none"
      dims = 10
      if len(sys.argv) > n:
        metodo = sys.argv[n]
        if metodo != "PCA" and metodo != "ICA" and metodo != "RFE" and metodo != "iPCA":
          print u'Dimensión inválida'
          exit()
        n = n + 1
        if len(sys.argv) > n:
          dims = int(sys.argv[n])
          n = n + 1
      else:
        print u'¿Qué dimension querés?'
        exit()
      red_dim(metodo, dims)
      exit()
    # CV
    if metodo == 'CV':
      cv = 10
      base = "testX.npy"
      if len(sys.argv) > n:
        metodo = sys.argv[n]
        n = n + 1
      else:
        print u'¿Qué método querés?'
        exit()
      if len(sys.argv) > n:
        base = sys.argv[n]
        n = n + 1
      else:
        print u'¿Qué base querés?'
        exit()
      if len(sys.argv) > n:
        cv = int(sys.argv[n])
        n = n + 1
      clf = pickle.load(open(path + metodo + base + '.pickle'))
      X = np.load(path + base)
      y = np.load(path + 'trainy.npy')
      res = cross_val_score(clf, X, y, cv=cv)
      d = datetime.datetime.now()
      f = open("data.txt",'a')
      f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + " " + str(d.hour) + "hs>\n")
      f.write(metodo + " - " + base + "\n")
      f.write("M:" + str(np.mean(res))+"\n")
      f.write("S:" + str(np.std(res))+"\n")
      f.close()
      exit()
    # TEST
    if metodo == 'Test':
      base = "testX.npy"
      if len(sys.argv) > n:
        metodo = sys.argv[n]
        n = n + 1
      else:
        print u'¿Qué método querés?'
        exit()
      if len(sys.argv) > n:
        base = sys.argv[n]
        n = n + 1
      else:
        print u'¿Qué base querés?'
        exit()
      predecir(metodo, base)
      exit()
    # TRAIN
    gs = False
    if metodo == 'Gsearch':
      if len(sys.argv) > n:
        metodo = sys.argv[n]
      else:
        print u'¿Qué método querés?'
        exit()
      gs = True
      n = n + 1
  else:
    print u'¿Qué método querés?'
    exit()
  if metodo != 'Dtree' and metodo != 'Rforest' and metodo != 'Knn' and metodo != 'Nbayes' and metodo != 'Svc':
    print u'Método inválido'
    exit()
  base = "trainX.npy"
  if len(sys.argv) > n:
    base = sys.argv[n]
    n = n + 1
  if len(sys.argv) > n:
    maxiter = int(sys.argv[n])
    n = n + 1
  else:
    maxiter = 100

  print "maxiter es " + str(maxiter)
  X = np.load(path + base)
  y = np.load(path + 'trainy.npy')

  start = 0
  end = 0
  if metodo == 'Dtree':
    clf = DecisionTreeClassifier()
    start = time.time()
    clf.fit(X, y)
    end = time.time()
  elif metodo == 'Rforest':
    clf = RandomForestClassifier()
    start = time.time()
    clf.fit(X, y)
    end = time.time()
  elif metodo == 'Knn':
    clf = KNeighborsClassifier()
    start = time.time()
    clf.fit(X, y)
    end = time.time()
  elif metodo == 'Nbayes':
    start = time.time()
    clf = GaussianNB()
    clf.fit(X, y)
    end = time.time()
  elif metodo == 'Svc':
    start = time.time()
    clf = SVC(max_iter=maxiter)
    clf.fit(X, y)
    end = time.time()

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
    start = time.time()
    clf.fit(X, y)
    end = time.time()
    print clf.best_params_

    metodo = "GS_" + metodo

  d = datetime.datetime.now()
  f = open("data.txt",'a')
  #f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + " " + str(d.hour) + "hs>\n")
  f.write(metodo + " NULL " + str(0) + " " + str(end - start))
  #TODO: calcular prec, acc, roc, f1, recall... promedio y varianza
  f.write("\n")
  f.close()
  guardar_modelo(metodo, base)
