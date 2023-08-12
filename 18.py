import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

age_data = []
body_fat_data = []

persons = int(input("Enter the noof persons:"))
for i in range(0,persons):
    b = int(input("Enter the age:"))
    age_data.append(b)
    c = float(input("Enter the fat percentage:"))
    body_fat_data.append(c)

data = pd.DataFrame({'Age': age_data, '%Fat': body_fat_data})
mean_age = data['Age'].mean()
median_age = data['Age'].median()
std_age = data['Age'].std()

mean_fat = data['%Fat'].mean()
median_fat = data['%Fat'].median()
std_fat = data['%Fat'].std()

print("Age - Mean:", mean_age)
print("Age - Median:", median_age)
print("Age - Standard Deviation:", std_age)

print("%Fat - Mean:", mean_fat)
print("%Fat - Median:", median_fat)
print("%Fat - Standard Deviation:", std_fat)

plt.figure(figsize=(8, 6))
sns.boxplot(data=data)
plt.title("Boxplots for Age and %Fat")
plt.xlabel("Variables")
plt.ylabel("Values")
plt.show()


Output:
Enter the noof persons:3
Enter the age:15
Enter the fat percentage:42
Enter the age:15
Enter the fat percentage:52
Enter the age:63
Enter the fat percentage:41
Age - Mean: 31.0
Age - Median: 15.0
Age - Standard Deviation: 27.712812921102035
%Fat - Mean: 45.0
%Fat - Median: 42.0
%Fat - Standard Deviation: 6.082762530298219
