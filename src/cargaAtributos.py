#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [3] CargaAtributos.

  Descripción: Almacena sólo la información relevante (los atributos) de las bases de train y test.

  Uso: python cargaAtributos.py

  Requiere los archivos train.npy y test.npy
  * si estoy_en_los_labos los va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: trainX.npy, testX.npy, trainy.npy y testy.npy
  * si estoy_en_los_labos los guarda en /media/libre/aa/.
  * si no, en el mismo directorio.
"""

from variables import *

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
  train = np.load(path + 'train.npy')
  test = np.load(path + 'test.npy')
  trainX, trainy = cargando_atributos(train)
  testX, testy = cargando_atributos(test)
  np.save(path + 'trainX', trainX)
  np.save(path + 'trainy', trainy)
  np.save(path + 'testX', testX)
  np.save(path + 'testy', testy)
if __name__ == '__main__':
  leer_base()
