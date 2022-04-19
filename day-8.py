'''

Challenge
Help Dot by answering following questions about Paris landmarks:

1.What is the most expensive landmark in Paris?
2.What is the average wait time for all landmarks?

'''

import pandas as pd
df = pd.read_csv('paris_landmarks.csv')
df.head()

# Solution

#1
df.iloc[df['price'].idxmax()]['landmark']

#2
df['queue_time'].mean()
