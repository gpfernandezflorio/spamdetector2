import os

for B in ["pca","ica"]:
  for M in ["pr","ac","re","f1","ro"]:
    print("gnuplot " + M + B + ".gnuplot")
    os.system("gnuplot " + M + B + ".gnuplot")

os.system("gnuplot tmica.gnuplot")
os.system("gnuplot tmpca.gnuplot")
