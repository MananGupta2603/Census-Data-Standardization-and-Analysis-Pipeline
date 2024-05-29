import streamlit as st
import pandas as pd

df=pd.read_excel("census_2011.xlsx")
change_state_name=[
'Adilabad',
'Nizamabad',
'Karimnagar',
'Medak',
'Hyderabad',
'Rangareddy',
'Mahbubnagar',
'Nalgonda',
'Warangal',
'Khammam'
]
a=df[df['District name'].isin(change_state_name)]
st.write(a)

df.loc[df['District name'].isin(change_state_name),'State name'] = 'Telangana'

df[df['District name'].isin(change_state_name)]
