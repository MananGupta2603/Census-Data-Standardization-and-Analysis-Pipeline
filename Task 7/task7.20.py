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

mycursor.execute("SELECT State_UT, (sum(Literate)*100/762536936) As percentage_of_literate_population  FROM census_db.census Group By state_ut")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("the overall literacy rate (percentage of literate population) in each state?")
st.table(df)


# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))


