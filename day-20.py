'''

Challenge
Pull the data from table worldcities in the database world.db to Pandas data frame to answer the following questions:

1. Using histogram from matplotlib, visualize distribution of population across all cities. What do you observe?
2. Create bar chart with the population of top 10 the most populated countries. Which country is two most populated?

'''

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect("world.db")

# SOLUTION

# 1
# Create visualized graph using histogram 
query = 'select * from worldcities'
df = pd.read_sql(query, conn)
plt.figure()
plt.hist(df['population'], bins = 30) 
plt.show()

# 2
# Filter, find the most populated country from the dataframe
countries = df.groupby("country")['population'].sum().sort_values(ascending = False)
countries.head(1).index.values[0] # => 'China'
