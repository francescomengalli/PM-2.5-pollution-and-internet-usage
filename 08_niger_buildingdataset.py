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
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Niger', '2016'].iloc[0]

niger_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Niger'), 'Number of internet users (OWID based on WB & UN)']
niger_users = [niu[2955],niu[2956],niu[2957],niu[2958],niu[2959],niu[2960],niu[2961]]

# extracting data for broadband penetration 
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Niger'),'Fixed broadband subscriptions (per 100 people)']
niger_broadcast = [nbp[2779],nbp[2780],nbp[2781],nbp[2782],nbp[2783],nbp[2784],nbp[2785]]

#extraxting data for mobile-cellular-subscriptions-per-100-people
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Niger','Mobile cellular subscriptions (per 100 people)']
niger_mobile = [nms[8035],nms[8036],nms[8037],nms[8038],nms[8039],nms[8040],nms[8041]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Niger','Individuals using the Internet (% of population)']
niger_share = [nsh[4759],nsh[4760],nsh[4761],nsh[4762],nsh[4763],nsh[4764],nsh[4765]]

niger_df = pd.DataFrame({'PM2.5':niger_pollution,'Internet_users' : niger_users,'Broadcast':niger_broadcast,'Mobile_subscriptions':niger_mobile,'Share' : niger_share})
niger_df.index=index

print(niger_df)

niger_df.to_csv('10_16_08_niger.csv')