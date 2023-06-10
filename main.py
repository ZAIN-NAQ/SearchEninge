# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 00:31:58 2022

@author: zainh
"""
from azure.storage.blob import BlobServiceClient
from flask import Flask ,request,render_template
import QueryProcess as  q
import ast
data = []

# Create a connection to your Azure Blob storage account
blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=searchenginestrg;AccountKey=LB3Y3pG2mzMkxYzE6M8fBHuspzJTOTR+NZlm3Dv29jSsAszGmY111rLntxYAsZR82p/Wh3y/jGZ2+AStWWThUQ==;EndpointSuffix=core.windows.net")

# Specify the container name
container_name = "searchenginepickle"

# Specify the blob name
blob_name = "PublicationData.txt"

# Get the blob client
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob content as text
blob_content = blob_client.download_blob().readall().decode("utf-8")

# Convert the content to Python objects
data = ast.literal_eval(blob_content)

#with open("PublicationData.txt", "r") as inFile:
#    data = ast.literal_eval(inFile.read())
app =Flask(__name__)
@app.route('/',methods=["GET","POST"])
def searchpage():

    if request.method == 'POST':
        query = request.form["msg"]
        res=q.QueryResults(query)
        results=[]
        for x in res:
            print(results.append(data[x]))
        return render_template('search1.html',foobar=results)
    else:
        res=0
        return render_template('index1.html',foobar=res)
        
if __name__=="__main__":
    app.run(debug=True)
    
#https://grantaguinaldo.com/rendering-variables-python-flask/
