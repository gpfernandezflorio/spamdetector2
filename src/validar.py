#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [6] Validar.

  Descripción: Utiliza K-fold Cross Validation para evaluar un modelo.

  Uso: python validar.py METODO [BASE=trainX.npy] [K=10]
  * Siendo METODO alguno de los siguientes: Dtree, Rforest, Nbayes, Knn o Svc.
  * Siendo BASE la base contra la que validar (debe ser un archivo .npy existente) (trainX.npy por defecto).
  * Siendo K la cantidad de folds (10 por defecto)

  Requiere el archivo trainy.npy y trainX.npy (o el pasado por parámetro como base).
  * si estoy_en_los_labos los va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: cv.txt (append).
"""

from variables import *

if __name__ == '__main__':
  max_iter=100
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    cv = 10
    base = "trainX.npy"
    n = 2
    if len(sys.argv) > n:
      base = sys.argv[n]
      n = n + 1
    if len(sys.argv) > n:
      cv = int(sys.argv[n])
      n = n + 1

    X = np.load(path + base)
    y = np.load(path + 'trainy.npy')

    cv_arg = KFold(y.size, cv)
    ys = []
    times = []
    for train_idx, valid_idx in cv_arg:
      clf = cargarModelo(False, metodo, max_iter)
      start = time.time()
      clf.fit(X[train_idx], y[train_idx])
      end = time.time()
      times.append(end-start)
      cur_pred = clf.predict(X[valid_idx])
      pred = map(lambda x : ( 0 if x == 'ham' else 1 ), cur_pred)
      real = map(lambda x : ( 0 if x == 'ham' else 1 ), y[valid_idx])
      ys.append((tuple(real), tuple(pred)))

    cv_accuracy = map(lambda x: accuracy_score(x[0], x[1]), ys)
    cv_recall = map(lambda x: recall_score(x[0], x[1]), ys)
    cv_f1 = map(lambda x: f1_score(x[0], x[1]), ys)
    cv_precision = map(lambda x: precision_score(x[0], x[1]), ys)
    cv_roc_auc = map(lambda x: roc_auc_score(x[0], x[1]), ys)

    f = open("cv.txt",'a')
    if (base == "trainX.npy"):
      f.write(metodo + " NULL 0 " + str(cv) + " ")
    else:
      name = base.split(".")
      f.write(metodo + " " + name[0] + " " + name[1] + " " + str(cv) + " ")
    f.write(str(np.mean(times)) + " ")
    f.write(str(np.mean(cv_precision)) + " ")
    f.write(str(np.mean(cv_recall)) + " ")
    f.write(str(np.mean(cv_f1)) + " ")
    f.write(str(np.mean(cv_accuracy)) + " ")
    f.write(str(np.mean(cv_roc_auc)) + " ")
    f.write(str(np.std(times)) + " ")
    f.write(str(np.std(cv_precision)) + " ")
    f.write(str(np.std(cv_recall)) + " ")
    f.write(str(np.std(cv_f1)) + " ")
    f.write(str(np.std(cv_accuracy)) + " ")
    f.write(str(np.std(cv_roc_auc)))
    f.write("\n")
    exit()
  else:
    print u'¿Qué método querés?'
    exit()
