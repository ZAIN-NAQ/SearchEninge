# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:26:38 2022

@author: zainh
"""

import feedparser
NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
entry = NewsFeed.entries[1]

for entry in NewsFeed.entries:
    print(entry.title)
    print(entry.link)
    print("--------------------------------------")
