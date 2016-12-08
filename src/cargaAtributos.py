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

  Output: trainX.npy | testX.npy | trainy.npy | testy.npy
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
  if estoy_en_los_labos:
    train = np.load('/media/libre/aa/train.npy')
    test = np.load('/media/libre/aa/test.npy')
  else:
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
