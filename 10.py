import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1000, 1300, 1400, 2500, 1800, 1600]

#create a bar plot
plt.figure(figsize=(8,5))
plt.bar(months, sales, color='b')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

