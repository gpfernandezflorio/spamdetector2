# spamdetector2

### INSTRUCCIONES:

1. Ejecutar python cortaBase.py
   * A partir de los archivos json, genera train.npy y test.npy nuestras bases de desarrollo y validación.

2.  Ejecutar python wordCounter.py
   * Lee la base de desarrollo (train.npy) y genera el archivo attributes.py con los atributos.

3.  Ejecutar python cargaAtributos.py
   * Toma ambas bases (train.npy y test.npy) y genera los dataframes con los atributos generados en el paso anterior.
   * Genera los archivos trainX.npy, testX.npy, trainy.npy y testy.npy

4. Ejecutar python reducirDimensiones.py M n
   * Variando M entre PCA y ICA.
   * Variando n entre 1, 2, 3, 4, 5, 10, 20, 40, 60, 80 y 100
   * Genera los archivos M.n.npy

5. Ejecutar gridSearch.py M B
   * Variando M entre Dtree, Rforest, Nbayes, Knn y Svc
   * Variando B entre trainX.npy y cada base generada en el paso 4.
   * Genera un archivo .param con el diccionario de parámetros elegidos.

6. Ejecutar python validar.py M B
   * Variando M entre Dtree, Rforest, Nbayes, Knn y Svc
   * Variando B entre trainX.npy y cada base generada en el paso 4.
   * Escribe en cv.txt las métricas resultantes de validar el modelo para ser ploteadas.

7. Ejecutar python entrenar.py M B
   * Variando M entre Dtree, Rforest, Nbayes, Knn y Svc.
   * Variando B entre trainX.npy, PCA.10.npy, PCA.100.npy, ICA.10.npy y ICA.100.npy.

8. (a) Ejecutar python predecir.py M.trainX.npy.pickle testX.npy testy.npy
   * Variando M entre Dtree, Rforest, Nbayes, Knn y Svc.
8. (b) Ejecutar python predecir.py M.B.npy.pickle B-test.npy testy.npy
   * Variando M entre Dtree, Rforest, Nbayes, Knn y Svc.
   * Variando B entre PCA.10, PCA.100, ICA.10 y ICA.100

9. Ejecutar python ploter.py
  * Genera en la carpeta data, todos los archivos .dat

10. Ejecutar, dentro de la carpeta data, python plotall.py
  * gnuplotea todos los gráficos
