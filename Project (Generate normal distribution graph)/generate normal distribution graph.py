import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Input values
mean = float(input("Enter the mean value: "))
std_dev = float(input("Enter the std_dev value: "))
z_score = float(input("Enter the Z-Score: "))

# Calculate the probability density function at the z-score
highlighted_pdf = norm.pdf(z_score, mean, std_dev)

# Find the p-value corresponding to the z-score
p_value = 2 * (1 - norm.cdf(np.abs(z_score)))

# Print the Z-Score and P-Value
print(f'Mean: {mean}')
print(f'Standard Deviation: {std_dev}')
print(f'Given Z-Score: {z_score}')
print(f'Calculated P-Value: {p_value:.4f}')

# Check if p-value is less than 0.05
if p_value < 0.05:
    print('Alternative hypothesis is accepted.')
else:
    print("Null hypothesis is rejected")

# Generate data for the standard normal distribution
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mean, std_dev)

# Plot the normal distribution
plt.plot(x, y, label='Standard Normal Distribution')
plt.vlines(z_score, 0, highlighted_pdf, colors='r', linestyles='dashed', label=f'Z-Score = {z_score:.2f}')
plt.fill_between(x, y, where=(x <= z_score), color='skyblue', alpha=0.4, label='Area to the left')
plt.title('Normal Distribution and Z-Score')
plt.xlabel('Z-Score')
plt.ylabel('Probability Density Function')
plt.legend()

# Add a table with input values, Z-Score, and P-Value
table_data = [['Mean', 'Standard Deviation', 'Given Z-Score', 'Calculated P-Value'],
              [mean, std_dev, z_score, p_value]]
plt.table(cellText=table_data, loc='bottom', cellLoc='center', bbox=[0, -0.5, 1, 0.4], colLabels=None)

# Add annotation for P-Value on the graph
plt.annotate(f'P-Value: {p_value:.4f}', xy=(0.5, 0.5), xycoords='axes fraction', ha='center', fontsize=10, color='green')

# Add a line for the P-Value on the graph
plt.axhline(y=p_value, color='green', linestyle='--', label=f'P-Value = {p_value:.4f}')

plt.show()
