import streamlit as st
import pandas as pd
import numpy as np

st.title('Explorative Data Analysis for Police Activity with Rhode Island dataset')

police_data = "./police.csv"
weather_data = "./weather.csv"

@st.cache
def load_data(path,nrows=10000):
    data = pd.read_csv(path, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
  

data_load_state = st.text('Loading Police Activity data...')
p_data = load_data(police_data,50000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(p_data)

