#!/usr/bin/env python
# coding: utf-8

# In[2]:


#install BeautifulSoup
pip install beautifulsoup4


# In[3]:


#install requests
pip install requests


# In[4]:


#install lxml
pip install lxml


# In[11]:


#Import BeautifulSoup and requests
from bs4 import BeautifulSoup
import requests

#access the user agent and url from the web page
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
url='https://www.reddit.com/r/nature'
response=requests.get(url, {'headers':headers})

soup=BeautifulSoup(response.text,'html.parser')
#print(soup.prettify)
#utilized the prettify function to view page, but commented it out for space purposes. Too long.


# In[12]:


#select and print the first 7 posts on the web page
for item in soup.select('.Post')[:7]:
    try:
        print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #print title
        print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #print likes
        print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #print comments
        print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href']) #access specific post url
        print('----------------------------------------')
    except Exception as e:
        print('')


# In[ ]:




