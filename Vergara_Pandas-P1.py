#accessing the Pandas library
import pandas as pd

#the varaible cars is used to store the .csv file
#the variable is also called
cars = pd.read_csv('cars.csv')
cars

#displaying the first five rows of the resulting cars
cars.head()

#displaying the first 8 rows of the resulting cars
cars.head(8)

#displaying the last five rows of the resulting cars
cars.tail()

#displaying the last 8 rows of the resulting cars
cars.tail(8)
