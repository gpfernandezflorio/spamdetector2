#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [4] ReducirDimensiones.

  Descripción: Utiliza los métodos de reducción de dimensionalidad para disminuír la cantidad de atributos.

  Uso: python reducirDimensiones.py METODO [DIMENSIONES=10]
  * Siendo METODO alguno de los siguientes: PCA o ICA.
  * Siendo DIMENSIONES la cantidad de componenetes deseada (10 por defecto).

  Requiere los archivos trainX.npy y testX.npy.
  * si estoy_en_los_labos los va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: NAME.npy NAME-test.npy
  * Siendo NAME el nombre del archivo, compuesto por el nombre del método y la cantidad de componentes.
  * si estoy_en_los_labos los guarda en /media/libre/aa/.
  * si no, en el mismo directorio.
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
  np.save(path + metodo + "." + str(n) , trainX)
  np.save(path + metodo + "." + str(n) + '-test', testX)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    if metodo != "PCA" and metodo != "ICA":
      print u'Dimensión inválida'
      exit()
    n = 2
    dims = 10
    if len(sys.argv) > n:
      dims = int(sys.argv[n])
    red_dim(metodo, dims)
    exit()
  else:
    print u'¿Qué dimension querés?'
    exit()
