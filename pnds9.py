import pandas as pd
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
  
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1,"\n\n",df2)
res=pd.merge(df1,df2,on='key')
print res

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
  					 'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result=pd.merge(left,right,on=['key1','key2'])
print(result)

res=pd.merge(left,right,how='left',on=['key2','key1'])

print(res)

res1=pd.merge(left,right,how='right',on=['key2','key1'])
print res1

res2 = pd.merge(left, right, how='outer', on=['key2', 'key1'])
print(res2)

res3 = pd.merge(left, right, how='inner', on=['key2', 'key1'])
print(res3)
