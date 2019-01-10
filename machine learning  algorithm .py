
# coding: utf-8

# In[41]:


#algorithms which perform best
#ensembles
from sklearn import model_selection 
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import sklearn.linear_model as skl_lm


# In[10]:


import os


# In[11]:


import os
print(os.getcwd())


# In[19]:


os . chdir('E:\\Datasets')


# In[22]:


data=pd.read_csv("Diabetes.csv")
data


# In[23]:


names = ['preg','plas','pres','skin','test','mass','pedi','age','class',]


# In[30]:


import pandas as pd


# In[32]:


data.head()


# In[33]:


array =data.values


# In[35]:


x = array[:,0:8]


# In[36]:


x = array[:8]


# In[38]:


seed =7


# In[53]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=101)


# In[51]:


cart = DecisionTreeClassifier


# num_trees =100
