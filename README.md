# spamdetector2
TODO (escribir esto en el informe):
Debido a que habíamos sacado los atributos sobre todos los mails y no solamente de parte de train
como debería haberse hecho consideramos que teníamos que realizar la expermientqación de nuevo.

Lo primero que hicimos fue dividir a la base de mails en dos dataframes, la de train y la de test.
Sobre la base de train sacamos las palabras más frecuentes para tener como atributo la cantidad de esas palabras.

### INSTRUCCIONES:

1. Ejecutar python cortaBase.py (esto sólo se hace una vez)
   * Genera train.npy y test.npy nuestras bases de train y test. Ya las tenemos guardadas en Drive
2.  Ejecutar python wordCounter.py
   * Lee la base de train y genera el archivo attributes.py con los atributos.
   * Puede requerir un retoque manual para los atributos que tengan comillas simples: Reemplazarlas por: \'
3.  Ejecutar python cargaAtributos.py
   * Toma ambas bases (train.npy y test.npy) y genera los dataframes con los atributos generados en el paso anterior.
   * Genera los archivos trainX.npy, testX.npy, trainy.npy y testy.npy
4. Ejecutar python reducirDimensiones.py M n
   * Variando M entre PCA y ICA.
   * Variando n entre 1,2,3,4,5,10,15,25,50 y 100
   * Genera los archivos M.n.npy
5. Ejecutar gridSearch.py M B
   * Variando M entre Dtree, Rforest, Nbayes, Knn, Svc
   * Variando B entre trainX.npy y cada base generada en el paso 4.
6. Ejecutar python validar.py M B
   * Variando M entre Dtree, Rforest, Nbayes, Knn, Svc
   * Variando B entre trainX.npy y cada base generada en el paso 4.
   * Escribe en cv.txt las métricas resultantes de validar el modelo para ser ploteadas.
7. Ejecutar python entrenar.py M B
   * Variando M entre cada uno de los métodos seleccionados.
   * Con B la base seleccionada para cada método.

# TODO
8. Ejecutar python predecir.py

9. Ejecutar python ploter.py
  * Genera en la carpeta data, todos los archivos .dat
10. Ejecutar, dentro de la carpeta data, python plotall.py
  * gnuplotea todos los gráficos