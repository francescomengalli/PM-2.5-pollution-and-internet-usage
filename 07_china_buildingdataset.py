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
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'China', '2016'].iloc[0]

china_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'China'), 'Number of internet users (OWID based on WB & UN)']
china_users = [niu[835],niu[836],niu[837],niu[838],niu[839],niu[840],niu[841]]

# extracting data for broadband penetration 
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='China'),'Fixed broadband subscriptions (per 100 people)']
china_broadcast = [nbp[724],nbp[725],nbp[726],nbp[727],nbp[728],nbp[729],nbp[730]]

#extraxting data for mobile-cellular-subscriptions-per-100-people
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='China','Mobile cellular subscriptions (per 100 people)']
china_mobile = [nms[2133],nms[2134],nms[2135],nms[2136],nms[2137],nms[2138],nms[2139]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='China','Individuals using the Internet (% of population)']
china_share = [nsh[1229],nsh[1230],nsh[1231],nsh[1232],nsh[1233],nsh[1234],nsh[1235]]

china_df = pd.DataFrame({'PM2.5':china_pollution,'Internet_users' : china_users,'Broadcast':china_broadcast,'Mobile_subscriptions':china_mobile,'Share' : china_share})
china_df.index=index

print(china_df)

china_df.to_csv('10_16_07_china.csv')