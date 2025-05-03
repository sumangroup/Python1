import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('stock_prices.csv')

# Create a bar graph
plt.figure(figsize=(10,6))
plt.bar(df['Date'], df['Stock Price'], color='skyblue')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Apple Stock Prices Over Time')
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
