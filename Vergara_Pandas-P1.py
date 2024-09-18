#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 1
# 
# In this problem, the corresponding .csv file with file name "cars.csv", is loaded to a data framed using Pandas. The function 'pd.read_csv()' will be used to load the file. Moreover, this problem aims to display the first five and last five rows of the resulting cars. It can be done by using the functions '.head()'and '.tail'.

# The first step is to tap in the Pandas library using 'import pandas as pd'.

# In[7]:


#accessing the Pandas library
import pandas as pd


# The 'cars' variable will be used to store the downloaded .csv file with file name 'cars.csv'. It will also be called in order to see the data contined in the file.

# In[10]:


#the varaible cars is used to store the .csv file
#the variable is also called
cars = pd.read_csv('cars.csv')
cars


# In order to display the fist five rows of the resulting cars, the function 'cars.head()' will be used. There are no arguments inside the parenthesis as using this returns the first 5 rows automatically.

# In[13]:


#displaying the first five rows of the resulting cars
cars.head()


# SIDENOTE: You may specifiy the number of rows from the start you want to display by idicating it inside the parenthesis as follows:

# In[21]:


#displaying the first 8 rows of the resulting cars
cars.head(8)


# To display the last five rows of the resulting cars, the function 'cars.tail()' will be used. There are no arguments inside the parenthesis as using this returns the last 5 rows automatically.

# In[16]:


#displaying the last five rows of the resulting cars
cars.tail()


# SIDENOTE: You may specifiy the number of rows from the end you want to display by idicating it inside the parenthesis as follows:

# In[25]:


#displaying the last 8 rows of the resulting cars
cars.tail(8)


# In[ ]:




