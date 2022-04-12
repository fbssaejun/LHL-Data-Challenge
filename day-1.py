"""
Challenge

Find a connection to Europe that will give them the best value per hour of travel time. The following tickets are available for the connection:

Vancouver - Toronto: 250 CAD, travel time 3.5 hours
Vancouver - Ottawa: 280 CAD, travel time 4 hours
Vancouver - Montreal: 240 CAD, travel time 4 hours
Vancouver - Edmonton: 150 CAD, travel time 1.5 hours
Vancouver - Calgary: 180 CAD, travel time 1 hour
These tickets are available for the second leg of the trip:

Ottawa - Berlin: 1350 CAD, layover: 3.5 hours, travel time 9 hours
Montreal - London: 1300 CAD, layover: 2 hours, travel time 8 hours
Edmonton - London: 1200 CAD, layover: 5 hours, travel time 10 hours
Calgary - London: 1400 CAD, layover: 2.5 hours, travel time 10 hours
Toronto - Munich: 990 CAD, layover: 1.5 hours, travel time 9.5 hours
Using math operators in Python, find out which flight will give Dot the best value per hour of travel time.

value = price_paid / travel_time

"""

# First connection
van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

# First connection travel time
van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

# Second connection
ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

# Layover time
ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

# Second connection travel time
ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

# value = total_price / total_travel_time
van_ed_lon = (van_edm_price + edm_lon_price) / (van_edm_travel_time + edm_lon_travel_time + edm_layover)
van_cal_lon = (van_cal_price + cal_lon_price) / (van_cal_travel_time + cal_lon_travel_time + cal_layover)
van_tor_mun = (van_tor_price + tor_mun_price) / (van_tor_travel_time + tor_mun_travel_time + tor_layover)
van_ott_ber = (van_ott_price + ott_ber_price) / (van_ott_travel_time + ott_ber_travel_time + ott_layover)
van_mon_lon = (van_mon_price + mon_lon_price) / (van_mon_travel_time + mon_lon_travel_time + mon_layover)

print(van_ed_lon) # => 87.27272727272727
print(van_cal_lon) # => 117.03703703703704
print(van_tor_mun) # => 85.51724137931035 (Answer)
print(van_ott_ber) # => 98.78787878787878
print(van_mon_lon) # => 110.0


# Answer : Vancouver -> Toronto -> Munich

travel_routes = [van_ed_lon, van_cal_lon, van_tor_mun, van_ott_ber, van_mon_lon]

# Create function that loops through an array of values and print the minimal value
def find_best_val(arr):
  print(min(arr))


find_best_val(travel_routes) # => 85.51724137931035
