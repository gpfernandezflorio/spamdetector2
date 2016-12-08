import os

#print "Cortar la base"
#print("python cortaBase.py")
#os.system("python cortaBase.py")

#print "Elegir atributos"
#print("python wordCounter.py")
#os.system("python wordCounter.py")

#print "Cargar atributos"
#print("python cargaAtributos.py")
#os.system("python cargaAtributos.py")

print "Reducir dimensiones"
for M in ["PCA","ICA"]:
  for n in [1,2,3,4,5,10,20,40,60,80,100]:
    print("python reducirDimensiones.py " + M + " " + str(n))
    os.system("python reducirDimensiones.py " + M + " " + str(n))

print "Validar modelos"
for M in ["Dtree","Rforest","Nbayes","Knn"]:
  print("python validar.py " + M)
  os.system("python validar.py " + M)
  for B in ["PCA","ICA"]:
    for n in [1,2,3,4,5,10,20,40,60,80,100]:
      print("python validar.py " + M + " " + B + "." + str(n) + ".npy")
      os.system("python validar.py " + M + " " + B + "." + str(n) + ".npy")
