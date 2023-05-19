# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:32:22 2022

@author: zainh
"""

import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
#import json # exporting to files

# save function
#def save_function(article_list):
#    with open(r"C:\Users\zainh\Downloads\sportarticles.txt", 'w') as outfile:
#        json.dump(article_list, outfile)
def save_function(article_list):
    with open(r"D:\masters\information\cnnhealth.txt", 'w') as f:
        for a in article_list:
            f.write(a+'\n')
        f.close()
# scraping function
def hackernews_rss():
    article_list = []

    try:
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://rss.nytimes.com/services/xml/rss/nyt/Health.xml')
        soup = BeautifulSoup(r.content, features='xml')

        # select only the "items" I want from the data
        articles = soup.findAll('item')
        
        # for each "item" I want, parse it into a list
        for a in articles:
            description = a.find('description').text
         #   link = a.find('link').text
          #  published = a.find('pubDate').text

            # create an "article" object with the data
            # from each "item"
           # article = {
            #    'description': description,
               # 'link': link,
               # 'published': published
             #   }

            # append my "article_list" with each "article" object
            article_list.append(description)
        
        # after the loop, dump my saved objects into a .txt file
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

print('Starting scraping')
hackernews_rss()
print('Finished scraping')