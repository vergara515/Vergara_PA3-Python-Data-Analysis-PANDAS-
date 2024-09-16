# Vergara_PA3-Python-Data-Analysis-PANDAS-

This respiratory contains Python codes using PANDAS for the given programming problems. Furthermore, solutions, explanations, and testings for each problem are written here.

# PROBLEM 1

Problem 1 involves loading a .csv file into a data frame by using PANDAS. The function 'pd.read_csv()' is used to read and load the downloaded .csv file. Additionally, the first and last five rows of the resulting cars is to be displayed by using the functions '.head()' and '.tail()' respectively. Lastly, experiments of the codes to further explore the functions are tested.

_Functions used and their descriptions:_

1. **'import pandas as pd'** - This function is used to access the Pandas library.

2. **'cars'** - A variable wherein the .csv file will be stored.

3. **'pd.read_csv('cars.csv)'** - This function is used to read and load the file 'cars.csv'.

4. **'cars.head()'** - This function automatically displays the first five rows of the resulting cars from the file 'cars.csv'.

5. **'cars.tail()** - This functions automatically the last five rows of the resulting cars from the file 'cars. csv'.

_Further exploration of the functions tested in Problem 1:_

6. **'cars.head(8)'** - This function is the same as 'cars.head()'; however, the number of rows starting from the first index can be specified by indicating the value inside the parenthesis. In this case, the indicated is 8, thus the first 8 rows of the resulting cars would be displayed.

7. **'cars.tail(8)'** - This function is the same as 'cars.tail()'; however, the number of rows starting from the last index can be specified by indicating the value inside the parenthesis. In this case, the indicated is 8, thus the last 8 rows of the resulting cars would be displayed.

In conclusion from the tests done, not indicating the value inside the parenthesis of '.head()' and '.tail()' will automatically display the five rows, whether it be from the start or from the end. On the other hand, it will display the number of rows depending on the value inserted in the parenthesis. The index position of where it will start will depend whether '.head()' or '.tail()' is used.

# PROBLEM 2

Problem 2 explores the concepts of subsetting, slicing, and indexing operations using the data frames loaded from 'cars.csv'. Functions such as 'cars.iloc[]', 'cars[]', and 'cars.loc[]' which contains conditions for some given problems are used to find what is needed to be determined. Moreover, different techniques or opeartions may be used to get the desired output which is demonstrated.

_General Functions used and their descriptions:_

1. **'import pandas as pd'** - This function is used to access the Pandas library.

2. **'cars'** - A variable wherein the .csv file will be stored.

3. **'pd.read_csv('cars.csv)'** - This function is used to read and load the file 'cars.csv'.

_Functions used and their descriptions for Part **a** wherein the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars is to be displayed:_

4. **'cars.iloc[:5, ::2]'** - This function is used to display the first five rows with odd-numbered columns of cars. It also selects the first five row starting from 0 due to the indicated ':5'. To then get the odd-numbered columns, '::2' is used at it selects every second column.

5. **'cars.head(5).iloc[:, ::2]'** - This function is an alternative way to get the same result. In this case, using '.head(5)' simply just means it is selecting the first 5 rows of the data frame while the '.iloc[:, ::2]' still functions the same of selecting every second column.

_Functions used and their descriptions for Part **b** wherein the row that contains the ‘Model’ of ‘Mazda RX4’ is displayed:_

6. **'cars[0:1]'** - This function indicates the data frame going to be used is the .csv file stored in variable car as indicated by 'cars[]'. Moreover, the index means the range starts at index 0 and ends before index 1 which will result to the desired output.

7. **'cars.iloc[[0]]'** - This function is an alternate way to display the same result but by using poistional indexing. The '.iloc[]' selects the rows and columns while '[0]' returns the first row but still keeps it in the data frame format.

_Functions used and their descriptions for Part **c** wherein the amount of cylinders (‘cyl’) of the car model ‘Camaro Z28’ is asked:_

8. **'cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]'** - The function uses a boolean series and indexing as conditions were specified to get the output. The expression cars['Model'] == 'Camaro Z28' checks whether the 'Model' column in the data frame contains the value 'Camaro Z28' for each row. On the other hand, the `cars.loc[condition, ['Model', 'cyl']] selects rows and columns based on labels. It uses the provided condition to determine which rows to select and specifies the 'Model' and 'cyl' columns to be included in the output.

_Functions used and their descriptions for Part **d** wherein the amount of cylinders (‘cyl’) and gear type (‘gear’) on the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ is determined:_

9. 'cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]' - This function uses '.isin()' which returns a boolean series while the modeals inside the parenthesis is the list of 'Model' to be checked. Meanwhile, the 'cars.loc[condition, ['Model', 'cyl', 'gear'] specifies the columns needed to be returned.

_Functions for an alternative way of getting same results as Part d, but with a cleaner line of codes:_

10. **'models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']'** - A variable 'models' is used to store the list of 'Models'.

11. **'cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]'** - The variable 'models' is inserted in the '.isin()'

In conclusion, there are many alternate ways to get the desired output of the given problems by the use of subsetting, slicing, and indexing.
