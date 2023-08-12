import numpy as np
import pandas as pd

#input data
data=pd.read_csv("C:/Users/shaharika/Documents/fod-1.csv")
print(data)
data1=np.array(data)
print(data1)

#maths
maths=np.array(data)[:,1]
print(maths)
len1=len(maths)
avg1=sum(maths)/len1
print(avg1)
3
#english
eng=np.array(data)[:,2]
print(eng)
avg2=sum(eng)/len(eng)
print(avg2)

#science
sci=np.array(data)[:,3]
print(sci)
avg3=sum(sci)/len(sci)
print(avg3)

#history
his=np.array(data)[:,4]
print(his)
avg4=sum(his)/len(his)
print(avg4)

#printing which has highest avg
if(avg1>avg2 and avg1>avg3 and avg1>avg4):
    print("maths has high avg")
elif(avg2>avg1 and avg2>avg3 and avg2>avg4):
    print("engish has high avg")
elif(avg3>avg1 and avg3>avg2 and avg3>avg4):
    print("science has high avg")
else:
    print("history has high avg")



Output:

    student  Math  Science  Englidh  History
0      rani    45       65       45       79
1     phani    25       45       45       96
2     amala    62       89       87       78
3  gowthami    45       89       95       48
4      roja    25       56       96       25
[['rani' 45 65 45 79]
 ['phani' 25 45 45 96]
 ['amala' 62 89 87 78]
 ['gowthami' 45 89 95 48]
 ['roja' 25 56 96 25]]
[45 25 62 45 25]
40.4
[65 45 89 89 56]
68.8
[45 45 87 95 96]
73.6
[79 96 78 48 25]
65.2
science has high avg

