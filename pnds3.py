import pandas as pd
s1=pd.Series([1,2,3,4,5,6,7])
s2=pd.Series([1.1,2.3,4.5,6.7,3.2,4.1])
s3=pd.Series(['a','b','c','d','e'])

data={'first':s1,'second':s2,'third':s3}
df=pd.DataFrame(data)
print df
