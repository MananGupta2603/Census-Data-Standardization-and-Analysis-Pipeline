
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
mycursor.execute("SELECT State_UT,AVG(Power_Parity_Less_than_Rs_45000 +Power_Parity_Rs_45000_90000 +Power_Parity_Rs_90000_150000+Power_Parity_Rs_45000_150000+ Power_Parity_Rs_150000_240000+Power_Parity_Rs_240000_330000+Power_Parity_Rs_150000_330000+Power_Parity_Rs_330000_425000+Power_Parity_Rs_425000_545000+Power_Parity_Rs_330000_545000+Power_Parity_Above_Rs_545000) As Average_household_income_distribution FROM census_db.census Group By state_ut")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The average household income distribution in each state based on the power parity categories")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))















