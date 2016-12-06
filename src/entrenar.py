#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [6] Entrenar.

  Descripción: Entrena un modelo.

  Uso: python entrenar.py [Gsearch] METODO [BASE=trainX.npy] [MAXITER=100]
  * Siendo METODO alguno de los siguientes: Dtree, Rforest, Nbayes, Knn o Svc.
  * Siendo BASE la base con la que entrenar (debe ser un archivo .npy existente) (trainX.npy por defecto).
  * Siendo MAXITER la máxima cantidad de iteraciones (100 por defecto)

  Requiere el archivo trainX.npy (o el pasado por parámetro).
  * si estoy_en_los_labos lo va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: NAME.npy.pickle
  * Siendo NAME el nombre del archivo, compuesto por el nombre del método y el nombre de la base.
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

def guardar_modelo(metodo, base):
  str_file = path + metodo + "." + base + '.pickle'
  fout = open(str_file,'w')
  pickle.dump(clf,fout)
  fout.close()
  return

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    gs = False
    n = 2
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
  X = np.load(path + base)
  y = np.load(path + 'trainy.npy')

  clf = cargarModelo(gs, metodo, max_iter)
  start = time.time()
  clf.fit(X, y)
  end = time.time()

  #d = datetime.datetime.now()
  #f = open("data.txt",'a')
  #f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + " " + str(d.hour) + "hs>\n")
  #f.write(metodo + " NULL " + str(0) + " " + str(end - start))
  #f.write("\n")
  #f.close()
  guardar_modelo(metodo, base)
