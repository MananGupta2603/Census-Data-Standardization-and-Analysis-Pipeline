
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
mycursor.execute("SELECT State_UT,sum(Locationofdrinkingwatersource_Near_the_premises_Households) As Location_of_drinking_water_source_Near_the_premises_Households FROM census_db.census Group By state_ut")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("Households have access to drinking water sources near the premises in each state")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))















