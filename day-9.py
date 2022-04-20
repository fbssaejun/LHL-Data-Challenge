'''

Challenge
Answer the following questions using the data:

1. How many Italian wines have a lower percentage of alcohol than 13%
2. How many wines are there in class 3?


Stretch Questions
How many wines have a level of magnesium between 90 and 100?
How many wines have a level of magnesium higher than 90, and a percentage of alcohol lower than 13.5%?

'''

import pandas as pd
df = pd.read_csv('wine.csv')
df.head()

# Solution

# 1
print(len(df[df['Alcohol'] < 13])) # => 86

# 2
print(len(df[df['Class'] == 3])) # => 48

# Stretch Questions

print(len(df[(df['Magnesium'] < 100) & (df['Magnesium'] > 90)])) # => 41
print(len(df[(df['Alcohol'] > 90) & (df['Alcohol'] < 13.5)])) # => 0
