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
mycursor.execute("select District, Condition_of_occupied_census_houses_Dilapidated_Households,Households_with_separate_kitchen_Cooking_inside_house,Having_bathing_facility_Total_Households,Having_latrine_facility_within_the_premises_Total_Households from census_db.census")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The condition of occupied census houses ")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))


