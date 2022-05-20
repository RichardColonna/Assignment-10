import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data by Richard Colonna')
df = pd.read_csv('housing.csv')

st.subheader('See more filters in the sidebar:')

Value_filter = st.slider(('Median House Price'), 0.00, 500001.00, 200000.00)

st.map(df)

p_filter = st.sidebar.multiselect(
    'Choose location',
    df.ocean_proximity.unique())

df=df[df.median_house_value <= value_filter]
df=df[df.df.ocean_proximity.isin(p_filter)]
      
income_filter= st.sidebar.radio(
    'Choose Income Status',
    ('Low','Medium','High'))

if income_filter =='Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]
    
st.subheader('Histogram of Median Values')

fig,ax = plt.subplots()
df.median_house_value.hist(ax = ax, bins = 30)

st.pyplot(fig)