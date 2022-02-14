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

# finding data for the pm2.5 pollution in Egypt
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Egypt, Arab Rep.', '2016'].iloc[0]

egypt_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Egypt'), 'Number of internet users (OWID based on WB & UN)']
egypt_users = [niu[1207],niu[1208],niu[1209],niu[1210],niu[1211],niu[1212],niu[1213]]

# extracting data for broadband penetration in Egypt
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Egypt'),'Fixed broadband subscriptions (per 100 people)']
egypt_broadcast = [nbp[1074],nbp[1075],nbp[1076],nbp[1077],nbp[1078],nbp[1079],nbp[1080]]

#extraxting data for mobile-cellular-subscriptions-per-100-people in Egypt
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Egypt','Mobile cellular subscriptions (per 100 people)']
egypt_mobile = [nms[3095],nms[3096],nms[3097],nms[3098],nms[3099],nms[3100],nms[3101]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Egypt','Individuals using the Internet (% of population)']
egypt_share = [nsh[1808],nsh[1809],nsh[1810],nsh[1811],nsh[1812],nsh[1813],nsh[1813]]

egypt_df = pd.DataFrame({'PM2.5':egypt_pollution,'Internet_users' : egypt_users,'Broadcast':egypt_broadcast,'Mobile_subscriptions':egypt_mobile,'Share' : egypt_share})
egypt_df.index=index

print(egypt_df)

egypt_df.to_csv('10_16_05_egypt.csv')