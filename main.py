# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 00:31:58 2022

@author: zainh
"""

from flask import Flask ,request,render_template
import QueryProcess as  q
import ast
data = []
with open("PublicationData.txt", "r") as inFile:
    data = ast.literal_eval(inFile.read())
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
