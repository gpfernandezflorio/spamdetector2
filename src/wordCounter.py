#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [2] WordCounter.

  Descripción: Determina las palabras más "spam".

  Uso: python wordCounter.py
  * si estoy_en_los_labos los va a buscar en /media/libre/aa/.
  * si no, en el mismo directorio.

  Output: attributes.py
  * Tras ejecutarlo, revisar el archivo de salida y reemplazar las apariciones de ' por \', dentro de los strings.
"""

from variables import *

if estoy_en_los_labos:
    train = np.load('/media/libre/aa/train.npy')
else:
    train = np.load('train.npy')

print "Base Cargada"

ham = [x[0] for x in train if x[1] == 'ham']
spam = [x[0] for x in train if x[1] == 'spam']

print "Divididos Ham/Spam"

ham_counter = Counter()
spam_counter = Counter()

for s in spam:
    for w in s.split():
        spam_counter[w] += 1

for s in ham:
    for w in s.split():
        ham_counter[w] += 1

print "Palabras Contadas"

spam_words = Counter()
proportions = Counter()

for s in spam_counter:
    if s in ham_counter:
        proportions[s] = float(spam_counter[s]) / float(ham_counter[s])
    else:
        spam_words[s] = float(spam_counter[s])

print "Proporciones Calculadas"

cant_words = 100
spam_words_list = spam_words.most_common(cant_words)
proportions_list = proportions.most_common(cant_words)

st1 = u"#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n"

st1 += "dnames = ['len',"
st2 = u""
st3 = u"dfuncs = [len,"
h=0
for t in proportions_list:
    h = h+1
    st1 += "'a" + str(h) + "',"
    st3 += "a" + str(h) + ","
    #st2 += "def a" + str(h) + "(txt): return txt.count('" + t[0].replace("'","\\'") + "')\n"
    st2 += "def a" + str(h) + "(txt): return txt.count('" + t[0] + "')\n"
    if h == cant_words:
        break
for t in spam_words_list:
    h = h+1
    st1 += "'a" + str(h) + "',"
    st3 += "a" + str(h) + ","
    #st2 += "def a" + str(h) + "(txt): return txt.count('" + t[0].replace("'","\\'") + "')\n"
    st2 += "def a" + str(h) + "(txt): return txt.count('" + t[0] + "')\n"
st1= st1[0:-1] + "]"
st3= st3[0:-1] + "]"
#print st1
#print st2
#print st3
f = open('attributes.py','w')
f.write(st1+u'\n'+st2+u'\n'+st3)
f.close()
