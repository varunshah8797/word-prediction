# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:56:39 2019

@author: chirag_vadodariya
"""
#%%
# IMPORTING THE TEXT FOR TRAINING OF THE MODEL
import string
dataset_train = open('try_text.txt' , encoding='ANSI')
text = dataset_train.read()
dataset_train.close()

# PRE-PROCESSING THE DATA IMPORTED(CLEANING)
text = text.replace('--',' ')
text = text.replace('??',' ')
text = text.replace('?',' ')
text = text.replace('_',' ')
text = text.replace('*',' ')
tokens = text.split()
table = str.maketrans('', '', string.punctuation)
tokens = [w.translate(table) for w in tokens]
tokens = [word for word in tokens if word.isalpha()]
tokens = [word.lower() for word in tokens]

length = 20 + 1
training_set_clean = list()
t=list()
for i in range(length, len(tokens)):
    seq = tokens[i-length:i]
    line = ' '.join(seq)
    training_set_clean.append(line)
    t.append(line)
    #print(line)
    #print()
print(t)
#with open('training_set_clean.txt', 'wb') as fp:
#   pickle.dump(training_set_clean, fp)

# IMPORTING THE TEXT FOR TRAINING OF THE MODEL
#dataset_clean = open('training_set_clean.txt' , encoding='ISO-8859-1')

"""training_set = dataset_clean.read()
dataset_clean.close()"""
#%%