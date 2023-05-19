# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:01:27 2022

@author: zainh
"""

import os
import string
import re
from nltk.stem import *
import nltk
import itertools
import math
import operator
import sys
from statistics import mean

import sys
sys.path.append("FINALFINAL")
import FINALFINAL as i
print(i.x)

def tokenize_and_remove_punctuations(s):
    translator = str.maketrans('','',string.punctuation)
    modified_string = s.translate(translator)
    modified_string = ''.join([i for i in modified_string if not i.isdigit()])
    return nltk.word_tokenize(modified_string)

def get_stopwords():
    stop_words = stopwordsfromnltk
    return stop_words

# def parse_data(contents):
#     contents = contents.lower()
#     title_start = contents.find('<title>')
#     title_end = contents.find('</title>')
#     title = contents[title_start+len('<title>'):title_end]
#     text_start = contents.find('<text>')
#     text_end = contents.find('</text>')
#     text = contents[text_start+len('<text>'):text_end]
#     return title+" "+text

def stem_words(tokens):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(token) for token in tokens]
    return stemmed_words

def remove_stop_words(tokens):
    stop_words = stopwords.words('english')
    filtered_words = [token for token in tokens if token not in stop_words and len(token) > 2]
    return filtered_words

# def read_data(path):
#     contents = []
#     for filename in os.listdir(path):
#         data = parse_data(open(path+'/'+filename,'r').read())
#         filename = re.sub('\D',"",filename)
#         contents.append((int(filename),data))
#    return contents

def calculate_tf(tokens):
    tf_score = {}
    for token in tokens:
        tf_score[token] = tokens.count(token)
    return tf_score

def get_vocabulary(data):
    tokens = []
    for token_list in data.values():
        tokens = tokens + token_list
    fdist = nltk.FreqDist(tokens)
    return list(fdist.keys())

def preprocess_data(contents):
    print('kkk')
    dataDict = {}
    count=0
    for content in contents:
        #print(content[1])
        tokens = tokenize_and_remove_punctuations(content)
        #print(tokens)
        filtered_tokens = remove_stop_words(tokens)
        stemmed_tokens = stem_words(filtered_tokens)
        #print(stemmed_tokens)
        filtered_tokens1 = remove_stop_words(stemmed_tokens)
        #print(filtered_tokens1)
        #print(content[0])
        dataDict[count] = filtered_tokens1
        count +=1
    return dataDict

def calculate_idf(data):
    idf_score = {}
    N = len(data)
    all_words = get_vocabulary(data)
    for word in all_words:
        word_count = 0
        for token_list in data.values():
            if word in token_list:
                word_count += 1
        idf_score[word] = math.log10(N/word_count)
    return idf_score

def calculate_tfidf(data, idf_score):
    scores = {}
    for key,value in data.items():
        scores[key] = calculate_tf(value)
    for doc,tf_scores in scores.items():
        for token, score in tf_scores.items():
            tf = score
            idf = idf_score[token]
            tf_scores[token] = tf * idf
    return scores

def preprocess_queries(path):
    queriesDict = {}
    queries = open(path,'r').read().split('\n')
    i = 1
    for query in queries:
        tokens = tokenize_and_remove_punctuations(query)
        filtered_tokens = remove_stop_words(tokens)
        stemmed_tokens = stem_words(filtered_tokens)
        filtered_tokens1 = remove_stop_words(stemmed_tokens)
        queriesDict[i] = filtered_tokens1
        i+=1
    return queriesDict

def calculate_tfidf_queries(queries, idf_score):
    scores = {}
    for key, value in queries.items():
        scores[key] = calculate_tf(value)
    for key, tf_scores in scores.items():
        for token, score in tf_scores.items():
            idf = 0
            tf = score
            if token in idf_score.keys():
                idf = idf_score[token]
            tf_scores[token] = tf * idf
    return scores

def generate_inverted_index(data):
    all_words = get_vocabulary(data)
    index = {}
    for word in all_words:
        for doc, tokens in data.items():
            if word in tokens :
                if word in index.keys():
                    index[word].append(doc)
                else:
                    index[word] = [doc]
    return index

def get_relevance(path):
    relevances = {}
    data = open(path,'r').read()
    for line in data.split('\n'):
        tokens = line.split(" ")
        if int(tokens[0]) in relevances.keys():
            relevances[int(tokens[0])].append(int(tokens[1]))
        else:
            relevances[int(tokens[0])] = [int(tokens[1])]
    return relevances

# def find_precision_recall(relevances, docList):
#     relevant_docs = len([doc for doc in docList if doc in relevances])
#     total_relevant = len(relevances)
#     total_docs = len(docList)
#     precision = relevant_docs/total_docs
#     recall = relevant_docs/total_relevant
#     return precision, recall

#main method
#args = sys.argv



