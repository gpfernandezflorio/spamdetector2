#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector.
  Uso: python cortaBase.py
"""

import sys
import time, datetime
import json
import numpy as np
import pandas as pd
from collections import Counter
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

estoy_en_los_labos = True
prueba_full = True

if __name__ == '__main__':
    print 'Cargando ham'
    if not prueba_full:
        ham_txt = json.load(open('../ham_dev_mini.json'))
    elif estoy_en_los_labos:
        ham_txt = json.load(open('/media/libre/dataset_dev/ham_dev.json'))
    else:
        ham_txt = json.load(open('../ham_dev.json'))
    print 'Cargando spam'
    if not prueba_full:
        spam_txt = json.load(open('../spam_dev_mini.json'))
    elif estoy_en_los_labos:
        spam_txt = json.load(open('/media/libre/dataset_dev/spam_dev.json'))
    else:
        spam_txt = json.load(open('../spam_dev.json'))

    df = pd.DataFrame(ham_txt+spam_txt, columns=['text'])
    df['class'] = ['ham' for _ in range(len(ham_txt))]+['spam' for _ in range(len(spam_txt))]
    train, test = train_test_split(df, test_size = 0.2)
    if estoy_en_los_labos:
        np.save('/media/libra/aa/train', train)
        np.save('/media/libra/aa/test', test)
    else:
        np.save('train', train)
        np.save('test', test)
