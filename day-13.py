'''

Challenge
Use the Pandas plot function to answer these two questions:

Using a histogram, what is the most likely temperature at 9am (Temp9am) in Melbourne?
Using a boxplot, does it ever rain (using variable Rainfall) in Melbourne? If yes, what was the highest daily amount recorded?

'''

import pandas as pd
df = pd.read_csv('aus_weather.csv')
df = df[df["Location"] == "Melbourne"]

# SOLUTION
df.Temp9am.plot(kind="hist")

df.Rainfall.plot(kind='box')
