# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:18:27 2022

@author: zainh
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\zainh\Downloads\dataset.csv")
X = df[['Chiness','Bejing','Shanghai','Macao','Tokyo','Japan']]
Y = df['class']
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf = clf.fit(X, Y)

print(clf.predict([[3,0,0,0,1,1]]))