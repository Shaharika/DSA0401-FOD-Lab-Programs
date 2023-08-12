import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/shaharika/Documents/house.csv.csv")
print("csv  data ")
print(data)
house_data=np.array(data)
house_data=house_data.astype(int)
print("numpy array")
print(house_data)
bedroom=house_data[:,1]
four=house_data[bedroom>4]
avg=np.mean(four[:,0])
print("average of price greater than 4 bedroom",avg)
 

Output:
csv  data 
     price  bedrooms  sqft_living  sqft_lot
0   313000         3         1340      7912
1  2384000         6         3650      9050
2   342000         3         1930     11947
3   420000         3         2000      8030
4   550000         5         1940     10500
5   490000         5          880      6380
6   335000         4         1350      2560
7   482000         4         2710     35868
8   452500         3         2430     88426
numpy array
[[ 313000       3    1340    7912]
 [2384000       6    3650    9050]
 [ 342000       3    1930   11947]
 [ 420000       3    2000    8030]
 [ 550000       5    1940   10500]
 [ 490000       5     880    6380]
 [ 335000       4    1350    2560]
 [ 482000       4    2710   35868]
 [ 452500       3    2430   88426]]
average of price greater than 4 bedroom 1141333.3333333333
