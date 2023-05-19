# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:32:57 2022

@author: zainh
"""

# this is only sample basic code to start with to implement a very simple crawler for the purpose of the labsheet

import requests
from bs4 import BeautifulSoup

def mycrawler(seed, maxcount):
	Q = [seed] #this is the queue which initially contains the given seed URL
	count = 0
	while(Q!=[] and count < maxcount):
		count +=1
		url = Q.pop(0)
		print("fetching " + url)

		code = requests.get(url)
		plain = code.text
		s = BeautifulSoup(plain, "html.parser")
		for link in s.findAll('a'):
			new_url = link.get('href')
			if(new_url != None and new_url != '/'):
				new_url = new_url.strip()
				#print("new_url is : ", new_url)

				#normalise if needed
				if( new_url[0:7] != 'http://' and new_url[0:8]!='https://' ) :
					if(url[len(url) -1] == '/'):
						new_url = url + new_url 
					else:
						new_url = url + '/' + new_url 
                                #NOTE : further normalization code required here
				#print("new_url is : ", new_url)  #uncomment the print statement to see the urls

				Q.append(new_url)


mycrawler('https://scholar.google.com',10) #use any number, instead of 10, to control the number of pages crawled