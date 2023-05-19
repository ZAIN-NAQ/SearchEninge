# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:24:19 2022

@author: zainh
"""
# Scrapper
import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files

# save function
def save_function(article_list):
    with open('scrappedresults.txt', 'w') as outfile:
        json.dump(article_list, outfile)

def get_authors_list(publication_url):
    try:
        page = requests.get(publication_url)
        #print(page.text)
        #  r = requests.get('https://news.ycombinator.com/rss')
        Soupobj2 = BeautifulSoup(page.text,"html.parser")
        authorlist=Soupobj2.find_all("p",{"class":'relations persons'})
        #print(authorlist)
#=============================================================================
        for authors in authorlist:
            print('--')
            #print(authors)
            #print(authors.text)
            return authors.text 
#=============================================================================
    except Exception as e:
        print('The scraping job failed in Author List')
        print(e)    
        
 
# scraping function
def hackernews_rss():
    """Web Scrapping"""
  #  pub_list = []
     
    try:
        # execute my request, parse the data using XML
        # parser in BS4
        #looping over the site
        pgurl = "https://pureportal.coventry.ac.uk/en/organisations/school-of-economics-finance-and-accounting/publications/?page="
        #looping over the site
        for pagenum in range(0,1):
          url=pgurl +str(pagenum)
          print(url)
          page = requests.get(url)
          #print(page.text)

      #  r = requests.get('https://news.ycombinator.com/rss')
          soup = BeautifulSoup(page.text,"html.parser")
        
          #publication_info = soup.find_all("div",{"class":'relation-list relation-list-publications'})
          authorinfor=soup.find_all("a",{"rel":'Person'})
          print('authorinfor')
          print(authorinfor)
          publicationInfo= soup.find_all("a",{"rel":'ContributionToJournal'})
          print('publicationInfo')
          print(publicationInfo)
          date= soup.find_all(True,{"class":"date"})
          print('date')
          print(date)   
          #print(publicationInfo)
#=============================================================================
          #Looping over each Publication
          for index in range(0, len (publicationInfo)):
            #authorslist=[]
           # authorslist=get_authors_list(publicationInfo[index]['href'])  
            paper = {
              'Title':publicationInfo[index].string,
              'PublicationLink':publicationInfo[index]['href'],
              'AuthorName': authorinfor[index].string,
              'AuthorProfile': authorinfor[index]['href'],
              'DatePublished':date[index].string,
            #  'AuthorList': authorslist
              }
            #dumping data in json format for later use
            print(json.dumps(paper,indent=2))
        #print(json.dumps(paper,indent=2))

    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

print('Starting scraping')
#publicationurl='https://pureportal.coventry.ac.uk/en/publications/a-bibliometric-review-of-the-waqf-literature'
#get_authors_list(publicationurl)
hackernews_rss()
print('Finished scraping')