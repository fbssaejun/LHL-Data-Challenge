'''

Challenge
Play around with the scatterplot and test out different correlations between the numerical variables in the dataset. Then, help Dot by answering these questions:

1. What kind of correlation is there between the Receipts (bn $) and % of GNP?

2. What is the correlation coefficient between the two columns?

3. Which columns are correlated the most?

'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('thai_tourism.csv')

# SOLUTION

# 1
df.corr()

'''
      	            Year	Number of tourists (m)	Receipts (bn $)	% of GNP
Year	              1.000000	0.936905	0.930061	0.870395
Number of tourists  (m)	0.936905	1.000000	0.994426	0.955270
Receipts (bn $)	    0.930061	0.994426	1.000000	0.932489
% of GNP	0.870395	0.955270	0.932489	1.000000

'''
# 2
df.corr().loc['Receipts (bn $)','% of GNP']
# => 0.9324892611735859

# 3
corr = df.corr().replace(1,0) # we replace 1 with 0 so max() function is not affected by 1
# maximum is in the row with index "Receipts (bn $)"
corr.max().sort_values()
'''
Year                      0.936905
% of GNP                  0.955270
Number of tourists (m)    0.994426
Receipts (bn $)           0.994426
dtype: float64
'''

corr['Receipts (bn $)'].idxmax()
# => 'Number of tourists (m)'
