
# Scrapper
import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files
import pandas as pd
import preprocandindexfuncs 
import pickle
.
# save function
def save_function(article_list):
    """Data Saved in Json"""
    with open(r'C:\VerticalSearch-Engine\PublicationData.txt', 'w') as outfile:
        json.dump(article_list, outfile)

def get_authors_list(publication_url):
    """Author List Scrapped from Publication Pages"""
    try:
        page = requests.get(publication_url)
        Soupobj2 = BeautifulSoup(page.text,"html.parser")
        authorlist=Soupobj2.find_all("p",{"class":'relations persons'})
        print(authorlist)
#=============================================================================
        for authors in authorlist:
            print('--')
            #print(authors)
            print('--')
            authorlist=authors.text
            #print(authorlist)
            try:
                authorlink=authors.find('a',{"class":'link person'})['href'] 
                covuniauthor=authors.find('a',{"class":'link person'}).text
            except:
                authorlink=''
                covuniauthor=''
                
                
            return covuniauthor, authorlink, authorlist
#=============================================================================
    except Exception as e:
        print('The scraping job failed in Author List')
        print(e)    
        
 
# scraping function
def webcrawler():
    """Web Crawler"""
  #  pub_list = []
    Datalist=[] 
    
    try:
        pgurl = "https://pureportal.coventry.ac.uk/en/organisations/school-of-economics-finance-and-accounting/publications/?page="
        #looping over the site
        
        for pagenum in range(0,13):
          url=pgurl +str(pagenum)
          print(url)
          page = requests.get(url)
          #print(page.text)
          soup = BeautifulSoup(page.text,"html.parser")
          publicationInfo= soup.find_all("a",{"rel":['ContributionToJournal','WorkingPaper','ContributionToBookAnthology','ContributionToConference','BookAnthology','OtherContribution','Thesis','ContributionToPeriodical']})

          date= soup.find_all(True,{"class":"date"})
#=============================================================================
          #Looping over each Publication
          for index in range(0, len (publicationInfo)):
            
            covuniauthor, authorlink, authorlist = get_authors_list(publicationInfo[index]['href'])  
            paper = {
              'Title':publicationInfo[index].string,
              'PublicationLink':publicationInfo[index]['href'],
              'AuthorName': covuniauthor,
              'AuthorProfile': authorlink,
              'DatePublished':date[index].string,
              'AuthorList': authorlist
              }
            print(json.dumps(paper,indent=2))
            Datalist.append(paper)
            #print(Datalist)
            #dumping data in json format for later use
            
        df=pd.DataFrame(Datalist)
        save_function(Datalist)
        #print(json.dumps(paper,indent=2))
        return df,Datalist

    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)
        
        
def file_saving(df):
    """Inverted Index, Inverse Document Frequency and Tf -Idfs Saved"""
    data=df['Title']+df["AuthorList"]+df["DatePublished"]
    preprocessed_data = preprocandindexfuncs.preprocess_data(data.tolist())
    inverted_index = preprocandindexfuncs.InvertedIndex(preprocessed_data)
    
    with open("invertedindex.pickle", "wb") as file:
        pickle.dump(inverted_index, file, pickle.HIGHEST_PROTOCOL)
    idf_scores = preprocandindexfuncs.idfCalculator(preprocessed_data)
    with open("idfscores.pickle", "wb") as file:
        pickle.dump(idf_scores, file, pickle.HIGHEST_PROTOCOL)
    scores = preprocandindexfuncs.tfidfCalculatorData(preprocessed_data,idf_scores)
    with open("scores.pickle", "wb") as file:
        pickle.dump(scores, file, pickle.HIGHEST_PROTOCOL)

print('Starting scraping')
df,Datalist=webcrawler()
print('Finished scraping')
#print(df.head())
print('File Saving ')
file_saving(df)
print("File Saved")












#=============================================================================
# =============================================================================
# with open("Datalist.pickle", "wb") as file:
#     pickle.dump(Datalist,file, pickle.HIGHEST_PROTOCOL)
#     with open("file.txt", "w") as f:
# for s in score:
#         f.write(str(s) +"\n")
# =============================================================================
   

#=============================================================================

