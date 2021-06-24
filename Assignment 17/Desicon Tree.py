#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.read_csv("dtdata.csv")
df


# In[30]:


X = df.iloc[:,:-1]
Y = df.iloc[:,4]


# In[31]:


X


# In[32]:


Y


# In[34]:


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()


# In[40]:


X=X.apply(encoder.fit_transform)
X


# In[41]:


Y = encoder.fit_transform(Y)


# In[42]:


Y


# In[46]:


from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X.iloc[:,1:5],Y)


# In[48]:


Y_ans =  model.predict(X.iloc[:,1:5])
Y_ans


# In[49]:


model.predict([[0,0,0,0]])


# In[ ]:




