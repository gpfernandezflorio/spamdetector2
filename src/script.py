import os

print "Cortar la base"
print("python cortaBase.py")
os.system("python cortaBase.py")

print "Elegir atributos"
print("python wordCounter.py")
os.system("python wordCounter.py")

print "Cargar atributos"
print("python cargaAtributos.py")
os.system("python cargaAtributos.py")

print "Reducir dimensiones"
for M in ["PCA","ICA"]:
  for n in [1,2,3,4,5,10,20,40,60,80,100]:
    print("python reducirDimensiones.py " + M + " " + str(n))
    os.system("python reducirDimensiones.py " + M + " " + str(n))

print "Grid Search"
for M in ["Dtree","Rforest","Nbayes","Knn","Svc"]:
  print("python gridSearch.py " + M)
  os.system("python gridSearch.py " + M)
  for B in ["PCA","ICA"]:
    for n in [1,2,3,4,5,10,20,40,60,80,100]:
      print("python gridSearch.py " + M + " " + B + "." + str(n) + ".npy")
      os.system("python gridSearch.py " + M + " " + B + "." + str(n) + ".npy")

print "Evaluar modelos (Cross Validation)"
for M in ["Dtree","Rforest","Nbayes","Knn","Svc"]:
  print("python validar.py " + M)
  os.system("python validar.py " + M)
  for B in ["PCA","ICA"]:
    for n in [1,2,3,4,5,10,20,40,60,80,100]:
      print("python validar.py " + M + " " + B + "." + str(n) + ".npy")
      os.system("python validar.py " + M + " " + B + "." + str(n) + ".npy")

print "Entrenar modelos"
for M in ["Dtree","Rforest","Nbayes","Knn","Svc"]:
  print("python entrenar.py " + M)
  os.system("python entrenar.py " + M)
  for B in ["PCA","ICA"]:
    for n in [10,100]:
      print("python entrenar.py " + M + " " + B + "." + str(n) + ".npy")
      os.system("python entrenar.py " + M + " " + B + "." + str(n) + ".npy")

print "Validar modelos (contra la base de validacion)"
for M in ["Dtree","Rforest","Nbayes","Knn","Svc"]:
  s = "python predecir.py " + M + ".trainX.npy.pickle testX.npy testy.npy"
  print s
  os.system(s)
  for B in ["PCA","ICA"]:
    for n in [10,100]:
      s = "python predecir.py " + M + "." + B + "." + str(n) + ".npy.pickle " + B + "." + str(n) + "-test.npy testy.npy"
      print s
      os.system(s)

print "Plotear medidas de la validacion"
print("python ploter.py")
os.system("python ploter.py")
