
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
#--> how this code work ex--> state= ladakh, sum=41467 ,count=2(number of state) percentage= (41467*100)/2=2073350

mycursor.execute("SELECT State_UT, round((sum(Married_couples_1_Households+Married_couples_2_Households+Married_couples_3_Households+Married_couples_3_or_more_Households+Married_couples_4_Households+Married_couples_5__Households+Married_couples_None_Households)*100)/Count(state_ut),2) As percentage FROM census_db.census Group By state_ut")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The percentage of married couples with different household sizes in each state")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))




























