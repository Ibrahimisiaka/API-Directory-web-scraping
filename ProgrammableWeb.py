#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question: web scrape the API lists on this page, and export your result into a CSV file.

# https://www.programmableweb.com/category/all/apis
'''
Your Python code should scrape the following details from each table row:

• API Name

• API (absolute) URL

• API Category

• API Description
'''
# Your Python code should crawl to all the available "next" pages. Your final result should be approx. 20,400 rows


# In[22]:


# import the required packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.programmableweb.com/category/all/apis"  # url to be scraped.
url_2 = "https://www.programmableweb.com/"
master_list = []

try:
    while True:

        response = requests.get(url)
        print(response.status_code)
        soup = BeautifulSoup(response.text) # Pass the requested page in to a bs4 object

        table = soup.find('table', {'class':'views-table'})
        table_rows = table.tbody.find_all('tr')
        for row in table_rows:
            API_NAME = row.find('td', {'class':'views-field-pw-version-title'}).text.strip()
            API_URL = url_2 + row.find('td', {'class':'views-field-pw-version-title'}).a['href']
            API_CATEGORY = row.find('td', {'class':'views-field-field-article-primary-category'}).text.strip()
            API_DESCRIPTION = row.find('td', {'class':'views-field-field-api-description'}).text.strip()
            API_FOLLOWER = row.find('td', {'class':'views-field-flag-follow-api-count'}).text.strip()
            API_DICT = {}
            API_DICT['API_NAME'] = API_NAME
            API_DICT['API_URL'] = API_URL
            API_DICT['API_CATEGORY'] = API_CATEGORY
            API_DICT['API_DESCRIPTION'] = API_DESCRIPTION
            API_DICT['API_FOLLOWER'] = API_FOLLOWER
            master_list.append(API_DICT)
        NEXT_PAGE_URL = soup.find('a', {'title':'Go to next page'})['href']
        if NEXT_PAGE_URL:
            url = "https://www.programmableweb.com" + NEXT_PAGE_URL
            print(url)
    #     elif len(count) == 5:
    #         break
        else:
            break
except:
    print('failed!')
    
    
# Saving extracted data to csv
df = pd.DataFrame(master_list)
print(len(master_list))
df.to_csv('api.csv')


# In[ ]:





# In[ ]:




