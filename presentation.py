#############################################################################################################################################
#   IMPORTING LIBRARIES
#from pyexpat import features
from importlib.util import spec_from_file_location
from tkinter import Button
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sn
#############################################################################################################################################
#   IMPORTING DATABASES
global_pollution_df = pd.read_csv('PM2.5 Global Air Pollution 2010-2017.csv')
users_per_country_df = pd.read_csv('number-of-internet-users-by-country.csv')
broadband_df = pd.read_csv('broadband-penetration-by-country.csv')
mobile_sub_df = pd.read_csv('mobile-cellular-subscriptions-per-100-people.csv')
share_df = pd.read_csv('share-of-individuals-using-the-internet.csv')
years = ['2010','2011','2012','2013','2014','2015','2016']
#############################################################################################################################################
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
#############################################################################################################################################
# CREATING HEADER
with header:
    st.title('PM 2.5 and Internet usage')
    st.text('Is there any correlation between pollution and using the Internet?')
    st.write('PM 2.5 indicates little pieces smaller than or equal to 2.5 micron (1/4 of the more famous PM 10)')
    first_button = st.checkbox('Original databases')
    second_button = st.checkbox('Overview of the first 10 most polluting countries')
    third_button = st.checkbox('New databases')


# Now we have the possibility to choose what to see in the presentation

#############################################################################################################################################
#   FIRST BUTTON
#############################################################################################################################################
with dataset:
    if first_button == True:            # here we can see the five original databases without any change or improvement
        with dataset:
            st.title('Original databases')
            st.text('Here we can see the original databases')
            choice = st.selectbox('Select',["PM 2.5","Internet usage"])
            if choice == "PM 2.5":
                with dataset:
                    st.text('We have data for all the countries around the world in the period 2010 - 2016')
                    first_choice = st.selectbox('Select',["Original dataset","First 10 polluting countries"])
                    if first_choice == "Original dataset":
                        st.dataframe(global_pollution_df)
                    else:
                        st.dataframe(global_pollution_df.sort_values(by=['2010'], ascending = False).head(12))
            else:
                with dataset:
                    second_choice = st.selectbox('Select',['Broadband','Mobile subscriptions','Number of internet users','Share of individuals using the Internet'])
                    if second_choice == "Broadband":
                        st.dataframe(broadband_df)
                        st.text('We have data for all the countries around the world in the period 1990 - 2016')
                    elif second_choice == 'Mobile subscriptions':
                        st.dataframe(mobile_sub_df)
                        st.text('We have data for all the countries around the world in the period 1960 - 2016')
                    elif second_choice == 'Number of internet users':
                        st.dataframe(users_per_country_df)
                        st.text('We have data for all the countries around the world in the period 1990 - 2016')
                    else:
                        st.dataframe(share_df)
                        st.text('We have data for all the countries around the world in the period 1990 - 2017')

#############################################################################################################################################
#   SECOND BUTTON               overview of the top 10 polluting countries
#############################################################################################################################################

    if second_button == True:                                   # in this section we have an idea of the grouth of pollution in these countries
        # values of pollution in different states
        image = Image.open('top10pollutingcountries.jpg')
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
        graph_df = pd.DataFrame({'Nepal':nep_pol,'India':india_pol,'Qatar':qat_pol,'Saudi Arabia':saab_pol,'Egypt':egy_pol,'Bangladesh':ban_pol,'China':chi_pol,'Niger':nig_pol,'Iraq':iraq_pol,'Pakistan':pak_pol})
        graph_df.index = years
        graph_df.index.name = 'Year'

        st.image(image,caption='10 most polluting countries')
        st.write('Population in this area: 5,109,754,000')
        st.write('This is the 68.46% of the global population in 2016')
        st.line_chart(graph_df)
        st.write('Increment or the decrement of pollution in these countries')

