#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [7] Entrenar.

  Descripción: Entrena un modelo.

  Uso: python entrenar.py METODO [BASE=trainX.npy]
  * Siendo METODO alguno de los siguientes: Dtree, Rforest, Nbayes, Knn o Svc.
  * Siendo BASE la base con la que entrenar (debe ser un archivo .npy existente) (trainX.npy por defecto).

  Requiere el archivo trainX.npy (o el pasado por parámetro).
  * si estoy_en_los_labos lo va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: NAME.npy.pickle
  * Siendo NAME el nombre del archivo, compuesto por el nombre del método y el nombre de la base.
  * si estoy_en_los_labos los guarda en /media/libre/aa/.
  * si no, en el mismo directorio.
"""

from variables import *

def guardar_modelo(metodo, base):
  str_file = path + metodo + "." + base + '.pickle'
  fout = open(str_file,'w')
  pickle.dump(clf,fout)
  fout.close()
  return

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    n = 2
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
  X = np.load(path + base)
  y = np.load(path + 'trainy.npy')

  clf = cargarModelo(metodo)
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
