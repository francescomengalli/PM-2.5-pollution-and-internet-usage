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

# finding data for the pm2.5 pollution in Saudi Arabia
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Saudi Arabia', '2016'].iloc[0]

saudiarabia_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Saudi Arabia'), 'Number of internet users (OWID based on WB & UN)']
saudiarabia_users = [niu[3513],niu[3514],niu[3515],niu[3516],niu[3517],niu[3518],niu[3519]]

# extracting data for broadband penetration in Saudi Arabia
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Saudi Arabia'),'Fixed broadband subscriptions (per 100 people)']
saudiarabia_broadcast = [nbp[3316],nbp[3317],nbp[3318],nbp[3319],nbp[3320],nbp[3321],nbp[3322]]

#extraxting data for mobile-cellular-subscriptions-per-100-people in Saudi Arabia
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Saudi Arabia','Mobile cellular subscriptions (per 100 people)']
saudiarabia_mobile = [nms[9516],nms[9517],nms[9518],nms[9519],nms[9520],nms[9521],nms[9522]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Saudi Arabia','Individuals using the Internet (% of population)']
saudiarabia_share = [nsh[5677],nsh[5678],nsh[5679],nsh[5680],nsh[5681],nsh[5682],nsh[5683]]

saudiarabia_df = pd.DataFrame({'PM2.5':saudiarabia_pollution,'Internet_users' : saudiarabia_users,'Broadcast':saudiarabia_broadcast,'Mobile_subscriptions':saudiarabia_mobile,'Share' : saudiarabia_share})
saudiarabia_df.index=index

print(saudiarabia_df)

saudiarabia_df.to_csv('10_16_04_saudiarabia.csv')