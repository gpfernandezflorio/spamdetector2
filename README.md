# spamdetector2
TODO (escribir esto en el informe):
Debido a que habíamos sacado los atributos sobre todos los mails y no solamente de parte de train
como debería haberse hecho consideramos que teníamos que realizar la expermientqación de nuevo.

Lo primero que hicimos fue dividir a la base de mails en dos dataframes, la de train y la de test.
Sobre la base de train sacamos las palabras más frecuentes para tener como atributo la cantidad de esas palabras.

INSTRUCCIONES:
1º: Ejecutar python cortaBase.py (esto sólo se hace una vez)
  - Genera train.npy y test.npy nuestras bases de train y test. Ya las tenemos guardadas en Drive
2º: Ejecutar python wordCounter.py
  - Lee la base de train y genera el archivo attributes.py con los atributos.
  - Puede requerir un retoque manual para los atributos que tengan comillas simples: Reemplazarlas por: \'
3º: Ejecutar python cargaAtributos.py
  - Toma ambas bases (train.npy y test.npy) y genera los dataframes con los atributos generados en el paso anterior.
  - Genera los archivos trainX.npy, testX.npy, trainy.npy y testy.npy
TO BE CONTINUED...
