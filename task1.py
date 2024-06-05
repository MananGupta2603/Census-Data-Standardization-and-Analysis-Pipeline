
import streamlit as st
import pandas as pd

# ---------Task 1: Rename the Column names----------

df=pd.read_csv("Clean_Data\Clean_Data.csv")
temp=pd.read_csv("Original_Data\census-2011.csv")

change_column_name={
  'State name': 'State/UT',
  'District name': 'District',
  'Male_Literate': 'Literate_Male',
  'Female_Literate': 'Literate_Female',
  'Rural_Households': 'Households_Rural',
  'Urban_ Households': 'Households_Urban',
  'Age_Group_0_29': 'Young_and_Adult',
  'Age_Group_30_49': 'Middle_Aged',
  'Age_Group_50': 'Senior_Citizen',
  'Age not stated': 'Age_Not_Stated'
}
df.rename(columns=change_column_name,inplace=True)
st.write(df.columns)
st.write(temp.columns)


