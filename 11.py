#bar plot
import matplotlib.pyplot as plt
Online_products =['watch','hand bag','lipstick','facewashes','bangles']
sales = [1000, 1200, 100, 250, 200]

#Create bar plot
plt.figure(figsize=(8,6))
plt.bar(Online_products, sales,color='g')
plt.title('Sales of Product Over Time')
plt.xlabel('Online_products')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#line plot
import matplotlib.pyplot as plt
Online_products =['watch','hand bag','lipstick','facewashes','bangles']
sales = [1000, 1200, 100, 250, 200]

#Create line plot
plt.figure(figsize=(8,5))
plt.plot(Online_products, sales,color='r',marker='o',linestyle='-',linewidth=2)
plt.title('Sales of Product Over Time')
plt.xlabel('Online_products')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Scatter plot
import matplotlib.pyplot as plt
Online_products =['watch','hand bag','lipstick','facewashes','bangles']
sales = [1000, 1200, 100, 250, 200]

#Create Scatter plot
plt.figure(figsize=(8,5))
plt.scatter(Online_products, sales,color='r',marker='o')
plt.title('Sales of Product Over Time')
plt.xlabel('Online_products')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


