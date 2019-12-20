import pandas as pd
df=pd.read_csv('cars.csv')
print df
by_comb=df.groupby("mpg")
print(by_comb.mean())
print(by_comb.std())
print(by_comb.min())
print(by_comb.max())
print(by_comb.count())
print(by_comb.describe())
print(by_comb.describe().transpose())
