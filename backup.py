# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 02:06:11 2022

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
        url = "https://pureportal.coventry.ac.uk/en/organisations/school-of-economics-finance-and-accounting"
        page = requests.get(url)
        print(page.text)

      #  r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(page.text,"html.parser")
        
        #publication_info = soup.find_all("div",{"class":'relation-list relation-list-publications'})
        authorinfor=soup.find("div",{"class":'relation-list relation-list-publications'}).find_all("a",{"rel":'Person'})
        print('--')
        print(authorinfor)
        publicationInfo= soup.find("div",{"class":'relation-list relation-list-publications'}).find_all("a",{"rel":'ContributionToJournal'})
        print(publicationInfo)
        date= soup.find("div",{"class":'relation-list relation-list-publications'}).find_all(True,{"class":"date"})
        Authors=soup.find_all("a", class_="link")
        print(date) 
       # print(Authors)
        #OtherAuthors=[]
        #for other_authors in Authors:
        #    print(other_authors)
        
# =============================================================================
#         for this_author in authorinfor:
#               print(this_author)
#               print("---")
#               print(this_author.string)
#               AuthorName=this_author.string
#               print("--")
#               if 'href' in this_author.attrs:
#                  link_author=this_author.attrs['href']
#                  print(this_author.attrs['href'])
#               print("---")
#         for this_publication in publicationInfo:
#             print(this_publication)
#             print("---")
#             title=this_publication.string
#             print(title)
#             print("---")
#             # title = this_publication.find("a",class_="link")
#             if 'href' in this_publication.attrs:
#                 link_publication=this_publication.attrs['href']
#                 print(this_publication.attrs['href'])
#              #
#             print("---")
#         for dt in date:
#               print(dt)
#               print(dt.string)
#               date_published= dt.string     
# =============================================================================
#=============================================================================
        
#=============================================================================
            
# =============================================================================
#         publication_info = soup.find_all("a",{"rel":'ContributionToJournal'})
#         #all_staff = soup.find_all(True,{"class": ["link","link person","date"]})
#         author_info = soup.find_all("a",{"rel":'Person'})
#         date_published=soup.find_all(True,{"class":"date"})
# =============================================================================

        
     ###Publication Information
# =============================================================================
#         for this_publication in publication_info:
#             print(this_publication)
#             print("---")
#             title=this_publication.string
#             print("---")
#            # title = this_publication.find("a",class_="link")
#             if 'href' in this_publication.attrs:
#                 link_publication=this_publication.attrs['href']
#                 print(this_publication.attrs['href'])
#             #
#             print("---")
# =============================================================================
            
     ##### Author Information
        
# =============================================================================
#         for this_author in author_info:
#               print(this_author)
#               print("---")
#               print(this_author.string)
#               AuthorName=this_author.string
#               print("--")
#               if 'href' in this_author.attrs:
#                  link_author=this_author.attrs['href']
#                  print(this_author.attrs['href'])
#               print("---")
# =============================================================================
          ### Date Published
# =============================================================================
#         for dt in date_published:
#              print(dt)
#              print(dt.string)
#              date= dt.string
# =============================================================================
            
            
            
            
            
            
            #links=this_staff.find("a",{"class":"link"}).get("href")
            #print(title)
           # print('---')
            #link_pub = this_staff.find("a",class_="link").text
            #link_auth= this_staff.find("a",class_="link person").text
          #  published = this_staff.find('pubDate').text
           # print(link)
            
        
        # select only the "items" I want from the data
        #articles = soup.findAll('item')

        # for each "item" I want, parse it into a list
        #for a in articles:
         #   title = this_staff.find('title').text
          #  link = this_staff.find('link').text
           # published = this_staff.find('pubDate').text

            # create an "article" object with the data
            # from each "item"
           # article = {
            #    'title': title,
             #   'link': link,
              #  'published': published
              #  }

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