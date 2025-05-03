import pandas as pd
dt=pd.read_csv('stock_prices.csv')
print(dt)
print('-'*50)

# sort the DataFrame by the 'Stock Price' column (ascending order by default)
dt_sorted=dt.sort_values(by='Stock Price')
print(dt_sorted)
print('-'*50)

# sort by index
dt_index=dt.sort_index(ascending=False)
print(dt_index)
print('-'*50)

# rank
dt['Price Rank'] = dt['Stock Price'].rank(ascending=False)
print(dt)
print('-'*50)

#Aggregation
total_price=dt['Stock Price'].sum()
print('sum',total_price)
mean_price = dt['Stock Price'].mean()
print('avg',mean_price)
max_price = dt['Stock Price'].max()
print('max',max_price)
min_price = dt['Stock Price'].min()
print('min',min_price)
count_price = dt['Stock Price'].count()
print('count',count_price)

#filter
filtered_df = dt[dt['Stock Price'] > 173]
print(filtered_df)

