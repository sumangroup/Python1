import pandas as pd

# Sample stock price data
data = {
    'Date': ['2025-04-28', '2025-04-29', '2025-04-30', '2025-05-01', '2025-05-02'],
    'Company': ['Apple', 'Apple', 'Apple', 'Apple', 'Apple'],
    'Stock Price': [172.15, 174.30, 175.50, 173.90, 170.75],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('stock_prices.csv', index=False)

print("CSV file 'stock_prices.csv' created successfully!")
