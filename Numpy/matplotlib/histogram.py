import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('stock_prices.csv')


# Create histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Stock Price'], bins=10, color='orange', edgecolor='black')

# Add labels and title
plt.xlabel('Stock Price')
plt.ylabel('Frequency')
plt.title('Distribution of Apple Stock Prices')

# Show plot
plt.grid(True)
plt.show()
