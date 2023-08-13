import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
dataset = np.array([[1400, 3, 300000],
                    [1600, 3, 330000],
                    [1700, 3, 350000],
                    [1875, 2, 270000],
                    [1100, 2, 220000],
                    [1550, 4, 350000]])
X = dataset[:, :-1]
y = dataset[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

new_area = float(input("Enter the area of the new house: "))
new_bedrooms = int(input("Enter the number of bedrooms in the new house: "))

new_house_features = np.array([[new_area, new_bedrooms]])
predicted_price = model.predict(new_house_features)
location = input(f"Enter location : ")
print(location)
print(f"Predicted price for the new house: ${predicted_price[0]:.2f}")
  

Output:
Enter the area of the new house: 1425
Enter the number of bedrooms in the new house: 3
Enter location : chennai
chennai
Predicted price for the new house: $300205.05
