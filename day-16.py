'''

Challenge¶
Answer following questions using our database:

1. How many expeditions went to the peak of Everest?

2. How many people went to the peak of Everest? (One person could have gone more than once)

'''

# Solution
import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

#1
everest = pd.read_sql('''
  select *
  from exped
  join peaks on exped.peakId = peaks.peakid where pkname='Everest'
  ''' , conn)

len(everest) # => 2161

#2
everest = pd.read_sql('''
  select *
  from members
  join peaks on members.peakId = peaks.peakid where pkname='Everest'
  ''' , conn)

len(everest) # => 21900
