# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:02:39 2022

@author: zainh
"""

import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files

# save function
def save_function(article_list):
    with open('scrappedresults.txt', 'w') as outfile:
        json.dump(article_list, outfile)

# scraping function
def hackernews_rss():
    """Web Scrapping"""
    pub_list = []

    try:
        # execute my request, parse the data using XML
        # parser in BS4
        url = "https://pureportal.coventry.ac.uk/en/organisations/school-of-economics-finance-and-accounting/publications/"
        page = requests.get(url)
        print(page.text)

      #  r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(page.text,"html.parser")
        
        #publication_info = soup.find_all("div",{"class":'relation-list relation-list-publications'})
        #authorinfor=soup.find("div",{"class":'relation-list relation-list-publications'}).find_all("a",{"rel":'Person'})
        #print(authorinfor)
        #publicationInfo= soup.find("div",{"class":'relation-list relation-list-publications'}).find_all("a",{"rel":'ContributionToJournal'})
        #print(publicationInfo)
        #date= soup.find("div",{"class":'relation-list relation-list-publications'}).find_all(True,{"class":"date"})
        #print(date) 
        Info=soup.find_all("a",{"rel":'ContributionToJournal'})
        print(Info)

# =============================================================================
#         paper = {
#               'Title': title,
#               'PublicationLink':link_publication,
#               'AuthorName': AuthorName,
#               'AuthorProfile': link_author,
#               'DatePublished':date_published
#               }
#         print(json.dumps(paper,indent=2))
# =============================================================================
#=============================================================================

            # append my "article_list" with each "article" object
            #pub_list.append(article)
        
        # after the loop, dump my saved objects into a .txt file
       # return save_function(pub_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

print('Starting scraping')
hackernews_rss()
print('Finished scraping')