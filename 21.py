import numpy as np
import pandas as pd

data = pd.read_csv("C:/Users/shaharika/Documents/rare_elements.csv")
concentration_measurements = data["concentration"].values

sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
precision = float(input("Enter the desired level of precision: "))
sample_mean = np.mean(concentration_measurements[:sample_size])
sample_std = np.std(concentration_measurements[:sample_size], ddof=1)
critical_value = np.abs(np.percentile(np.random.normal(0, 1, 10000), (1 - confidence_level / 2) * 100))
margin_of_error = critical_value * (sample_std / np.sqrt(sample_size))
confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error

required_sample_size = int(np.ceil((critical_value * sample_std / precision)**2))

print("\nPoint Estimation:")
print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std)

print("\nConfidence Interval:")
print("Lower Bound:", confidence_interval_lower)
print("Upper Bound:", confidence_interval_upper)

print("\nRequired Sample Size for Desired Precision:", required_sample_size)



Output:
Enter the sample size: 15
Enter the confidence level (between 0 and 1): 0.8
Enter the desired level of precision: 51

Point Estimation:
Sample Mean: 58.29
Sample Standard Deviation: 25.86213233453284

Confidence Interval:
Lower Bound: 56.775766224403476
Upper Bound: 59.80423377559652

Required Sample Size for Desired Precision: 1