#############################################################################################################################################
#   THIRD BUTTON                we can see the new databases for each country and the correlation matrix
#############################################################################################################################################
    if third_button == True:       # we can see the new database for each country
        country_choice = st.selectbox('Select Country',['Nepal','India','Qatar','Saudi Arabia','Egypt','Bangladesh','China','Niger','Iraq','Pakistan'])
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

        if country_choice == 'Nepal':
            nepal_df.index = years
            nepal_df.index.name = 'Year'
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
            new_nepal_df = pd.DataFrame({'PM2.5':nep_pol,'Internet_users' : nep_int,'Broadcast':nep_bro,'Mobile_subscriptions':nep_mob,'Share' : nep_sch})
            new_nepal_df.index = years 
            st.subheader('The dataset')
            st.dataframe(nepal_df)
            st.subheader('Correlation Matrix')
            st.dataframe(nepal_df.corr())
            st.line_chart(new_nepal_df)

        elif country_choice == 'India':
            india_df.index = years
            india_df.index.name = 'Year'
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
            new_india_df = pd.DataFrame({'PM2.5':india_pol,'Internet_users' : india_int,'Broadcast':india_bro,'Mobile_subscriptions':india_mob,'Share' : india_sch})
            new_india_df.index = years
            st.subheader('The dataset')
            st.dataframe(india_df)
            st.subheader('Correlation Matrix')
            st.dataframe(india_df.corr())
            st.line_chart(new_india_df)

        elif country_choice == 'Qatar':
            qatar_df.index = years
            qatar_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(qatar_df)
            st.subheader('Correlation Matrix')
            st.dataframe(qatar_df.corr())            
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
            new_qatar_df = pd.DataFrame({'PM2.5':qatar_pol,'Internet_users' : qatar_int,'Broadcast':qatar_bro,'Mobile_subscriptions':qatar_mob,'Share' : qatar_sch})
            new_qatar_df.index = years
            st.line_chart(new_qatar_df)

        elif country_choice == 'Saudi Arabia':
            saudiarabia_df.index = years
            saudiarabia_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(saudiarabia_df)
            st.subheader('Correlation Matrix')
            st.dataframe(saudiarabia_df.corr())
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
            new_saudiarabia_df = pd.DataFrame({'PM2.5':saab_pol,'Internet_users':saab_int,'Broadcast':saab_bro,'Mobile_subscriptions':saab_mob,'Share' : saab_sch})
            new_saudiarabia_df.index = years
            st.line_chart(new_saudiarabia_df)

        elif country_choice == 'Egypt':
            egypt_df.index = years
            egypt_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(egypt_df)
            st.dataframe(egypt_df.corr())
            st.subheader('Correlation Matrix')
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
            new_egypt_df = pd.DataFrame({'PM2.5':egy_pol,'Internet_users':egy_int,'Broadcast':egy_bro,'Mobile_subscriptions':egy_mob,'Share':egy_sch})
            new_egypt_df.index = years
            st.line_chart(new_egypt_df)

        elif country_choice == 'Bangladesh':
            bangladesh_df.index = years
            bangladesh_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(bangladesh_df)
            st.subheader('Correlation Matrix')
            st.dataframe(bangladesh_df.corr())   
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
            new_bangladesh_df = pd.DataFrame({'PM2.5':ban_pol,'Internet_users':ban_int,'Broadcast':ban_bro,'Mobile_subscriptions':ban_mob,'Share':ban_sch})
            new_bangladesh_df.index = years
            st.line_chart(new_bangladesh_df)

        elif country_choice == 'China':
            china_df.index = years
            china_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(china_df)
            st.subheader('Correlation Matrix')
            st.dataframe(china_df.corr())
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
            new_china_df = pd.DataFrame({'PM2.5':chi_pol,'Internet_users':chi_int,'Broadcast':chi_bro,'Mobile_subscriptions':chi_mob,'Share':chi_sch})
            new_china_df.index = years
            st.line_chart(new_china_df)

        elif country_choice == 'Niger':
            niger_df.index = years
            niger_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(niger_df)
            st.subheader('Correlation Matrix')
            st.dataframe(niger_df.corr())
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
            new_niger_df = pd.DataFrame({'PM2.5':nig_pol,'Internet_users':nig_int,'Broadcast':nig_bro,'Mobile_subscriptions':nig_mob,'Share':nig_sch})
            new_niger_df.index = years
            st.line_chart(new_niger_df)

        elif country_choice == 'Iraq':
            iraq_df.index = years
            iraq_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(iraq_df)
            st.subheader('Correlation Matrix')
            st.dataframe(iraq_df.corr())
            iraq_pol = iraq_df['PM2.5']                       # taking data of the pollution
            iraq_int = iraq_df['Internet_users']              # taking data for the internet usage
            iraq_bro = iraq_df['Broadcast']                   # taking data for broadcast
            iraq_mob = iraq_df['Mobile_subscriptions']        # taking data for mobile subscriptions
            iraq_sch = iraq_df['Share']                       # taking data for share
            # now we want to find out the increment or decrement of each parameter
            iraq_pol = np.divide(iraq_pol,iraq_pol[0])
            iraq_int = np.divide(iraq_int,iraq_int[0])
            iraq_mob = np.divide(iraq_mob,iraq_mob[0])
            iraq_sch = np.divide(iraq_sch,iraq_sch[0])
            new_iraq_df = pd.DataFrame({'PM2.5':iraq_pol,'Internet_users':iraq_int,'Mobile_subscriptions':iraq_mob,'Share':iraq_sch})
            new_iraq_df.index = years
            st.line_chart(new_iraq_df)
            # since the increments of broadcast parameter hides the other increments, firstly this parameter is hidden and with this button we unhide it
            iraq_button = st.button('Graph with Broadcast parameter')
            if iraq_button:
                iraq_pol = np.divide(iraq_pol,iraq_pol[0])
                iraq_int = np.divide(iraq_int,iraq_int[0])
                iraq_bro = np.divide(iraq_bro,iraq_bro[0])
                iraq_mob = np.divide(iraq_mob,iraq_mob[0])
                iraq_sch = np.divide(iraq_sch,iraq_sch[0])
                new_iraq_df = pd.DataFrame({'PM2.5':iraq_pol,'Internet_users':iraq_int,'Broadcast':iraq_bro,'Mobile_subscriptions':iraq_mob,'Share':iraq_sch})
                new_iraq_df.index = years
                st.line_chart(new_iraq_df)

        else:
            pakistan_df.index = years
            pakistan_df.index.name = "Year"
            st.subheader('The dataset')
            st.dataframe(pakistan_df)
            st.subheader('Correlation Matrix')
            st.dataframe(pakistan_df.corr())
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
            new_pakistan_df = pd.DataFrame({'PM2.5':pak_pol,'Internet_users':pak_int,'Broadcast':pak_bro,'Mobile_subscriptions':pak_mob,'Share':pak_sch})
            new_pakistan_df.index = years
            st.line_chart(new_pakistan_df)         

