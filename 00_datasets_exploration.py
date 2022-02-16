# I am importing libraries for all the computations below
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

global_pollution_df = pd.read_csv('PM2.5 Global Air Pollution 2010-2017.csv') # importing the pollution dataset
users_per_country_df = pd.read_csv('number-of-internet-users-by-country.csv')
broadband_df = pd.read_csv('broadband-penetration-by-country.csv')
mobile_sub_df = pd.read_csv('mobile-cellular-subscriptions-per-100-people.csv')
share_df = pd.read_csv('share-of-individuals-using-the-internet.csv')
#print(global_pollution_df)
global_pollution_df.sort_values(by=['2010'], ascending = False).head(10)
# we look for the 10 most polluting countries (South Asia = South Asia (IDA & IBRD) are not so clear)
# this definition identifies a region in the northern India, our aim is to identify countries
print(global_pollution_df.sort_values(by=['2010'], ascending = False).head(12))
# 
# now we explore the other datasets
print(users_per_country_df)
print(users_per_country_df.info())

print(broadband_df)
print(broadband_df.info())

print(mobile_sub_df)
print(mobile_sub_df.info())

print(share_df)
print(share_df.info())