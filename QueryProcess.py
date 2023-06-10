# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:16:49 2022

@author: zainh
"""
import preprocandindexfuncs as func
import pickle
import math
import io
import operator
from azure.storage.blob import BlobServiceClient
import pickle

#Azure Blob Storage connection details
connection_string = "DefaultEndpointsProtocol=https;AccountName=searchenginestrg;AccountKey=LB3Y3pG2mzMkxYzE6M8fBHuspzJTOTR+NZlm3Dv29jSsAszGmY111rLntxYAsZR82p/Wh3y/jGZ2+AStWWThUQ==;EndpointSuffix=core.windows.net"
container_name = "searchenginepickle"
idfscores_blob_name = "idfscores.pickle"
scores_blob_name = "scores.pickle"
invertedindex_blob_name = "invertedindex.pickle"

#BlobServiceClient object using the connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

#Reference to the container
container_client = blob_service_client.get_container_client(container_name)




def QueryResults(search):
    
    #print(data)
    
    qr=search #Query from the web page
    #qr=r'C:\Users\zainh\Desktop\qquery.txt'
    query=func.query_preproces(qr)  # Preprocess the Query 
    
    idfscores_blob_client = blob_service_client.get_blob_client(container=container_name, blob=idfscores_blob_name)
    idfscores_data = idfscores_blob_client.download_blob().readall()
    # Create a file-like object from the pickled data
    idfscores_data_stream = io.BytesIO(idfscores_data)
    idf = pickle.load(idfscores_data_stream)
    
    scores_blob_client = blob_service_client.get_blob_client(container=container_name, blob=scores_blob_name)
    scores_data = scores_blob_client.download_blob().readall()

    # Create a file-like object from the pickled data for scores 
    scores_data_stream = io.BytesIO(scores_data)

    # Load the deserialized scores using pickle.load()
    scores = pickle.load(scores_data_stream)

    # Get the blob client and download the pickled data for inverted index
    invertedindex_blob_client = blob_service_client.get_blob_client(container=container_name, blob=invertedindex_blob_name)
    invertedindex_data = invertedindex_blob_client.download_blob().readall()

    # Create a file-like object from the pickled data for inverted index
    invertedindex_data_stream = io.BytesIO(invertedindex_data)

    # Load the deserialized inverted index using pickle.load()
    invertedindex = pickle.load(invertedindex_data_stream)
    
    #with open("idfscores.pickle", "rb") as file:
    #    idf = pickle.load(file)
        
    #with open("scores.pickle", "rb") as file:
    #    scores = pickle.load(file)
    
   # with open("invertedindex.pickle", "rb") as file:
    #    invertedindex = pickle.load(file)
       
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