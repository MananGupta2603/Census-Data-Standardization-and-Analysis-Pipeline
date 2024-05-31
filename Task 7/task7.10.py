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
mycursor.execute("select District, Household_size_1_person_Households,Household_size_2_persons_Households,Household_size_1_to_2_persons,Household_size_3_persons_Households,Household_size_3_to_5_persons_Households,Household_size_4_persons_Households,Household_size_5_persons_Households,Household_size_6_8_persons_Households,Household_size_9_persons_and_above_Households from census_db.census")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The household size distributed ")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))


