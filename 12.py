#line plot
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
temperatures = [25, 27, 28, 30, 32]
rainfall = [50, 45, 70, 80, 90]

#create Line Plot
plt.figure(figsize=(8,5))
plt.plot(months,temperatures,color='b',marker='o',linestyle='-',linewidth=2)
plt.title('monthly temperature data')
plt.xlabel('months')
plt.ylabel('temperatures')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Scatter plot
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
temperatures = [25, 27, 28, 30, 32]
rainfall = [50, 45, 70, 80, 90]

#create scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(months,rainfall,color='b',marker='o')
plt.title('monthly temperature data')
plt.xlabel('months')
plt.ylabel('rainfall')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

