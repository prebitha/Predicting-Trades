#!/usr/bin/env python
# coding: utf-8

# # CLUSTER CUSTOMER USING KMEANS ML MODEL 
# 

# Inorder to cluster the customer we will do k-means ML and then we can see more

# In[1]:


#import library
import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# for data preprocessing and clustering
from sklearn.cluster import KMeans


# In[2]:


# loading the dataset
trades=pd.read_csv("trades.csv")
print("The number of rows for trades.csv",trades.shape[0])


# ### UNDERSTANDING THE DATA

# In[3]:


trades[["date","time"]]=trades["execution_time"].str.split(' ',1,expand=True) #splitting the execution into data and time
pd.to_datetime(trades["date"]) #converting the type to DateTime format
trades['Month'] = pd.DatetimeIndex(trades['date']).month #making a new column with Month data


# In[4]:


trades= trades.drop(["Unnamed: 0", "execution_time"], axis=1) #we drop columns that are irrelvant


# In[5]:


# first glance of customers_trades data
trades.info()


# In[6]:


# descriptive statistics of the numerical columns
trades.describe()


# In[7]:


trades.isna().sum() #we can drop the null values


# ### DEFINING THE DATAFRAME
# Since Trade Republic makes its profits when the customer makes a trade so therefore the execution_size ( the number of trades made) will be the mark for clsutering

# In[8]:


# Grouping Customer based on the execution_size i.e the Number of Trades they made
df=trades.groupby(['direction','date','execution_price',"execution_size",'time'])["customer_id"].sum().reset_index()


# In[9]:


print("The Number of Customer is:", df.shape[0]) #871384 customer
df.head()


# ## UNSUPERVISED MACHINE LEARNING

# ### STEP 1 - DEFINING THE TRAINING DATA

# In[10]:


X=df[["execution_price",'execution_size']]


# ### STEP 2 - STANDARDISING THE DATA

# In[11]:


from sklearn.preprocessing import StandardScaler
X_prep = StandardScaler().fit_transform(X)
X_prep


# ### STEP 3 - BRINGING THE STANDARDISED DATA BACK INTO A DATAFRAME 

# In[12]:


X_prep_df = pd.DataFrame(X_prep, columns=["execution_price",'execution_size'])
X_prep_df 


# ### STEP 4 - MACHINE LEARNING MODEL

# In[13]:


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=8, random_state=1234)
kmeans.fit(X_prep_df)


# In[14]:


kmeans.cluster_centers_


# ### STEP 5 : FINDING THE INERTIAL FOR VALIDATING

# In[15]:


# total inertia of all the centroids
kmeans.inertia_


# In[20]:


# I want to iterate over a range of mx_iter and for every value, I want to return the inertia
def get_kmeans_ineratia_varying_max_iter(max_iter):
    kmeans = KMeans(n_clusters=5,
                    random_state=1234,
                    n_init=3,
                    algorithm='elkan',
                    max_iter=max_iter,
                   )
    kmeans.fit(X_prep_df)

    return kmeans.inertia_

max_iter_list = [1, 5, 10, 20, 30]

plt.plot(max_iter_list,
         [get_kmeans_ineratia_varying_max_iter(x) for x in max_iter_list],
        )
plt.xlabel('Max iter')
plt.ylabel('inertia')


# ### VALIDATION 
# 
# FROM THE PLOT ITS EVIDENT THAT 5 IS A GOOD NUMBER FOR CLUSTERS K

# ### STEP 6 : DEFINING THE NUMBER OF CLUSTER K= 5

# In[21]:


kmeans = KMeans(n_clusters=5,
             random_state=1234)

kmeans.fit(X_prep)

clusters = kmeans.predict(X_prep)
clusters


# In[22]:


clusters.shape


# ### STEP 7 - BRINGING THE CLUSTER INTO THE DATAFRAME

# In[23]:


trades_clustered = pd.DataFrame(X_df, columns=["execution_price",'execution_size'])
trades_clustered['cluster_id'] = clusters
trades_clustered[['customer_id','date','time','direction']]= df[['customer_id','date','time','direction']]


# In[39]:


trades_clustered.to_csv ('export_dataframe.csv', index = False, header=True)


# ### STEP 8 - VISUALISATION 

# In[24]:


import plotly.express as px
fig = px.scatter(trades_clustered, x="execution_price", y="execution_size", color="cluster_id")
fig.show()


# ## CONCLUSION:
# Its very evident that the cluster_id=1 are the ones who make more trades even though they put into less amout into the market
# Trade Republics ideal customers are the ones with cluster_id=1

# In[ ]:




