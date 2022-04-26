'''

Challenge
Use our database to answer the following questions:

1. How many peaks are higher than 8000 metres? Use the len() function to count the number of rows of the DataFrame that were returned by the pd.read_sql() function.

2. How many women (sex = 'F') were part of the expeditions?

'''
# Solution
import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

#1
peaks = pd.read_sql('select * from peaks where heightm > 8000',conn)
len(peaks) # => 16

#2
members = pd.read_sql("select * from members where sex = 'F'",conn)
len(members) # => 7254
