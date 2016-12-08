#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

"""
  Modulo de TP Spam Detector. [1] CortaBase.

  Descripción: Divide la base completa en train y test.

  Uso: python cortaBase.py

  Output: train.npy | test.npy
  * si estoy_en_los_labos los guarda en /media/libre/aa/.
  * si no, en el mismo directorio.
"""

from variables import *

if __name__ == '__main__':
    print 'Cargando ham'
    if not prueba_full:
        ham_txt = json.load(open('../ham_dev_mini.json'))
    elif estoy_en_los_labos:
        ham_txt = json.load(open('/media/libre/dataset_dev/ham_dev.json'))
    else:
        ham_txt = json.load(open('../ham_dev.json'))
    print 'Cargando spam'
    if not prueba_full:
        spam_txt = json.load(open('../spam_dev_mini.json'))
    elif estoy_en_los_labos:
        spam_txt = json.load(open('/media/libre/dataset_dev/spam_dev.json'))
    else:
        spam_txt = json.load(open('../spam_dev.json'))

    df = pd.DataFrame(ham_txt+spam_txt, columns=['text'])
    df['class'] = ['ham' for _ in range(len(ham_txt))]+['spam' for _ in range(len(spam_txt))]
    train, test = train_test_split(df, test_size = 0.2)
    if estoy_en_los_labos:
        np.save('/media/libre/aa/train', train)
        np.save('/media/libre/aa/test', test)
    else:
        np.save('train', train)
        np.save('test', test)
