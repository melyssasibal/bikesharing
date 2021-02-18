#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# 1. Create a DataFrame for the 201908-citibike-tripdata data. 
citibike_df = pd.read_csv("201908-citibike-tripdata.csv")
citibike_df


# In[3]:


# 2. Check the datatypes of your columns. 
citibike_df.dtypes


# In[4]:


# 3. Convert the 'tripduration' column to datetime datatype.
citibike_df['tripduration'] = pd.to_datetime(citibike_df['tripduration'], unit='s')


# In[5]:


# 4. Check the datatypes of your columns. 
citibike_df.dtypes


# In[6]:


citibike_df.head()


# In[8]:


# 5. Export the Dataframe as a new CSV file without the index.
citibike_df.to_csv("citibike_data.csv", index=False)


# In[ ]:




