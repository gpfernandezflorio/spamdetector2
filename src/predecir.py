#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [8] Predecir.

  Descripción: Clasifica una base a partir de un modelo entrenado.

  Uso: python predecir.py MODELO [BASE=testX.npy] [LABEl]
  * Siendo MODELO el modelo a utilizar (debe ser un archivo .pickle existente)
  * Siendo BASE la base a clasificar (debe ser un archivo .npy existente) (testX.npy por defecto).
  * Siendo LABEL el vector de etiquetas de la base (debe ser un archivo .npy existente) (puede ignorarse).

  Requiere el archivo testX.npy (o el pasado por parámetro como base), el archivo pasado por parámetro como modelo y el archivo pasado por parámetro como LABEL, de haber alguno.
  * si estoy_en_los_labos los va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: data.txt (append) | predict.txt.
  * Si se pasa un vector de etiquetas por parámetro, se modifica el achivo data.txt
  * En caso contrario, se genera el vector de etiquetas en predict.txt.
"""

from variables import *

def predecir(metodo, base):
  # TODO: Esto no va acá! debería estar al final, con la parte de cross validation
  testX = np.load(path + base)
  clf = pickle.load(open(path + metodo + base.replace("test","train") + '.pickle'))
  start = time.time()
  predy = list(clf.predict(testX))
  end = time.time()
  testy = np.load(path + 'testy.npy')
  testn = map(lambda x : ( 1 if x == 'ham' else 0 ), testy)
  predn = map(lambda x : ( 1 if x == 'ham' else 0 ), predy)
  d = datetime.datetime.now()
  f = open("data.txt",'a')
  #f.write("<" + str(d.day) + "/" + str(d.month) + "/" + str(d.year) + " " + str(d.hour) + "hs>\n")
  #f.write(metodo + " " + base + "\n")
  #TODO: obtener RedDim y cant_comp a partir del nombre de la base
  f.write(metodo + " " + redDim + " " + cant_comp + " ")
  f.write(str(end - start) + " ")
  #TODO: calcular prec, acc, roc, f1, recall... promedio y varianza con CV
  f.write(str(precision_score(testn, predn)) + " ")
  f.write(str(recall_score(testn, predn)) + " ")
  f.write(str(f1_score(testn, predn)) + " ")
  f.write(str(accuracy_score(testn, predn)) + " ")
  f.write(str(roc_auc_score(testn, predn)) + "\n")
  f.close()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    metodo = sys.argv[1]
    n = 2
    # TEST
    if metodo == 'Test':
      base = "testX.npy"
      if len(sys.argv) > n:
        metodo = sys.argv[n]
        n = n + 1
      else:
        print u'¿Qué método querés?'
        exit()
      if len(sys.argv) > n:
        base = sys.argv[n]
        n = n + 1
      else:
        print u'¿Qué base querés?'
        exit()
      predecir(metodo, base)
      exit()
    else:
      print "error"
      exit()
  else:
    print u'¿Qué método querés?'
    exit()
