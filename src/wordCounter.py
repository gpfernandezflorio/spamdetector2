#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import numpy as np
from collections import Counter
import pandas as pd

estoy_en_los_labos = True
prueba_full = True

train = np.load('train.npy')
print "Base Cargada"

ham = [x[0] for x in train if x[1] == 'ham']
spam = [x[0] for x in train if x[1] == 'spam']

print "Divididos Ham/Spam"

ham_counter = Counter()
spam_counter = Counter()

for s in spam:
    for w in s.split(" "):
        spam_counter[w] += 1

for s in ham:
    for w in s.split(" "):
        ham_counter[w] += 1

print "Palabras Contadas"

spam_words = Counter()
proportions = Counter()

for s in spam_counter:
    if s in ham_counter.keys():
        proportions[s] = float(spam_counter[s]) / float(ham_counter[s])
    else:
        spam_words[s] = float(spam_counter[s])

print "Proporciones Calculadas"

proportions_list = proportions.most_common()
spam_words_list = spam_words.most_common()

cant_words = 10
st1 = "dnames = ['len',"
st2 = ""
st3 = "dfuncs = [len,"
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
print st1
print st2
print st3
