#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [9] Ploter.

  Descripción: Grafica resultados.

  Uso: python ploter.py

  Requiere el archivo data.txt

  Output: ?
"""

import matplotlib.pyplot as plt

f1ica = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
prica = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
rcica = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
acica = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
roica = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}

f1pca = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
prpca = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
rcpca = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
acpca = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}
ropca = {"Dtree":{},"Rforest":{},"Nbayes":{},"Knn":{},"Svc":{}}

f1 = {}

fname = 'cv.txt'

lines = [line.rstrip('\n') for line in open(fname,'r')]

for line in lines:
	data = line.split(" ")
	if data[1] == "ICA":
		f1ica[data[0]][data[2]] = float(data[6])
		prica[data[0]][data[2]] = float(data[4])
		rcica[data[0]][data[2]] = float(data[5])
		acica[data[0]][data[2]] = float(data[7])
		roica[data[0]][data[2]] = float(data[8])
	elif data[1] == "PCA":
		f1pca[data[0]][data[2]] = float(data[6])
		prpca[data[0]][data[2]] = float(data[4])
		rcpca[data[0]][data[2]] = float(data[5])
		acpca[data[0]][data[2]] = float(data[7])
		ropca[data[0]][data[2]] = float(data[8])
	elif data[1] == "NULL":
		f1[data[0]] = float(data[6])
		pr[data[0]] = float(data[4])
		rc[data[0]] = float(data[5])
		ac[data[0]] = float(data[7])
		ro[data[0]] = float(data[8])


