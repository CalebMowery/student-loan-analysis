#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd


# In[2]:


data = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools?&_fields=admissions.sat_scores.average.overall,school.name,repayment.repayment_cohort.3_year_declining_balance&per_page=100&page=40&api_key=4JJj7qqqCjEBcUklTsF6XI2X5ZK69KZAZ1P8QKjZ")
json_data=data.json()
json_data


# In[3]:


metadata = json_data["metadata"]
total = metadata["total"]
per_page = metadata["per_page"]
num_of_pages = total / per_page
num_of_pages


# In[4]:


merged2021_22 = pd.read_csv("data/MERGED2021_22_PP.csv",dtype="string",index_col = 0)
merged2021_22


# In[ ]:




