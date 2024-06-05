
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
#--Set-- power_perity=90000

mycursor.execute("SELECT State_UT,sum(Power_Parity_Less_than_Rs_45000+Power_Parity_Rs_45000_90000) As Households_fall_below_the_poverty_line  FROM census_db.census Group By state_ut")

out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("Households fall below the poverty line in each state ")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))




























