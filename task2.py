import streamlit as st
import pandas as pd

df=pd.read_csv("census-2011.csv")

#---------covert old name to new name----------
p=df.drop_duplicates(subset='State name')
new_column=[]
old_column=[]

for i in p['State name']:
    old_column.append(i)
    temp=i.split()
    l=[]
    for j in temp:
        if j == 'AND' or j == 'and':
            l.append(j.lower())
        else:
            l.append(j.lower().capitalize())
    new_column.append(" ".join(l))

#-----------------change state name ------------------------------
for k in range(len(new_column)):
    df.replace(to_replace=old_column[k],value=new_column[k],inplace=True)


st.write(df)
