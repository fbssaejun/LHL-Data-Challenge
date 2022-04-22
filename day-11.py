'''

Challenge

Which neighborhood has the biggest difference between maximum and minimum property price?

'''

# Solution 1

import pandas as pd
import numpy as np

df = pd.read_csv('dubai_properties_data.csv')
# np.ptp finds minimum and maximum value and finds the difference
df.groupby('neighborhood')['price'].agg(np.ptp).max() # => 34375112

# Solution 2

df = pd.read_csv('dubai_properties_data.csv')
# Use aggregate function to find min max of price, then find difference with axis 1 which sotres the value in 'min' column, extract that row.
min_max_difference = df.groupby('neighborhood')['price'].agg(['max', 'min']).diff(axis=1)['min']
# Get the min value since the difference is in negative value
min_max_difference.min()
