import numpy as np
a=[]
for i in range(0,4):
    sales = int(input("Enter the sales of the year:"))
    a.append(sales)
sales_data = np.array(a)
print(sales_data)
total_sales_for_year = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Total sales for the year:", total_sales_for_year)
print("Percentage increase in sales from Q1 to Q4:", percentage_increase,"%")



Ouput:
Enter the sales of the year:1998
Enter the sales of the year:2001
Enter the sales of the year:2003
Enter the sales of the year:2004
[1998 2001 2003 2004]
Total sales for the year: 8006
Percentage increase in sales from Q1 to Q4: 0.3003003003003003 %
