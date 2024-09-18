#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # PROBLEM 2
# In this problem, the concepts of subsetting, slicing, and indexing operations are further explored using the data frame of cars in Problem 1. The indexing function 'cars.iloc[]' will be used to display the first five rows with odd-numbered columns of cars. The slicing function 'cars[]' will be used to display the row that contained the 'Model'of 'Mazda RX4'. To then find the amount of cylinders in car model 'Camaro Z28', the function 'cars.loc' is used and will be conditioned to find what it needed. Lastly, the same function 'cars.loc' is used to find the 'cyl'and 'gear' of the following car models given. Moreover, it is important to take note that different techniques may be used to get the desired output which will also be demonstrated in some partsas as pd'.

# The first step is to tap in the Pandas library using 'import pandas as pd'.

# In[4]:


#accessing the Pandas library
import pandas as pd


# The 'cars' variable will be used to store the downloaded .csv file with file name 'cars.csv'. It will also be called in order to see the data contined in the file.

# In[7]:


#the varaible cars is used to store the .csv file
#the variable is also called
cars = pd.read_csv('cars.csv')
cars


# # a.
# 
# To find and display the first five rows with odd-numbered columns of cars, the function 'cars.iloc[]' was used. The 'cars' refers to the data frame being used while '.iloc[]' is for selsecting the rows and columns based by their index positions. For the indexing, ':5' selects the first five row starting from 0, while '::2' selects every second column which are the "odd-numbered" columns.

# In[10]:


#getting the first five rows with odd-numbered columns of cars
cars.iloc[:5, ::2]


# ALTERNATIVE WAY: In this alternate way, the same results are displayed; however, with the addition of using '.head'. The function 'cars.head(5)' simply selects the first 5 rows of the data frame again. The function '.iloc[:, ::2]' is to select the odd-numbered columns from the first 5 rows indicated.

# In[13]:


#different way to get the same result of getting the first five rows with odd-numbered columns of cars
cars.head(5).iloc[:, ::2]


# # b.
# 
# To display the row that contains the 'Model' of 'Mazda RX4', the slicing function 'cars[]' is used. The 'cars[]' indicate the data frame going to be used, while '[0:1]' means the range starts at index 0 and ends before index 1. 

# In[17]:


#displaying the row of the 'Model' of 'Mazda RX4' using a slicing function
cars[0:1]


# ALTERNATIVE WAY: Another way to to display the same results is to use the postional indexing function '.iloc[[]]'. Again, the 'cars' indicate the data frame being used. The function '.iloc[]' is then used to select the rows and columns by their position, while '[0]' returns the first row but it keeps it in the data frame format.

# In[20]:


#another way to display the row of the 'Model' of 'Mazda RX4' by using positional indexing
cars.iloc[[0]]


# # c.
# 
# To know how much cylinders ('cyl') the car model 'Camaro Z28' have, the function 'cars.loc' was used. The 'cars' is used to indicate the data frame to be used. The 'cars['Model'] == 'Camaro Z28' is a boolean series which indicates that the model should correspond to row 'Model' and column 'Camaro Z28'. Lastly, the 'cars.loc[condition, ['Model', 'cyl']] altogether selects the rows and columns by labels, specifies which rows to select based on the given condition, and it also specifies which columns to include in the result.

# In[23]:


#displays how many cylinders ('cyl') the car model 'Camaro Z28' have through indexing
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]


# # d.
# 
# To determine how many cylinders ('cyl') and what gear type ('gear') do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civicc' have, the function 'cars.loc' with specific conditions is used. The 'cars' specifies the data frame to be used. The 'cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']) wherein '.isin()' is a method that returns a boolean series, while ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'] is a list of the 'Model' column to be checked. Lastly, the 'cars.loc[condition, ['Model', 'cyl', 'gear'] specifies the columns needed.

# In[26]:


#displays how many cylinders ('cyl') and what gear type ('gear') do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic' have through indexing
cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]


# ALTERNATIVE WAY: For a more cleaner line of code and still achieve the same result, the Models 'Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic' are stored in variable 'models' which will be called instead.

# In[31]:


#the variable 'models' is used to store the specified car models and is put in the '.isin()' condition
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]


# In[ ]:




