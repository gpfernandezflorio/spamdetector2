#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [9] Ploter.

  Descripción: Grafica resultados.

  Uso: python ploter.py

  Requiere el archivo cv.txt

  Output: Todos los archivos .dat necesarios para generar los gráficos.
  * En la carpeta data
"""

M = 201

tmica = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
f1ica = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
prica = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
reica = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
acica = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
roica = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}

tmpca = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
f1pca = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
prpca = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
repca = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
acpca = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}
ropca = {"Dtree":[None]*M,"Rforest":[None]*M,"Nbayes":[None]*M,"Knn":[None]*M,"Svc":[None]*M}

tm = {}
f1 = {}
pr = {}
re = {}
ac = {}
ro = {}

fname = 'cv.txt'

lines = [line.rstrip('\n') for line in open(fname,'r')]

for line in lines:
	data = line.split(" ")
	if data[1] == "ICA":
		tmica[data[0]][int(data[2])] = [data[3],data[9]]
		f1ica[data[0]][int(data[2])] = [data[6],data[12]]
		prica[data[0]][int(data[2])] = [data[4],data[10]]
		reica[data[0]][int(data[2])] = [data[5],data[11]]
		acica[data[0]][int(data[2])] = [data[7],data[13]]
		roica[data[0]][int(data[2])] = [data[8],data[14]]
	elif data[1] == "PCA":
		tmpca[data[0]][int(data[2])] = [data[3],data[9]]
		f1pca[data[0]][int(data[2])] = [data[6],data[12]]
		prpca[data[0]][int(data[2])] = [data[4],data[10]]
		repca[data[0]][int(data[2])] = [data[5],data[11]]
		acpca[data[0]][int(data[2])] = [data[7],data[13]]
		ropca[data[0]][int(data[2])] = [data[8],data[14]]
	elif data[1] == "NULL":
		tm[data[0]] = [data[3],data[9]]
		f1[data[0]] = [data[6],data[12]]
		pr[data[0]] = [data[4],data[10]]
		re[data[0]] = [data[5],data[11]]
		ac[data[0]] = [data[7],data[13]]
		ro[data[0]] = [data[8],data[14]]

if "Dtree" in tm:
  f = open('data/dttm.dat','w')
  f.write(str(1) + ' "Decision Tree" ' + str(tm["Dtree"][0]) + " " + str(tm["Dtree"][1]) + "\n")
  f.close()
if "Rforest" in tm:
  f = open('data/rftm.dat','w')
  f.write(str(2) + ' "Random Forest" ' + str(tm["Rforest"][0]) + " " + str(tm["Rforest"][1]) + "\n")
  f.close()
if "Nbayes" in tm:
  f = open('data/nbtm.dat','w')
  f.write(str(3) + ' "Naive Bayes" ' + str(tm["Nbayes"][0]) + " " + str(tm["Nbayes"][1]) + "\n")
  f.close()
if "Knn" in tm:
  f = open('data/knntm.dat','w')
  f.write(str(4) + " KNN " + str(tm["Knn"][0]) + " " + str(tm["Knn"][1]) + "\n")
  f.close()
if "Svc" in tm:
  f = open('data/svctm.dat','w')
  f.write(str(5) + " SVM " + str(tm["Svc"][0]) + " " + str(tm["Svc"][1]) + "\n")
  f.close()

if "Dtree" in f1:
  f = open('data/dtf1.dat','w')
  f.write(str(1) + ' "Decision Tree" ' + str(f1["Dtree"][0]) + " " + str(f1["Dtree"][1]) + "\n")
  f.close()
if "Rforest" in f1:
  f = open('data/rff1.dat','w')
  f.write(str(2) + ' "Random Forest" ' + str(f1["Rforest"][0]) + " " + str(f1["Rforest"][1]) + "\n")
  f.close()
if "Nbayes" in f1:
  f = open('data/nbf1.dat','w')
  f.write(str(3) + ' "Naive Bayes" ' + str(f1["Nbayes"][0]) + " " + str(f1["Nbayes"][1]) + "\n")
  f.close()
if "Knn" in f1:
  f = open('data/knnf1.dat','w')
  f.write(str(4) + " KNN " + str(f1["Knn"][0]) + " " + str(f1["Knn"][1]) + "\n")
  f.close()
if "Svc" in f1:
  f = open('data/svcf1.dat','w')
  f.write(str(5) + " SVM " + str(f1["Svc"][0]) + " " + str(f1["Svc"][1]) + "\n")
  f.close()

if "Dtree" in pr:
  f = open('data/dtpr.dat','w')
  f.write(str(1) + ' "Decision Tree" ' + str(pr["Dtree"][0]) + " " + str(pr["Dtree"][1]) + "\n")
  f.close()
if "Rforest" in pr:
  f = open('data/rfpr.dat','w')
  f.write(str(2) + ' "Random Forest" ' + str(pr["Rforest"][0]) + " " + str(pr["Rforest"][1]) + "\n")
  f.close()
if "Nbayes" in pr:
  f = open('data/nbpr.dat','w')
  f.write(str(3) + ' "Naive Bayes" ' + str(pr["Nbayes"][0]) + " " + str(pr["Nbayes"][1]) + "\n")
  f.close()
if "Knn" in pr:
  f = open('data/knnpr.dat','w')
  f.write(str(4) + " KNN " + str(pr["Knn"][0]) + " " + str(pr["Knn"][1]) + "\n")
  f.close()
if "Svc" in pr:
  f = open('data/svcpr.dat','w')
  f.write(str(5) + " SVM " + str(pr["Svc"][0]) + " " + str(pr["Svc"][1]) + "\n")
  f.close()

if "Dtree" in re:
  f = open('data/dtre.dat','w')
  f.write(str(1) + ' "Decision Tree" ' + str(re["Dtree"][0]) + " " + str(re["Dtree"][1]) + "\n")
  f.close()
if "Rforest" in re:
  f = open('data/rfre.dat','w')
  f.write(str(2) + ' "Random Forest" ' + str(re["Rforest"][0]) + " " + str(re["Rforest"][1]) + "\n")
  f.close()
if "Nbayes" in re:
  f = open('data/nbre.dat','w')
  f.write(str(3) + ' "Naive Bayes" ' + str(re["Nbayes"][0]) + " " + str(re["Nbayes"][1]) + "\n")
  f.close()
if "Knn" in re:
  f = open('data/knnre.dat','w')
  f.write(str(4) + " KNN " + str(re["Knn"][0]) + " " + str(re["Knn"][1]) + "\n")
  f.close()
if "Svc" in re:
  f = open('data/svcre.dat','w')
  f.write(str(5) + " SVM " + str(re["Svc"][0]) + " " + str(re["Svc"][1]) + "\n")
  f.close()

if "Dtree" in ro:
  f = open('data/dtro.dat','w')
  f.write(str(1) + ' "Decision Tree" ' + str(ro["Dtree"][0]) + " " + str(ro["Dtree"][1]) + "\n")
  f.close()
if "Rforest" in ro:
  f = open('data/rfro.dat','w')
  f.write(str(2) + ' "Random Forest" ' + str(ro["Rforest"][0]) + " " + str(ro["Rforest"][1]) + "\n")
  f.close()
if "Nbayes" in ro:
  f = open('data/nbro.dat','w')
  f.write(str(3) + ' "Naive Bayes" ' + str(ro["Nbayes"][0]) + " " + str(ro["Nbayes"][1]) + "\n")
  f.close()
if "Knn" in ro:
  f = open('data/knnro.dat','w')
  f.write(str(4) + " KNN " + str(ro["Knn"][0]) + " " + str(ro["Knn"][1]) + "\n")
  f.close()
if "Svc" in ro:
  f = open('data/svcro.dat','w')
  f.write(str(5) + " SVM " + str(ro["Svc"][0]) + " " + str(ro["Svc"][1]) + "\n")
  f.close()

if "Dtree" in ac:
  f = open('data/dtac.dat','w')
  f.write(str(1) + ' "Decision Tree" ' + str(ac["Dtree"][0]) + " " + str(ac["Dtree"][1]) + "\n")
  f.close()
if "Rforest" in ac:
  f = open('data/rfac.dat','w')
  f.write(str(2) + ' "Random Forest" ' + str(ac["Rforest"][0]) + " " + str(ac["Rforest"][1]) + "\n")
  f.close()
if "Nbayes" in ac:
  f = open('data/nbac.dat','w')
  f.write(str(3) + ' "Naive Bayes" ' + str(ac["Nbayes"][0]) + " " + str(ac["Nbayes"][1]) + "\n")
  f.close()
if "Knn" in ac:
  f = open('data/knnac.dat','w')
  f.write(str(4) + " KNN " + str(ac["Knn"][0]) + " " + str(ac["Knn"][1]) + "\n")
  f.close()
if "Svc" in ac:
  f = open('data/svcac.dat','w')
  f.write(str(5) + " SVM " + str(ac["Svc"][0]) + " " + str(ac["Svc"][1]) + "\n")
  f.close()

f = open('data/dttmica.dat','w')
for i in range(len(tmica["Dtree"])):
  if not tmica["Dtree"][i] == None:
    f.write(str(i) + " " + str(tmica["Dtree"][i][0]) + " " + str(tmica["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rftmica.dat','w')
for i in range(len(tmica["Rforest"])):
  if not tmica["Rforest"][i] == None:
    f.write(str(i) + " " + str(tmica["Rforest"][i][0]) + " " + str(tmica["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbtmica.dat','w')
for i in range(len(tmica["Nbayes"])):
  if not tmica["Nbayes"][i] == None:
    f.write(str(i) + " " + str(tmica["Nbayes"][i][0]) + " " + str(tmica["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knntmica.dat','w')
for i in range(len(tmica["Knn"])):
  if not tmica["Knn"][i] == None:
    f.write(str(i) + " " + str(tmica["Knn"][i][0]) + " " + str(tmica["Knn"][i][1]) + "\n")
f.close()
f = open('data/svctmica.dat','w')
for i in range(len(tmica["Svc"])):
  if not tmica["Svc"][i] == None:
    f.write(str(i) + " " + str(tmica["Svc"][i][0]) + " " + str(tmica["Svc"][i][1]) + "\n")
f.close()

f = open('data/dttmpca.dat','w')
for i in range(len(tmpca["Dtree"])):
  if not tmpca["Dtree"][i] == None:
    f.write(str(i) + " " + str(tmpca["Dtree"][i][0]) + " " + str(tmpca["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rftmpca.dat','w')
for i in range(len(tmpca["Rforest"])):
  if not tmpca["Rforest"][i] == None:
    f.write(str(i) + " " + str(tmpca["Rforest"][i][0]) + " " + str(tmpca["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbtmpca.dat','w')
for i in range(len(tmpca["Nbayes"])):
  if not tmpca["Nbayes"][i] == None:
    f.write(str(i) + " " + str(tmpca["Nbayes"][i][0]) + " " + str(tmpca["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knntmpca.dat','w')
for i in range(len(tmpca["Knn"])):
  if not tmpca["Knn"][i] == None:
    f.write(str(i) + " " + str(tmpca["Knn"][i][0]) + " " + str(tmpca["Knn"][i][1]) + "\n")
f.close()
f = open('data/svctmpca.dat','w')
for i in range(len(tmpca["Svc"])):
  if not tmpca["Svc"][i] == None:
    f.write(str(i) + " " + str(tmpca["Svc"][i][0]) + " " + str(tmpca["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtf1ica.dat','w')
for i in range(len(f1ica["Dtree"])):
  if not f1ica["Dtree"][i] == None:
    f.write(str(i) + " " + str(f1ica["Dtree"][i][0]) + " " + str(f1ica["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rff1ica.dat','w')
for i in range(len(f1ica["Rforest"])):
  if not f1ica["Rforest"][i] == None:
    f.write(str(i) + " " + str(f1ica["Rforest"][i][0]) + " " + str(f1ica["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbf1ica.dat','w')
for i in range(len(f1ica["Nbayes"])):
  if not f1ica["Nbayes"][i] == None:
    f.write(str(i) + " " + str(f1ica["Nbayes"][i][0]) + " " + str(f1ica["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnf1ica.dat','w')
for i in range(len(f1ica["Knn"])):
  if not f1ica["Knn"][i] == None:
    f.write(str(i) + " " + str(f1ica["Knn"][i][0]) + " " + str(f1ica["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcf1ica.dat','w')
for i in range(len(f1ica["Svc"])):
  if not f1ica["Svc"][i] == None:
    f.write(str(i) + " " + str(f1ica["Svc"][i][0]) + " " + str(f1ica["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtprica.dat','w')
for i in range(len(prica["Dtree"])):
  if not prica["Dtree"][i] == None:
    f.write(str(i) + " " + str(prica["Dtree"][i][0]) + " " + str(prica["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfprica.dat','w')
for i in range(len(prica["Rforest"])):
  if not prica["Rforest"][i] == None:
    f.write(str(i) + " " + str(prica["Rforest"][i][0]) + " " + str(prica["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbprica.dat','w')
for i in range(len(prica["Nbayes"])):
  if not prica["Nbayes"][i] == None:
    f.write(str(i) + " " + str(prica["Nbayes"][i][0]) + " " + str(prica["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnprica.dat','w')
for i in range(len(prica["Knn"])):
  if not prica["Knn"][i] == None:
    f.write(str(i) + " " + str(prica["Knn"][i][0]) + " " + str(prica["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcprica.dat','w')
for i in range(len(prica["Svc"])):
  if not prica["Svc"][i] == None:
    f.write(str(i) + " " + str(prica["Svc"][i][0]) + " " + str(prica["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtreica.dat','w')
for i in range(len(reica["Dtree"])):
  if not reica["Dtree"][i] == None:
    f.write(str(i) + " " + str(reica["Dtree"][i][0]) + " " + str(reica["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfreica.dat','w')
for i in range(len(reica["Rforest"])):
  if not reica["Rforest"][i] == None:
    f.write(str(i) + " " + str(reica["Rforest"][i][0]) + " " + str(reica["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbreica.dat','w')
for i in range(len(reica["Nbayes"])):
  if not reica["Nbayes"][i] == None:
    f.write(str(i) + " " + str(reica["Nbayes"][i][0]) + " " + str(reica["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnreica.dat','w')
for i in range(len(reica["Knn"])):
  if not reica["Knn"][i] == None:
    f.write(str(i) + " " + str(reica["Knn"][i][0]) + " " + str(reica["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcreica.dat','w')
for i in range(len(reica["Svc"])):
  if not reica["Svc"][i] == None:
    f.write(str(i) + " " + str(reica["Svc"][i][0]) + " " + str(reica["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtacica.dat','w')
for i in range(len(acica["Dtree"])):
  if not acica["Dtree"][i] == None:
    f.write(str(i) + " " + str(acica["Dtree"][i][0]) + " " + str(acica["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfacica.dat','w')
for i in range(len(acica["Rforest"])):
  if not acica["Rforest"][i] == None:
    f.write(str(i) + " " + str(acica["Rforest"][i][0]) + " " + str(acica["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbacica.dat','w')
for i in range(len(acica["Nbayes"])):
  if not acica["Nbayes"][i] == None:
    f.write(str(i) + " " + str(acica["Nbayes"][i][0]) + " " + str(acica["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnacica.dat','w')
for i in range(len(acica["Knn"])):
  if not acica["Knn"][i] == None:
    f.write(str(i) + " " + str(acica["Knn"][i][0]) + " " + str(acica["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcacica.dat','w')
for i in range(len(acica["Svc"])):
  if not acica["Svc"][i] == None:
    f.write(str(i) + " " + str(acica["Svc"][i][0]) + " " + str(acica["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtroica.dat','w')
for i in range(len(roica["Dtree"])):
  if not roica["Dtree"][i] == None:
    f.write(str(i) + " " + str(roica["Dtree"][i][0]) + " " + str(roica["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfroica.dat','w')
for i in range(len(roica["Rforest"])):
  if not roica["Rforest"][i] == None:
    f.write(str(i) + " " + str(roica["Rforest"][i][0]) + " " + str(roica["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbroica.dat','w')
for i in range(len(roica["Nbayes"])):
  if not roica["Nbayes"][i] == None:
    f.write(str(i) + " " + str(roica["Nbayes"][i][0]) + " " + str(roica["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnroica.dat','w')
for i in range(len(roica["Knn"])):
  if not roica["Knn"][i] == None:
    f.write(str(i) + " " + str(roica["Knn"][i][0]) + " " + str(roica["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcroica.dat','w')
for i in range(len(roica["Svc"])):
  if not roica["Svc"][i] == None:
    f.write(str(i) + " " + str(roica["Svc"][i][0]) + " " + str(roica["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtf1pca.dat','w')
for i in range(len(f1pca["Dtree"])):
  if not f1pca["Dtree"][i] == None:
    f.write(str(i) + " " + str(f1pca["Dtree"][i][0]) + " " + str(f1pca["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rff1pca.dat','w')
for i in range(len(f1pca["Rforest"])):
  if not f1pca["Rforest"][i] == None:
    f.write(str(i) + " " + str(f1pca["Rforest"][i][0]) + " " + str(f1pca["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbf1pca.dat','w')
for i in range(len(f1pca["Nbayes"])):
  if not f1pca["Nbayes"][i] == None:
    f.write(str(i) + " " + str(f1pca["Nbayes"][i][0]) + " " + str(f1pca["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnf1pca.dat','w')
for i in range(len(f1pca["Knn"])):
  if not f1pca["Knn"][i] == None:
    f.write(str(i) + " " + str(f1pca["Knn"][i][0]) + " " + str(f1pca["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcf1pca.dat','w')
for i in range(len(f1pca["Svc"])):
  if not f1pca["Svc"][i] == None:
    f.write(str(i) + " " + str(f1pca["Svc"][i][0]) + " " + str(f1pca["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtprpca.dat','w')
for i in range(len(prpca["Dtree"])):
  if not prpca["Dtree"][i] == None:
    f.write(str(i) + " " + str(prpca["Dtree"][i][0]) + " " + str(prpca["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfprpca.dat','w')
for i in range(len(prpca["Rforest"])):
  if not prpca["Rforest"][i] == None:
    f.write(str(i) + " " + str(prpca["Rforest"][i][0]) + " " + str(prpca["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbprpca.dat','w')
for i in range(len(prpca["Nbayes"])):
  if not prpca["Nbayes"][i] == None:
    f.write(str(i) + " " + str(prpca["Nbayes"][i][0]) + " " + str(prpca["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnprpca.dat','w')
for i in range(len(prpca["Knn"])):
  if not prpca["Knn"][i] == None:
    f.write(str(i) + " " + str(prpca["Knn"][i][0]) + " " + str(prpca["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcprpca.dat','w')
for i in range(len(prpca["Svc"])):
  if not prpca["Svc"][i] == None:
    f.write(str(i) + " " + str(prpca["Svc"][i][0]) + " " + str(prpca["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtrepca.dat','w')
for i in range(len(repca["Dtree"])):
  if not repca["Dtree"][i] == None:
    f.write(str(i) + " " + str(repca["Dtree"][i][0]) + " " + str(repca["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfrepca.dat','w')
for i in range(len(repca["Rforest"])):
  if not repca["Rforest"][i] == None:
    f.write(str(i) + " " + str(repca["Rforest"][i][0]) + " " + str(repca["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbrepca.dat','w')
for i in range(len(repca["Nbayes"])):
  if not repca["Nbayes"][i] == None:
    f.write(str(i) + " " + str(repca["Nbayes"][i][0]) + " " + str(repca["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnrepca.dat','w')
for i in range(len(repca["Knn"])):
  if not repca["Knn"][i] == None:
    f.write(str(i) + " " + str(repca["Knn"][i][0]) + " " + str(repca["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcrepca.dat','w')
for i in range(len(repca["Svc"])):
  if not repca["Svc"][i] == None:
    f.write(str(i) + " " + str(repca["Svc"][i][0]) + " " + str(repca["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtacpca.dat','w')
for i in range(len(acpca["Dtree"])):
  if not acpca["Dtree"][i] == None:
    f.write(str(i) + " " + str(acpca["Dtree"][i][0]) + " " + str(acpca["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfacpca.dat','w')
for i in range(len(acpca["Rforest"])):
  if not acpca["Rforest"][i] == None:
    f.write(str(i) + " " + str(acpca["Rforest"][i][0]) + " " + str(acpca["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbacpca.dat','w')
for i in range(len(acpca["Nbayes"])):
  if not acpca["Nbayes"][i] == None:
    f.write(str(i) + " " + str(acpca["Nbayes"][i][0]) + " " + str(acpca["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnacpca.dat','w')
for i in range(len(acpca["Knn"])):
  if not acpca["Knn"][i] == None:
    f.write(str(i) + " " + str(acpca["Knn"][i][0]) + " " + str(acpca["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcacpca.dat','w')
for i in range(len(acpca["Svc"])):
  if not acpca["Svc"][i] == None:
    f.write(str(i) + " " + str(acpca["Svc"][i][0]) + " " + str(acpca["Svc"][i][1]) + "\n")
f.close()

f = open('data/dtropca.dat','w')
for i in range(len(ropca["Dtree"])):
  if not ropca["Dtree"][i] == None:
    f.write(str(i) + " " + str(ropca["Dtree"][i][0]) + " " + str(ropca["Dtree"][i][1]) + "\n")
f.close()
f = open('data/rfropca.dat','w')
for i in range(len(ropca["Rforest"])):
  if not ropca["Rforest"][i] == None:
    f.write(str(i) + " " + str(ropca["Rforest"][i][0]) + " " + str(ropca["Rforest"][i][1]) + "\n")
f.close()
f = open('data/nbropca.dat','w')
for i in range(len(ropca["Nbayes"])):
  if not ropca["Nbayes"][i] == None:
    f.write(str(i) + " " + str(ropca["Nbayes"][i][0]) + " " + str(ropca["Nbayes"][i][1]) + "\n")
f.close()
f = open('data/knnropca.dat','w')
for i in range(len(ropca["Knn"])):
  if not ropca["Knn"][i] == None:
    f.write(str(i) + " " + str(ropca["Knn"][i][0]) + " " + str(ropca["Knn"][i][1]) + "\n")
f.close()
f = open('data/svcropca.dat','w')
for i in range(len(ropca["Svc"])):
  if not ropca["Svc"][i] == None:
    f.write(str(i) + " " + str(ropca["Svc"][i][0]) + " " + str(ropca["Svc"][i][1]) + "\n")
f.close()
