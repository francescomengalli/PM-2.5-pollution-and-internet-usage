# I am importing libraries for all the computations below
from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#########################################################################################################################################
# Now I import all the datasets I have built up in order to make our analysis

years = [2010,2011,2012,2013,2014,2015,2016]

nepal_df = pd.read_csv('10_16_01_nepal.csv')
india_df = pd.read_csv('10_16_02_india.csv')
qatar_df = pd.read_csv('10_16_03_qatar.csv')
saudiarabia_df = pd.read_csv('10_16_04_saudiarabia.csv')
egypt_df = pd.read_csv('10_16_05_egypt.csv')
bangladesh_df = pd.read_csv('10_16_06_bangladesh.csv')
china_df = pd.read_csv('10_16_07_china.csv')
niger_df = pd.read_csv('10_16_08_niger.csv')
iraq_df = pd.read_csv('10_16_09_iraq.csv')
pakistan_df = pd.read_csv('10_16_10_pakistan.csv')

# values of pollution in different states

nep_pol = nepal_df['PM2.5']
india_pol = india_df['PM2.5']
qat_pol = qatar_df['PM2.5']
saab_pol = saudiarabia_df['PM2.5']
egy_pol = egypt_df['PM2.5']
ban_pol = bangladesh_df['PM2.5']
chi_pol = china_df['PM2.5']
nig_pol = niger_df['PM2.5']
iraq_pol = iraq_df['PM2.5']
pak_pol = pakistan_df['PM2.5']

# we take 2010 as reference year to see increments or decrements in the following years
nep_pol = np.divide(nep_pol,nep_pol[0])
india_pol = np.divide(india_pol,india_pol[0])
qat_pol = np.divide(qat_pol,qat_pol[0])
saab_pol = np.divide(saab_pol,saab_pol[0])
egy_pol = np.divide(egy_pol,egy_pol[0])
ban_pol = np.divide(ban_pol,ban_pol[0])
chi_pol = np.divide(chi_pol,chi_pol[0])
nig_pol = np.divide(nig_pol,nig_pol[0])
iraq_pol = np.divide(iraq_pol,iraq_pol[0])
pak_pol = np.divide(pak_pol,pak_pol[0])

plt.plot(years,nep_pol,label='Nepal')
plt.plot(years,india_pol,label='India')
plt.plot(years,qat_pol,label='Qatar')
plt.plot(years,saab_pol,label='Saudi Arabia')
plt.plot(years,egy_pol,label='Egypt')
plt.plot(years,ban_pol,label='Bangladesh')
plt.plot(years,chi_pol,label='China')
plt.plot(years,nig_pol,label='Niger')
plt.plot(years,iraq_pol,label='Iraq')
plt.plot(years,pak_pol,label='Pakistan')
plt.xlabel('Years')
plt.ylabel('Pollution index')
plt.legend(facecolor='white',framealpha=1)
# plt.legend(facecolor='white', framealpha=1)
plt.title('PM 2.5 pollution - top 10 countries')
plt.show()

#########################################################################################################################################
#########################################################################################################################################

# we saw the value of the parameter PM 2.5
# now we want to see if there are correlations between an increment of pollution and the usage of internet
#
# to show this, we need:
#                           - to consider 2010 as the reference year: any increment or decrement will be evident from this value
#                           - to import all the informations we have for each country
#                           - to see the correlations between each parameter and the pollution
# 
# this should be done for each country

#########################################################################################################################################
#########################################################################################################################################
#
# Nepal
nep_pol = nepal_df['PM2.5']                         # taking data of the pollution
nep_int = nepal_df['Internet_users']                # taking data for the internet usage
nep_bro = nepal_df['Broadcast']                     # taking data for broadcast
nep_mob = nepal_df['Mobile_subscriptions']          # taking data for mobile subscriptions
nep_sch = nepal_df['Share']                         # taking data for share

# now we want to find out the increment or decrement of each parameter
nep_pol = np.divide(nep_pol,nep_pol[0])
nep_int = np.divide(nep_int,nep_int[0])
nep_bro = np.divide(nep_bro,nep_bro[0])
nep_mob = np.divide(nep_mob,nep_mob[0])
nep_sch = np.divide(nep_sch,nep_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,nep_pol,label='PM 2.5')
plt.plot(years,nep_int,label='Internet users')
plt.plot(years,nep_bro,label='Broadcast')
plt.plot(years,nep_mob,label='Mobile subscriptions')
plt.plot(years,nep_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Nepal')
plt.legend(facecolor='white',framealpha=1)
plt.show()

#########################################################################################################################################

# India

india_pol = india_df['PM2.5']                       # taking data of the pollution
india_int = india_df['Internet_users']              # taking data for the internet usage
india_bro = india_df['Broadcast']                   # taking data for broadcast
india_mob = india_df['Mobile_subscriptions']        # taking data for mobile subscriptions
india_sch = india_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
india_pol = np.divide(india_pol,india_pol[0])
india_int = np.divide(india_int,india_int[0])
india_bro = np.divide(india_bro,india_bro[0])
india_mob = np.divide(india_mob,india_mob[0])
india_sch = np.divide(india_sch,india_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,india_pol,label='PM 2.5')
plt.plot(years,india_int,label='Internet users')
plt.plot(years,india_bro,label='Broadcast')
plt.plot(years,india_mob,label='Mobile subscriptions')
plt.plot(years,india_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('India')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# Qatar

qatar_pol = qatar_df['PM2.5']                       # taking data of the pollution
qatar_int = qatar_df['Internet_users']              # taking data for the internet usage
qatar_bro = qatar_df['Broadcast']                   # taking data for broadcast
qatar_mob = qatar_df['Mobile_subscriptions']        # taking data for mobile subscriptions
qatar_sch = qatar_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
qatar_pol = np.divide(qatar_pol,qatar_pol[0])
qatar_int = np.divide(qatar_int,qatar_int[0])
qatar_bro = np.divide(qatar_bro,qatar_bro[0])
qatar_mob = np.divide(qatar_mob,qatar_mob[0])
qatar_sch = np.divide(qatar_sch,qatar_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,qatar_pol,label='PM 2.5')
plt.plot(years,qatar_int,label='Internet users')
plt.plot(years,qatar_bro,label='Broadcast')
plt.plot(years,qatar_mob,label='Mobile subscriptions')
plt.plot(years,qatar_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Qatar')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# Saudi Arabia

saab_pol = saudiarabia_df['PM2.5']                       # taking data of the pollution
saab_int = saudiarabia_df['Internet_users']              # taking data for the internet usage
saab_bro = saudiarabia_df['Broadcast']                   # taking data for broadcast
saab_mob = saudiarabia_df['Mobile_subscriptions']        # taking data for mobile subscriptions
saab_sch = saudiarabia_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
saab_pol = np.divide(saab_pol,saab_pol[0])
saab_int = np.divide(saab_int,saab_int[0])
saab_bro = np.divide(saab_bro,saab_bro[0])
saab_mob = np.divide(saab_mob,saab_mob[0])
saab_sch = np.divide(saab_sch,saab_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,saab_pol,label='PM 2.5')
plt.plot(years,saab_int,label='Internet users')
plt.plot(years,saab_bro,label='Broadcast')
plt.plot(years,saab_mob,label='Mobile subscriptions')
plt.plot(years,saab_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Saudi Arabia')
plt.legend(facecolor='white',framealpha=1)
plt.show()

#########################################################################################################################################

# Egypt

egy_pol = egypt_df['PM2.5']                       # taking data of the pollution
egy_int = egypt_df['Internet_users']              # taking data for the internet usage
egy_bro = egypt_df['Broadcast']                   # taking data for broadcast
egy_mob = egypt_df['Mobile_subscriptions']        # taking data for mobile subscriptions
egy_sch = egypt_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
egy_pol = np.divide(egy_pol,egy_pol[0])
egy_int = np.divide(egy_int,egy_int[0])
egy_bro = np.divide(egy_bro,egy_bro[0])
egy_mob = np.divide(egy_mob,egy_mob[0])
egy_sch = np.divide(egy_sch,egy_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,egy_pol,label='PM 2.5')
plt.plot(years,egy_int,label='Internet users')
plt.plot(years,egy_bro,label='Broadcast')
plt.plot(years,egy_mob,label='Mobile subscriptions')
plt.plot(years,egy_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Egypt')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# Bangladesh

ban_pol = bangladesh_df['PM2.5']                       # taking data of the pollution
ban_int = bangladesh_df['Internet_users']              # taking data for the internet usage
ban_bro = bangladesh_df['Broadcast']                   # taking data for broadcast
ban_mob = bangladesh_df['Mobile_subscriptions']        # taking data for mobile subscriptions
ban_sch = bangladesh_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
ban_pol = np.divide(ban_pol,ban_pol[0])
ban_int = np.divide(ban_int,ban_int[0])
ban_bro = np.divide(ban_bro,ban_bro[0])
ban_mob = np.divide(ban_mob,ban_mob[0])
ban_sch = np.divide(ban_sch,ban_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,ban_pol,label='PM 2.5')
plt.plot(years,ban_int,label='Internet users')
plt.plot(years,ban_bro,label='Broadcast')
plt.plot(years,ban_mob,label='Mobile subscriptions')
plt.plot(years,ban_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentual variation')
plt.title('Bangladesh')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# China

chi_pol = china_df['PM2.5']                       # taking data of the pollution
chi_int = china_df['Internet_users']              # taking data for the internet usage
chi_bro = china_df['Broadcast']                   # taking data for broadcast
chi_mob = china_df['Mobile_subscriptions']        # taking data for mobile subscriptions
chi_sch = china_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
chi_pol = np.divide(chi_pol,chi_pol[0])
chi_int = np.divide(chi_int,chi_int[0])
chi_bro = np.divide(chi_bro,chi_bro[0])
chi_mob = np.divide(chi_mob,chi_mob[0])
chi_sch = np.divide(chi_sch,chi_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,chi_pol,label='PM 2.5')
plt.plot(years,chi_int,label='Internet users')
plt.plot(years,chi_bro,label='Broadcast')
plt.plot(years,chi_mob,label='Mobile subscriptions')
plt.plot(years,chi_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('China')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# Niger

nig_pol = niger_df['PM2.5']                       # taking data of the pollution
nig_int = niger_df['Internet_users']              # taking data for the internet usage
nig_bro = niger_df['Broadcast']                   # taking data for broadcast
nig_mob = niger_df['Mobile_subscriptions']        # taking data for mobile subscriptions
nig_sch = niger_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
nig_pol = np.divide(nig_pol,nig_pol[0])
nig_int = np.divide(nig_int,nig_int[0])
nig_bro = np.divide(nig_bro,nig_bro[0])
nig_mob = np.divide(nig_mob,nig_mob[0])
nig_sch = np.divide(nig_sch,nig_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,nig_pol,label='PM 2.5')
plt.plot(years,nig_int,label='Internet users')
plt.plot(years,nig_bro,label='Broadcast')
plt.plot(years,nig_mob,label='Mobile subscriptions')
plt.plot(years,nig_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Niger')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# Iraq

iraq_pol = iraq_df['PM2.5']                       # taking data of the pollution
iraq_int = iraq_df['Internet_users']              # taking data for the internet usage
iraq_bro = iraq_df['Broadcast']                   # taking data for broadcast
iraq_mob = iraq_df['Mobile_subscriptions']        # taking data for mobile subscriptions
iraq_sch = iraq_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
iraq_pol = np.divide(iraq_pol,iraq_pol[0])
iraq_int = np.divide(iraq_int,iraq_int[0])
iraq_bro = np.divide(iraq_bro,iraq_bro[0])
iraq_mob = np.divide(iraq_mob,iraq_mob[0])
iraq_sch = np.divide(iraq_sch,iraq_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,iraq_pol,label='PM 2.5')
plt.plot(years,iraq_int,label='Internet users')
#plt.plot(years,iraq_bro,label='Broadcast')
plt.plot(years,iraq_mob,label='Mobile subscriptions')
plt.plot(years,iraq_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Iraq')
plt.legend(facecolor='white',framealpha=1)
plt.show()


#########################################################################################################################################

# Pakistan

pak_pol = pakistan_df['PM2.5']                       # taking data of the pollution
pak_int = pakistan_df['Internet_users']              # taking data for the internet usage
pak_bro = pakistan_df['Broadcast']                   # taking data for broadcast
pak_mob = pakistan_df['Mobile_subscriptions']        # taking data for mobile subscriptions
pak_sch = pakistan_df['Share']                       # taking data for share

# now we want to find out the increment or decrement of each parameter
pak_pol = np.divide(pak_pol,pak_pol[0])
pak_int = np.divide(pak_int,pak_int[0])
pak_bro = np.divide(pak_bro,pak_bro[0])
pak_mob = np.divide(pak_mob,pak_mob[0])
pak_sch = np.divide(pak_sch,pak_sch[0])

# now we plot a graph
plt.figure(figsize=(8,5))
plt.plot(years,pak_pol,label='PM 2.5')
plt.plot(years,pak_int,label='Internet users')
plt.plot(years,pak_bro,label='Broadcast')
plt.plot(years,pak_mob,label='Mobile subscriptions')
plt.plot(years,pak_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Pakistan')
plt.legend(facecolor='white',framealpha=1)
plt.show()

#########################################################################################################################################
#########################################################################################################################################
plt.figure()
plt.subplot(1,2,1)
plt.plot(years,nep_pol,label='PM 2.5')
plt.plot(years,nep_int,label='Internet users')
plt.plot(years,nep_bro,label='Broadcast')
plt.plot(years,nep_mob,label='Mobile subscriptions')
plt.plot(years,nep_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('Nepal')

plt.subplot(1,2,2)
plt.figure(figsize=(8,5))
plt.plot(years,india_pol,label='PM 2.5')
plt.plot(years,india_int,label='Internet users')
plt.plot(years,india_bro,label='Broadcast')
plt.plot(years,india_mob,label='Mobile subscriptions')
plt.plot(years,india_sch,label='Share')
plt.xlabel('Years')
plt.ylabel('Percentage variation')
plt.title('India')