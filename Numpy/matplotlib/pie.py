import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('stock_prices.csv')

# Extract data
companies = df['Company']
prices = df['Stock Price']

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(prices, labels=companies, autopct='%1.1f%%', startangle=140, 
        colors=plt.cm.Paired.colors)

plt.title('Stock Price Share by Company')
plt.axis('equal')  # Makes the pie chart circular
plt.show()
