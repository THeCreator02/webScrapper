# Created By: Sam Ramirez
# Created On: February 20, 2020

# installed dependencies
# pip install bs4
# pip install selenium
# pip install pandas
# pip install lxml

# timeit allows for tracking exe timing
#import timeit
#testCode="""

from bs4 import BeautifulSoup
from selenium import webdriver as wd

import pandas as pd
import os

path="/usr/local/bin/chromedriver" # path for chrome driver

driver=wd.Chrome(path) # setting driver 
pages=19 # number of pages we want to tranverse through
sources=[] # list of all the news org
titles=[] # list of the headlines of news articles
links=[] # list of the links of news articles
dates=[] # list of the date of publication
webpage='https://lostcoastoutpost.com/elsewhere/categories/humboldt-news/' 
# origin webpage
next = 1 #setting page destination, needed so we can ignore clicking on "next page"

while next<=pages: 
    # since the website uses numerical indexes for pages loop until number reached
    driver.get(webpage+str(next)+'/') # initialize driver to current webpage
    next+=1 # increase, can happen whenever, simply after so we dont lost track
    content=driver.page_source # get the contents of the webpage from driver
    soup=BeautifulSoup(content,features="lxml") 
    # parse the webpage into xml (maybe do html, maybe faster)
    a = soup.findAll('div', attrs={'class':'elsewhere-box'}) 
    #find all the divisors that have the class elsewhere-box (should simply be one)
    for p in a[0].findAll('p'): #find all paragraph elements in div class elsewhere-box
        i=1 # index for each content in paragraph
        for s in p.findAll('a'): # find all source links with attribute href
            if i%2: 
                if s.text=='Homepage': # ignore if paragraph has this text
                    break
                else:
                    sources.append(s.text) #grab text in <p> tag
            else:
                if s.text=='Elsewhere': # ignore if paragraph has this text
                    break
                else:
                    titles.append(s.text) #grab text in <a> tag
                    links.append(s['href']) # grab link and append to list
            i+=1
        if(p.find('u')==None): 
            date=p.find_previous('u')
            if date != None:
                date=str(date)
                date=date[3:-4]
                dates.append(date)
            else:
                continue
driver.close()# close driver now that data has been collected
df = pd.DataFrame({'Date':dates,'headline':titles,'publisher':sources,'link':links})
#add all list to a dataframe for analysis
df.to_csv('2020NewsStory.csv', index=False, encoding='utf-8')
#now save all dataframe data to a csv

#"""

#elapsed_time = timeit.timeit(testCode, number=10)/10
#print(elapsed_time)

