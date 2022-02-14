# I am importing libraries for all the computations below
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# in order to build up the new dataset, we import the datasets we have

global_pollution_df = pd.read_csv('PM2.5 Global Air Pollution 2010-2017.csv')
users_per_country_df = pd.read_csv('number-of-internet-users-by-country.csv')
broadband_df = pd.read_csv('broadband-penetration-by-country.csv')
mobile_sub_df = pd.read_csv('mobile-cellular-subscriptions-per-100-people.csv')
share_df = pd.read_csv('share-of-individuals-using-the-internet.csv')

# now we estract the datas we are interested in
index = [2010,2011,2012,2013,2014,2015,2016]

# finding data for the pm2.5 pollution in India
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'India', '2016'].iloc[0]

india_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for indian internet users from year 2010
# output: list of all indian data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'India'), 'Number of internet users (OWID based on WB & UN)']
india_users = [niu[1883],niu[1884],niu[1885],niu[1886],niu[1887],niu[1888],niu[1889]]

# extracting data for broadband penetration in India
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='India'),'Fixed broadband subscriptions (per 100 people)']
india_broadcast = [nbp[1765],nbp[1766],nbp[1767],nbp[1768],nbp[1769],nbp[1770],nbp[1771]]

#extraxting data for mobile-cellular-subscriptions-per-100-people In India
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='India','Mobile cellular subscriptions (per 100 people)']
india_mobile = [nms[5172],nms[5173],nms[5174],nms[5175],nms[5176],nms[5177],nms[5178]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='India','Individuals using the Internet (% of population)']
india_share = [nsh[3052],nsh[3053],nsh[3054],nsh[3055],nsh[3056],nsh[3057],nsh[3058]]

india_df = pd.DataFrame({'PM2.5':india_pollution,'Internet_users' : india_users,'Broadcast':india_broadcast,'Mobile_subscriptions':india_mobile,'Share' : india_share})
india_df.index=index

print(india_df)

india_df.to_csv('10_16_02_india.csv')