#############################################################################################################################################
#       NOW WE WANT TO MAKE SOME PREDICTION FROM THE DATA WE HAVE
#############################################################################################################################################

with model_training:
    st.header('Can we predict the value of PM 2.5?')
    #st.text('Some text, its a description')
    model_button = st.checkbox('Train model')
    if model_button == True:       # we can see the new database for each country
        country_choice_2 = st.selectbox('Select Country',['Nepal','India','Qatar','Saudi Arabia','Egypt','Bangladesh','China','Niger','Iraq','Pakistan'])
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

        if country_choice_2 == 'Nepal':
            y = nepal_df['PM2.5']
            X =[nepal_df['Broadcast'],nepal_df['Internet_users'],nepal_df['Mobile_subscriptions'],nepal_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'India':
            y = india_df['PM2.5']
            X =[india_df['Broadcast'],india_df['Internet_users'],india_df['Mobile_subscriptions'],india_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'Qatar':
            y = qatar_df['PM2.5']
            X =[qatar_df['Broadcast'],qatar_df['Internet_users'],qatar_df['Mobile_subscriptions'],qatar_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'Saudi Arabia':
            y = saudiarabia_df['PM2.5']
            X =[saudiarabia_df['Broadcast'],saudiarabia_df['Internet_users'],saudiarabia_df['Mobile_subscriptions'],saudiarabia_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'Egypt':
            y = egypt_df['PM2.5']
            X =[egypt_df['Broadcast'],egypt_df['Internet_users'],egypt_df['Mobile_subscriptions'],egypt_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'Bangladesh':
            y = bangladesh_df['PM2.5']
            X =[bangladesh_df['Broadcast'],bangladesh_df['Internet_users'],bangladesh_df['Mobile_subscriptions'],bangladesh_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'China':
            y = china_df['PM2.5']
            X =[china_df['Broadcast'],china_df['Internet_users'],china_df['Mobile_subscriptions'],china_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'Niger':
            y = niger_df['PM2.5']
            X =[niger_df['Broadcast'],niger_df['Internet_users'],niger_df['Mobile_subscriptions'],niger_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        elif country_choice_2 == 'Iraq':
            y = iraq_df['PM2.5']
            X =[iraq_df['Broadcast'],iraq_df['Internet_users'],iraq_df['Mobile_subscriptions'],iraq_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)

        else:
            y = pakistan_df['PM2.5']
            X =[pakistan_df['Broadcast'],pakistan_df['Internet_users'],pakistan_df['Mobile_subscriptions'],pakistan_df['Share']]
            X = np.transpose(X) # transpose so input vectors
            X = np.c_[X, np.ones(X.shape[0])]  # add bias term
            linreg = np.linalg.lstsq(X, y, rcond=None)[0]
            fig = plt.figure()
            years_lin_reg = ['2017','2019','2020','2021','2022']
            plt.scatter(years,y)
            plt.scatter(years_lin_reg,linreg,c='red')
            plt.plot(years,y)
            plt.plot(years_lin_reg,linreg,c='red')
            plt.xlabel("Year")
            plt.ylabel("PM 2.5")
            plt.title('PM 2.5 forecast')
            st.write(fig)