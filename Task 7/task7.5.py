import mysql.connector
import streamlit as st
import pandas as pd

#-------------------------------------
mydb=mysql.connector.connect(
host="localhost",
user="root",
password=""
)
mycursor=mydb.cursor(buffered=True)
#-------------------------------------
mycursor.execute("select District,((Hindus)+(Muslims)+(Christians)+(Sikhs)+(Buddhists)+(Jains))As Religion_Composition from census_db.census")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("Religion_Composition(Hindus,Muslims,Sikhs,Buddhists,Jains)")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))


