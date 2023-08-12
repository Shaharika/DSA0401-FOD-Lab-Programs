import numpy as np
sales_data = []
for i in range(4):
    b = int(input("Enter the sales data:"))
    sales_data.append(b)
c = np.array(sales_data)
print(c)
average_price = np.mean(sales_data)
print("Average price of all products sold in the past month:", average_price)



Output:
Enter the sales data:21
Enter the sales data:15
Enter the sales data:41
Enter the sales data:25
[21 15 41 25]
Average price of all products sold in the past month: 25.5
