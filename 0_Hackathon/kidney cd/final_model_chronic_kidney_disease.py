#!/usr/bin/env python
# coding: utf-8

# In[150]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score , train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# In[151]:


data=pd.read_csv('kidney_disease.csv')


# In[152]:


data.head()


# In[153]:


data.columns


# In[154]:


data.info()


# In[155]:


data.describe()


# In[156]:


numericalColumns = ['age','bp','al','su','bgr','bu','sc','sod','pot','hemo']
categoricalColumns = ['rbc','sg','pc','pcc','ba','pcv','wc','rc','htn','dm','cad','appet','pe','ane']


# In[157]:


for columnName in data.columns:
    sns.histplot(data[columnName])
    plt.title(columnName)
    plt.show()


# #Missing Data

# In[158]:


data.isnull().sum()


# In[159]:


data['classification'].replace("ckd\t","ckd",inplace= True)

data['dm'].replace(["\tno","\tyes","yes"],["no","yes","yes"],inplace= True)

data['cad'].replace(["\tno"],["no"],inplace= True)


# In[160]:


data['rc'].replace("\t?",np.nan, inplace=True)

data.wc.replace("\t?",np.nan, inplace=True)

data['pcv'].replace(["\t?","\t43"],np.nan, inplace=True)


# In[161]:


for columnName in categoricalColumns:
    data[columnName].fillna(data[columnName].mode()[0],inplace=True)


# In[162]:


for columnName in numericalColumns:
    data[columnName].fillna(data[columnName].mean(), inplace= True)


# In[163]:


data.isnull().sum()


# #Dummy encode

# In[164]:


encodeColumn= ['rbc','pc' ,'pcc' ,'ba' ,'htn' ,'dm' ,'cad' ,'appet' ,'pe' ,'ane']

data = pd.get_dummies(data , columns=encodeColumn , prefix=encodeColumn , drop_first=True)


# In[165]:


data['classification'].replace(["ckd","notckd"],[1,0],inplace= True)


# In[166]:


data.head()


# In[167]:


data.classification.value_counts()


# #Min Max

# In[168]:


X = data.loc[:,data.columns!='classification']

Y= data['classification']


# In[169]:


min_max= MinMaxScaler()
min_max.fit(X)
X=min_max.transform(X)


# #Train Test Split 

# In[170]:


X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.20,random_state=42)


# In[171]:


log = LogisticRegression()
cv_v = cross_val_score(log, X_train, Y_train, cv=4)
print(cv_v)
print(cv_v.std())
print(cv_v.mean())


# In[172]:


log.fit(X_train,Y_train)


# In[173]:


y_pred = log.predict(X_test)
print(classification_report(Y_test,y_pred))


# In[ ]:




