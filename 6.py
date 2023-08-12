import numpy as np
cost=np.array([45,85,96,41,23])
qu=np.array([2,3,4,5,3])
dis=25
tax=10
for i in range(len(cost)):
    tot=cost*qu
    tot1=tot-tot*(dis/100)
    tot2=tot1-tot1*(tax/100)
    total=sum(tot2)
print("purchased amount after discount nad tax added:",total)



Output:
purchased amount after discount nad tax added: 677.0250000000001
