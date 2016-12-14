import os

for M in ["pr","ac","re","f1","ro"]:
  print("gnuplot " + M + ".gnuplot")
  os.system("gnuplot " + M + ".gnuplot")
  for B in ["pca","ica"]:
    print("gnuplot " + M + B + ".gnuplot")
    os.system("gnuplot " + M + B + ".gnuplot")

os.system("gnuplot tmica.gnuplot")
os.system("gnuplot tmpca.gnuplot")
os.system("gnuplot tm.gnuplot")
