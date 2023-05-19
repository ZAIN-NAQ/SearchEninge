# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 01:43:50 2022

@author: zainh
"""
import pickle
with open("invertedindex.pickle", "rb") as file:
    invertedindex = pickle.load(file)
print(invertedindex)