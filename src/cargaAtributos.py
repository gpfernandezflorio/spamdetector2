#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def cargando_atributos(idf):
  print "Cargando atributos"
  df = pd.DataFrame([x[0] for x in idf], columns=['text'])
  df['class'] = [x[1] for x in idf]
  for i in range(len(dnames)):
    df[dnames[i]] = map(dfuncs[i], df.text)
  X = df[dnames].values
  y = df['class']
  return X, y

def leer_base():
  if estoy_en_los_labos:
    train = np.load('/media/libre/aa/train.npy')
    test = np.load('/media/libre/aa/test.npy')
  else
    train = np.load('train.npy')
    test = np.load('test.npy')
  trainX, trainy = cargando_atributos(train)
  testX, testy = cargando_atributos(test)
  if estoy_en_los_labos:
    np.save('/media/libre/aa/trainX', trainX)
    np.save('/media/libre/aa/trainy', trainy)
    np.save('/media/libre/aa/testX', testX)
    np.save('/media/libre/aa/testy', testy)
  else:
    np.save('trainX', trainX)
    np.save('trainy', trainy)
    np.save('testX', testX)
    np.save('testy', testy)
if __name__ == '__main__':
  leer_base()
