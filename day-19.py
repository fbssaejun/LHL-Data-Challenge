'''

Challenge
Use air traffic data to help Dot by finding out which US city has the best connection with Vancouver.

1. What is the origin city (using variable ORIGIN_CITY_NAME) with the highest total number of passengers who travelled to Vancouver?
2. According to our data, how many passengers travelled from that origin city to Vancouver?
3. Use a histogram to plot the probability distribution of distances for all routes in June 2021.

'''
# Solution
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('air_traffic_data.csv')

# 1 & 2

# Filter datafram by destination city name that has the value of Vancouver, Canada
vancouver_destination = df.loc[df['DEST_CITY_NAME'] == "Vancouver, Canada"]
# Get sum of all passengers grouped by origin city name
total_passengers = vancouver_destination.groupby('ORIGIN_CITY_NAME')[['PASSENGERS']].sum()
# Find the origin city with the maximum total passengers
total_passengers.loc[total_passengers['PASSENGERS'] == total_passengers['PASSENGERS'].max()] # => Seattle, WA / 17109

# 3 Create histogram to generate visualized data graph
plt.figure()
plt.hist(df[df['MONTH'] == 6]['DISTANCE'], bins = 30)
plt.show()
