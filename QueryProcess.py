# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:16:49 2022

@author: zainh
"""
import preprocandindexfuncs as func
import pickle
import math
import operator


def QueryResults(search):
    
    
    #print(data)
    qr=search
    #qr=r'C:\Users\zainh\Desktop\qquery.txt'
    query=func.query_preproces(qr)
    with open("idfscores.pickle", "rb") as file:
        idf = pickle.load(file)
        
    with open("scores.pickle", "rb") as file:
        scores = pickle.load(file)
    
    with open("invertedindex.pickle", "rb") as file:
        invertedindex = pickle.load(file)
       
    query_scores=func.tfidfCalculatorQuery(query,idf)
    query_docs = {}
    for key, value in query.items():
        doc_sim = {}
        for term in value:
            if term in invertedindex.keys():
                docs = invertedindex[term]
                print(docs)
                for doc in docs:
                    doc_score = scores[doc][term]
                    doc_length = math.sqrt(sum(x ** 2 for x in scores[doc].values()))
                    query_score = query_scores[key][term]
                    query_length = math.sqrt(sum(x ** 2 for x in query_scores[key].values()))
                    #Cosine Similrity Calculated
                    cosine_sim = (doc_score * query_score) / (doc_length * query_length)
                    if doc in doc_sim.keys():
                        doc_sim[doc] += cosine_sim
                    else:
                        doc_sim[doc] = cosine_sim
        ranked = sorted(doc_sim.items(), key=operator.itemgetter(1), reverse=True)
        query_docs[key] = ranked
    for i in range(1, len(query_docs) + 1):
        docs = query_docs[i][:100]
        doc_list = [x[0] for x in docs]
        print("Query: " + str(i))
    return doc_list