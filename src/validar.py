#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [6] Validar.

  Descripción: Utiliza K-fold Cross Validation para evaluar un modelo entrenado.

  Uso: python validar.py MODELO [BASE=trainX.npy] [K=10]
  * Siendo MODELO el modelo a entrenar (debe ser un archivo .pickle existente)
  * Siendo BASE la base contra la que validar (debe ser un archivo .npy existente) (trainX.npy por defecto).
  * Siendo K la cantidad de folds (10 por defecto)

  Requiere el archivo trainX.npy (o el pasado por parámetro como base) y el archivo pasado por parámetro como modelo.
  * si estoy_en_los_labos los va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: data.txt (append).
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

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    cv = 10
    base = "testX.npy"
    n = 2
    if len(sys.argv) > n:
      base = sys.argv[n]
      n = n + 1
    if len(sys.argv) > n:
      cv = int(sys.argv[n])
      n = n + 1
    clf = pickle.load(open(path + metodo))
    X = np.load(path + base)
    y = np.load(path + 'trainy.npy')
    res = cross_val_score(clf, X, y, cv=cv)
    d = datetime.datetime.now()
    #TODO: calcular prec, acc, roc, f1, recall... promedio y varianza
    f = open("data.txt",'a')
    f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + " " + str(d.hour) + "hs>\n")
    f.write(metodo + " - " + base + "\n")
    f.write("M:" + str(np.mean(res))+"\n")
    f.write("S:" + str(np.std(res))+"\n")
    f.close()
    exit()
  else:
    print u'¿Qué método querés?'
    exit()
