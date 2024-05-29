import streamlit as st
import pandas as pd

df=pd.read_excel("census_2011.xlsx")
change_state_name=[
'Leh(Ladakh)',
'Kargil'
]
a=df[df['District name'].isin(change_state_name)]
st.write(a)

df.loc[df['District name'].isin(change_state_name),'State name'] = 'Ladakh'

df[df['District name'].isin(change_state_name)]
