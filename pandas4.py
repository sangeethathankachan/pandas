# import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
  
  
# accessing a element using index element
print(ser[16])
