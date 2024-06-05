
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

mycursor.execute("SELECT State_UT, (sum(Married_couples_1_Households+Married_couples_2_Households+Married_couples_3_Households+Married_couples_3_or_more_Households+Married_couples_4_Households+Married_couples_5__Households+Married_couples_None_Households)*100)/sum(Household_size_1_person_Households+Household_size_2_persons_Households+Household_size_1_to_2_persons+Household_size_3_persons_Households+Household_size_3_to_5_persons_Households+Household_size_4_persons_Households+Household_size_5_persons_Households+Household_size_6_8_persons_Households+Household_size_9_persons_and_above_Households) As percentage FROM census_db.census Group By state_ut")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The percentage of married couples with different household sizes in each state")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))




























