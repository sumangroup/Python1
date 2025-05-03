import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('stock_prices.csv')

# Plot the line graph
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Stock Price'], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Apple Stock Prices Over Time')

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()
