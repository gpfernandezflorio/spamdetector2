import sys
import time, datetime
import json
import numpy as np
import pandas as pd
from collections import Counter
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import (cross_val_predict, train_test_split, KFold)
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
from cargarModelo import *

estoy_en_los_labos = True
prueba_full = True

if estoy_en_los_labos:
  path = "/media/libre/aa/"
else:
  path = ""
