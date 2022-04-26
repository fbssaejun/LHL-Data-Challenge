'''

Challenge

1. Find the region (using variable regionName) with the lowest total amount of light (using variable classWeight) traffic, and the region with the lowest total amount of heavy (using variable classWeight) traffic

2. Using a bar chart, which month had the lowest amount of total traffic in 2020?

3. What percent of New Zealand’s traffic (using variable trafficCount) was classified as heavy (using variable classWeight) in 2020?

'''

# SOLUTION
import pandas as pd
df = pd.read_csv('nz_car_traffic.csv')

# 1
grouped = df.groupby(['regionName','classWeight'])[['trafficCount']].sum().unstack()
print(grouped.iloc[:,0].idxmin()) # heavy
print(grouped.iloc[:,1].idxmin()) # light

# 2
df.groupby("month").agg({"trafficCount":'sum'}).plot(kind='bar')

# 3
df[df.classWeight == 'Heavy'].trafficCount.sum() / df.trafficCount.sum()
