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
year = ['2010','2011','2012','2013','2014','2015','2016']

# finding data for the pm2.5 pollution in Nepal
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Nepal', '2016'].iloc[0]

nepal_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for italian internet users from year 2010
# output: list of all italian data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Nepal'), 'Number of internet users (OWID based on WB & UN)']
nepal_users = [niu[2832],niu[2833],niu[2834],niu[2835],niu[2836],niu[2837],niu[2838]]

# extracting data for broadband penetration in Nepal
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Nepal'),'Fixed broadband subscriptions (per 100 people)']
nepal_broadcast = [nbp[2690],nbp[2691],nbp[2692],nbp[2693],nbp[2694],nbp[2695],nbp[2696]]

#extraxting data for mobile-cellular-subscriptions-per-100-people In Nepal
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Nepal','Mobile cellular subscriptions (per 100 people)']
nepal_mobile = [nms[7803],nms[7804],nms[7805],nms[7806],nms[7807],nms[7808],nms[7809]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Nepal','Individuals using the Internet (% of population)']
nepal_share = [nsh[4617],nsh[4618],nsh[4619],nsh[4620],nsh[4621],nsh[4622],nsh[4623]]

nepal_df = pd.DataFrame({'PM2.5':nepal_pollution,'Internet_users' : nepal_users,'Broadcast':nepal_broadcast,'Mobile_subscriptions':nepal_mobile,'Share' : nepal_share})
nepal_df.index=year
nepal_df.index.name = 'Year'
print(nepal_df)

nepal_df.to_csv('10_16_01_nepal.csv')
print(nepal_df.corr())