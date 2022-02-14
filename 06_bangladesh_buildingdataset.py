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

# finding data for the pm2.5 pollution in Bangladesh
np10 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2010'].iloc[0]
np11 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2011'].iloc[0]
np12 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2012'].iloc[0]
np13 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2013'].iloc[0]
np14 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2014'].iloc[0]
np15 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2015'].iloc[0]
np16 = global_pollution_df.loc[global_pollution_df['Country Name'] == 'Bangladesh', '2016'].iloc[0]

bangladesh_pollution = [np10,np11,np12,np13,np14,np15,np16]

# finding data of the number of Internet users
# extracting data for internet users from year 2010
# output: list of all data about the number of internet users
upc_df=users_per_country_df
niu = upc_df.loc[(upc_df['Entity'] == 'Bangladesh'), 'Number of internet users (OWID based on WB & UN)']
bangladesh_users = [niu[316],niu[317],niu[318],niu[319],niu[320],niu[321],niu[322]]

# extracting data for broadband penetration 
# output: list of fixed broadband subscriptions
bp_df = broadband_df
nbp = bp_df.loc[(bp_df['Entity']=='Bangladesh'),'Fixed broadband subscriptions (per 100 people)']
bangladesh_broadcast = [nbp[283],nbp[284],nbp[285],nbp[286],nbp[287],nbp[288],nbp[289]]

#extraxting data for mobile-cellular-subscriptions-per-100-people
ms_df = mobile_sub_df
nms =ms_df.loc[ms_df['Entity']=='Bangladesh','Mobile cellular subscriptions (per 100 people)']
bangladesh_mobile = [nms[868],nms[869],nms[870],nms[871],nms[872],nms[873],nms[874]]

# extracting data for share of people using internet
nsh = share_df.loc[share_df['Entity']=='Bangladesh','Individuals using the Internet (% of population)']
bangladesh_share = [nsh[495],nsh[496],nsh[497],nsh[498],nsh[499],nsh[500],nsh[501]]

bangladesh_df = pd.DataFrame({'PM2.5':bangladesh_pollution,'Internet_users' : bangladesh_users,'Broadcast':bangladesh_broadcast,'Mobile_subscriptions':bangladesh_mobile,'Share' : bangladesh_share})
bangladesh_df.index=index

print(bangladesh_df)

bangladesh_df.to_csv('10_16_06_bangladesh.csv')