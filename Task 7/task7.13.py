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

mycursor.execute("SELECT State_UT, AVG(Household_size_1_person_Households+ Household_size_2_persons_Households+ Household_size_1_to_2_persons+ Household_size_3_persons_Households+ Household_size_3_to_5_persons_Households+ Household_size_4_persons_Households+ Household_size_5_persons_Households+ Household_size_6_8_persons_Households+ Household_size_9_persons_and_above_Households) AS Average_household_size FROM census_db.census Group By state_ut")

out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The average household size in each state")
st.table(df)


# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))


