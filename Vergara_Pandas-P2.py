#accessing the Pandas library
import pandas as pd

#the varaible cars is used to store the .csv file
#the variable is also called
cars = pd.read_csv('cars.csv')
cars

#getting the first five rows with odd-numbered columns of cars
cars.iloc[:5, ::2]

#different way to get the same result of getting the first five rows with odd-numbered columns of cars
cars.head(5).iloc[:, ::2]

#displaying the row of the 'Model' of 'Mazda RX4' using a slicing function
cars[0:1]

#another way to display the row of the 'Model' of 'Mazda RX4' by using positional indexing
cars.iloc[[0]]

#displays how many cylinders ('cyl') the car model 'Camaro Z28' have through indexing
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]

#displays how many cylinders ('cyl') and what gear type ('gear') do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic' have through indexing
cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]

#the variable 'models' is used to store the specified car models and is put in the '.isin()' condition
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]