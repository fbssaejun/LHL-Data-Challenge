'''

Challenge
Use the bar chart from matplotlib to answer the following question:

1. What were the two most popular Toyota's car categories in 2020?

'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('toyota_cars.csv')

# Solution

# Filter only year 2020 data
df = df[df.Year == 2020]
# Groupby category
grouped_df = df.groupby('Category').size()

#The Frame: Start our plot with a figure
plt.figure()
# The Body: Declaring the specific bar plot
plt.bar(x = grouped_df.index, height = grouped_df.values)
#To show the plot, end our plot with a plt.show()
plt.show()
