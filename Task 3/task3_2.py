import streamlit as st
import pandas as pd

df=pd.read_csv("census-2011.csv")
change_state_name=[
'Leh(Ladakh)',
'Kargil'
]
a=df[df['District name'].isin(change_state_name)]
st.write(a[['State name','District name']])

df.loc[df['District name'].isin(change_state_name),'State name'] = 'Ladakh'

b=df[df['District name'].isin(change_state_name)]
st.write(b[['State name','District name']])