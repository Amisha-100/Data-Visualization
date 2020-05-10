#!/usr/bin/env python
# coding: utf-8

# ## About dataset ##
# 
# The dataset is on the job outcomes of students who graduated from college between 2010 and 2012. The original data on job outcomes was released by American Community Survey, which conducts surveys and aggregates the data.
# 
# Download Dataset: [Recent Grads](https://github.com/fivethirtyeight/data/blob/master/college-majors/recent-grads.csv)
# 
# Each row in the dataset represents a different major in college and contains information on gender diversity, employment rates, median salaries, and more. Here are some of the columns in the dataset:
# 
# - Rank - Rank by median earnings (the dataset is ordered by this column).
# - Major_code - Major code.
# - Major - Major description.
# - Major_category - Category of major.
# - Total - Total number of people with major.
# - Sample_size - Sample size (unweighted) of full-time.
# - Men - Male graduates.
# - Women - Female graduates.
# - ShareWomen - Women as share of total.
# - Employed - Number employed.
# - Median - Median salary of full-time, year-round workers.
# - Low_wage_jobs - Number in low-wage service jobs.
# - Full_time - Number employed 35 hours or more.
# - Part_time - Number employed less than 35 hours.

# ## Data Visualization##
# Using visualizations, we can start to explore questions from the dataset like:
# 
# - Do students in more popular majors make more money?
#      Using scatter plots
# - How many majors are predominantly male? Predominantly female?
#      Using histograms
# - Which category of majors have the most students?
#      Using bar plots

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

recent_grads = pd.read_csv('recent-grads.csv')
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())
recent_grads = recent_grads.dropna()


# ## Pandas, Scatter Plots##

# In[2]:


recent_grads.plot(x="Sample_size", y="Median", kind="scatter")


# In[3]:


recent_grads.plot(x="Sample_size", y="Unemployment_rate", kind="scatter")


# In[4]:


recent_grads.plot(x="Full_time", y="Median", kind="scatter")


# In[5]:


recent_grads.plot(x="ShareWomen", y="Unemployment_rate", kind="scatter")


# In[6]:


recent_grads.plot(x="Men", y="Median", kind="scatter")


# In[7]:


recent_grads.plot(x="Women", y="Median", kind="scatter")


# ## Pandas, Histograms##

# In[8]:


recent_grads['Sample_size'].plot(kind='hist')


# In[9]:


recent_grads['Median'].plot(kind='hist')


# In[10]:


recent_grads['Employed'].plot(kind='hist')


# In[11]:


recent_grads['Full_time'].plot(kind='hist')


# In[12]:


recent_grads['ShareWomen'].plot(kind='hist')


# In[13]:


recent_grads['Unemployment_rate'].plot(kind='hist')


# In[14]:


recent_grads['Men'].plot(kind='hist')


# In[15]:


recent_grads['Women'].plot(kind='hist')


# **This is tedious to do every time for column. We can do it in a better way:**

# In[16]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(1,5):
    ax = fig.add_subplot(4,1,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# In[17]:


cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(4,8):
    ax = fig.add_subplot(4,1,r-3)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# ## Pandas, Scatter Matrix Plot##

# In[18]:


from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(6,6))
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# ## Pandas, Bar Plots##

# In[25]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)


# In[28]:


recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', legend=False)
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate', legend=False)

