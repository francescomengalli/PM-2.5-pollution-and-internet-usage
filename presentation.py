#from locale import PM_STR
from pyexpat import features
import streamlit as st
import pandas as pd

global_pollution_df = pd.read_csv('PM2.5 Global Air Pollution 2010-2017.csv')
users_per_country_df = pd.read_csv('number-of-internet-users-by-country.csv')
broadband_df = pd.read_csv('broadband-penetration-by-country.csv')
mobile_sub_df = pd.read_csv('mobile-cellular-subscriptions-per-100-people.csv')
share_df = pd.read_csv('share-of-individuals-using-the-internet.csv')


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('PM 2.5 and Internet usage')
    st.text('Is there any correlation between pollution and using the Internet?')
    st.write('PM 2.5 indicates little pieces smaller than or equal to 2.5 micron (1/4 of the more famous PM 10)')
    first_button = st.button('Original database')
    second_button = st.button('New databases')


    if first_button == True:
        with dataset:
            st.title('Original databases')
            st.text('Here we can see the original databases')
            choice = st.selectbox('Select',['PM 2.5','Internet usage'])
            if choice == 'PM 2.5':
                with dataset:
                    st.text('We have data for all the countries around the world in the period 2010 - 2016')
                    first_choice = st.selectbox('Select',['Original dataset','First 10 polluting countries'])
                    if first_choice == 'Original dataset':
                        st.dataframe(global_pollution_df)

                    else:
                        st.dataframe(global_pollution_df.sort_values(by=['2010'], ascending = False).head(12))
            else:
                with dataset:
                    second_choice = st.selectbox('Select',['Broadband','Mobile subscriptions','Number of internet users','Share of individuals using the Internet'])
                    if second_choice == 'Broadband':
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
    if second_button == True:
        st.write('fenomeno')

with features:
    st.header('The featurese I created')
    button = st.button('Hit me')
    button_2 = st.button('Hit me again')
    if button == True:
        st.write('success')
    if button_2 == True:
        st.write('bravo')


with model_training:
    st.header('Time to train the model')
    st.text('Some text, its a description')