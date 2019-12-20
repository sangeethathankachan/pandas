import pandas as pd
s=pd.Series([3,-5,7,4],index=['a','b','c','d'])
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
df=pd.DataFrame(dict,
columns=['country','capital','area','population'])

#import pandas as pd
bric=pd.DataFrame(dict)
print bric
bric.index=["BR","RU","IN","CH","SA"]
print bric
s=s.drop(['a','b'])
print s
df=df.drop('country',axis=1)
print(df)
