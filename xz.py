# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:17:45 2022

@author: zainh
"""
#import numpy as np  
#def function_accuracy(tp,tn,fp,fn):
#    matrix= np.array([tp,fn],[fp,tn])
#    Precision= matrix[0][0]/(matrix[0][0]+matrix[0][1])
#    print(Precision)
#    Recall= matrix[0][0]/(matrix[0][0]+matrix[1][0])
#    print(Recall)
#    accuracy= (matrix[0][0]+matrix[1][1])/(matrix[0][0]+matrix[0][1]+matrix[1][0]+matrix[1][1])
#    print(accuracy)
  
#matrix= np.array([[1,2],[3,4]])
#print(matrix)
##########
TP = int(input("Please enter number of true positives: "))
TN = int(input("Please enter number of true negatives: "))
FP = int(input("Please enter number of false positives: "))
FN = int(input("Please enter number of false negatives: "))
         
if(TP+FP == 0):
    print("Precision is undefined.")
else:
    Precision = TP / (TP + FP)
    print("Precision = ", Precision, " ( " + str(Precision*100) + "% )")

if(TP+FN == 0):
    print("Recall is undefined.")
else:
    Recall = TP / (TP + FN)
    print("Recall = ", Recall, " ( " + str(Recall*100) + "% )")
    
Accuracy  = (TP + TN) / (TP + FP + FN + TN)
print("Accuracy = ", Accuracy, " ( " + str(Accuracy*100) + "% )")
