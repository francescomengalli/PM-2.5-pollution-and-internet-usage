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

# finding data for the pm2.5 pollution in Qatar
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Qatar', '2016'].iloc[0]

qatar_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Qatar'), 'Number of internet users (OWID based on WB & UN)']
qatar_users = [niu[3327],niu[3328],niu[3329],niu[3330],niu[3331],niu[3332],niu[3333]]

# extracting data for broadband penetration in India
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Qatar'),'Fixed broadband subscriptions (per 100 people)']
qatar_broadcast = [nbp[3150],nbp[3151],nbp[3152],nbp[3153],nbp[3154],nbp[3155],nbp[3156]]

#extraxting data for mobile-cellular-subscriptions-per-100-people In India
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Qatar','Mobile cellular subscriptions (per 100 people)']
qatar_mobile = [nms[9090],nms[9091],nms[9092],nms[9093],nms[9094],nms[9095],nms[9096]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Qatar','Individuals using the Internet (% of population)']
qatar_share = [nsh[5404],nsh[5405],nsh[5406],nsh[5407],nsh[5408],nsh[5409],nsh[5410]]

qatar_df = pd.DataFrame({'PM2.5':qatar_pollution,'Internet_users' : qatar_users,'Broadcast':qatar_broadcast,'Mobile_subscriptions':qatar_mobile,'Share' : qatar_share})
qatar_df.index=index

print(qatar_df)

qatar_df.to_csv('10_16_03_qatar.csv')