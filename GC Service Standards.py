#!/usr/bin/env python
# coding: utf-8

# In[16]:


### Import package 
from urllib.request import urlretrieve


# In[ ]:





# In[17]:


# Import pandas
import pandas as pd


# In[18]:


# Assign url of file: url_std
url_std = 'https://open.canada.ca/data/dataset/3ac0d080-6149-499a-8b06-7ce5f00ec56c/resource/272143a7-533e-42a1-b72d-622116474a21/download/service_standards.csv'


# In[21]:


df_std = pd.read_csv(url_std)


# In[22]:


df_std.head()


# In[ ]:





# In[ ]:




