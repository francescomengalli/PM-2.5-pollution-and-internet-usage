# I am importing libraries for all the computations below
from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
plt.legend(bbox_to_anchor=(1.05, 1.0))
# plt.legend(facecolor='white', framealpha=1)
plt.title('PM 2.5 pollution - top 10 countries')
plt.show()

# we saw the value of the parameter PM 2.5
# now we want to see if there are correlations between an increment of pollution and the usage of internet
#
# to show this, we need:
#                           - to consider 2010 as the reference year: any increment or decrement will be evident from this value
#                           - to import all the informations we have for each country
#                           - to see the correlations between each parameter and the pollution
