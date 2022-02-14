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

# finding data for the pm2.5 pollution
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Iraq', '2016'].iloc[0]

iraq_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Iraq'), 'Number of internet users (OWID based on WB & UN)']
iraq_users = [niu[1951],niu[1952],niu[1953],niu[1954],niu[1955],niu[1956],niu[1957]]

# extracting data for broadband penetration 
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Iraq'),'Fixed broadband subscriptions (per 100 people)']
iraq_broadcast = [nbp[1811],nbp[1812],nbp[1813],nbp[1814],nbp[1815],nbp[1816],nbp[1817]]

#extraxting data for mobile-cellular-subscriptions-per-100-people
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Iraq','Mobile cellular subscriptions (per 100 people)']
iraq_mobile = [nms[5316],nms[5317],nms[5318],nms[5319],nms[5320],nms[5321],nms[5322]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Iraq','Individuals using the Internet (% of population)']
iraq_share = [nsh[3135],nsh[3136],nsh[3137],nsh[3138],nsh[3139],nsh[3140],nsh[3141]]

iraq_df = pd.DataFrame({'PM2.5':iraq_pollution,'Internet_users' : iraq_users,'Broadcast':iraq_broadcast,'Mobile_subscriptions':iraq_mobile,'Share' : iraq_share})
iraq_df.index=index

print(iraq_df)

iraq_df.to_csv('10_16_09_iraq.csv')