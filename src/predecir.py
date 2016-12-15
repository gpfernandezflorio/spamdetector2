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
  * La base debería coincidir en componentes con la base con la que el modelo fue entrenado.
  * La base y el vector de etiquetas deberían tener el mismo tamaño.

  Output: data.txt (append) | predict.txt.
  * Si se pasa un vector de etiquetas por parámetro, se modifica el achivo data.txt con las métricas.
  * En caso contrario, se genera el vector de etiquetas en predict.txt.
"""

from variables import *

def predecir(modelo, base, label):
  print modelo, base
  if label == None:
    print "sin label"
  else:
    print "Label:", label

  f_base = path + base
  if os.path.isfile(f_base):
    f_modelo = path + modelo
    if os.path.isfile(f_modelo):
      clf = pickle.load(open(f_modelo))
      testX = np.load(f_base)
    else:
      print "Error: No existe el archvivo \""+f_modelo+"\""
      exit()
  else:
    print "Error: No existe el archvivo \""+f_base+"\""
    exit()

  start = time.time()
  predy = list(clf.predict(testX))
  end = time.time()

  if label == None:
    f = open("predict.txt",'w')
    for p in predy:
      f.write(p + "\n")
    f.close()
    exit()

  f_label = path + label
  if os.path.isfile(f_label):
    testy = np.load(f_label)
  else:
    print "Error: No existe el archvivo \""+f_label+"\""
    exit()

  testn = map(lambda x : ( 0 if x == 'ham' else 1 ), testy)
  predn = map(lambda x : ( 0 if x == 'ham' else 1 ), predy)
  f = open("data.txt",'a')
  f.write(modelo + " " + base + " ")
  f.write(str(end - start) + " ")
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
    base = "testX.npy"
    label = None
    if len(sys.argv) > n:
      base = sys.argv[n]
      n = n + 1
      if len(sys.argv) > n:
        label = sys.argv[n]
        n = n + 1
    predecir(metodo, base, label)
  else:
    print u'¿Qué método querés?'
