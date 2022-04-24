'''

Challenge
Step I: Using the season column, filter the DataFrame so it contains only rows for summer and winter.

Step II:Using groupby() and unstack(), compute the difference between the average temperature in summer and winter(at 9am) for all locations.

Question: What is the difference between the average summer temperatures (using variable Temp9am) and the average winter temperatures (using variable Temp9am) for Adelaide, Albany and Albury?

'''

# SOLUTION
import pandas as pd
df = df[df.season.isin(["winter","summer"])]
unstack = df.groupby(["Location","season"])[['Temp9am']].mean().unstack()
(unstack.iloc[:,0] - unstack.iloc[:,1]).tail(6)
'''

Location
Walpole         7.580851
Watsonia        9.739332
Williamtown    10.725402
Witchcliffe     8.162081
Wollongong      7.459804
Woomera        13.454238
dtype: float64

'''

print((unstack.iloc[:,0] - unstack.iloc[:,1])['Adelaide']) # 10.71286498520401
print((unstack.iloc[:,0] - unstack.iloc[:,1])['Albany']) # 7.395200302343159
print((unstack.iloc[:,0] - unstack.iloc[:,1])['Albury']) # 14.257000981580923
