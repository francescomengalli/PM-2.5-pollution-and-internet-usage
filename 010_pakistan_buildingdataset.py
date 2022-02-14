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
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Pakistan', '2016'].iloc[0]

pakistan_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Pakistan'), 'Number of internet users (OWID based on WB & UN)']
pakistan_users = [niu[3089],niu[3090],niu[3091],niu[3092],niu[3093],niu[3094],niu[3095]]

# extracting data for broadband penetration 
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Pakistan'),'Fixed broadband subscriptions (per 100 people)']
pakistan_broadcast = [nbp[2930],nbp[2931],nbp[2932],nbp[2933],nbp[2934],nbp[2935],nbp[2936]]

#extraxting data for mobile-cellular-subscriptions-per-100-people
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Pakistan','Mobile cellular subscriptions (per 100 people)']
pakistan_mobile = [nms[8536],nms[8537],nms[8538],nms[8539],nms[8540],nms[8541],nms[8542]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Pakistan','Individuals using the Internet (% of population)']
pakistan_share = [nsh[5046],nsh[5047],nsh[5048],nsh[5049],nsh[5050],nsh[5051],nsh[5052]]

pakistan_df = pd.DataFrame({'PM2.5':pakistan_pollution,'Internet_users' : pakistan_users,'Broadcast':pakistan_broadcast,'Mobile_subscriptions':pakistan_mobile,'Share' : pakistan_share})
pakistan_df.index=index

print(pakistan_df)

pakistan_df.to_csv('10_16_10_pakistan.csv')