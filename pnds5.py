import pandas as pd
cars=pd.read_csv('cars.csv')
print cars
cars=pd.read_csv('cars.csv',index_col=0)
print(cars)
print(cars['mpg'])
print(cars[['mpg']])
print(cars[['mpg','hp']])
print(cars.iloc[2])
print(cars.loc[['Duster 360','valient'],['mpg','cyl','disp']])
