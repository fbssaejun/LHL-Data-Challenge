'''

Challenge

1. Which neighborhood has the highest average property price ?
2. Which neighborhood has the highest average  size_in_sqft ?

'''

# Solution
import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
# Group table with neighborhood and average values of price and size in square feet
grouped_table = df.groupby('neighborhood')[['price','size_in_sqft']].mean()

#1 Sort values by price from biggest to smallest, get the first (biggest) value
grouped_table.sort_values(['price'], ascending=False).head(1)

#2 Sort values by size_in_sqft from biggest to smallest, get the first (biggest) value
grouped_table.sort_values(['size_in_sqft'], ascending=False).head(1)
