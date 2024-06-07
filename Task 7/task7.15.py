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
mycursor.execute("SELECT State_UT,sum(Type_of_latrine_facility_Pit_latrine_Households) As Type_of_latrine_facility_Pit_latrine_Households,sum(Type_of_latrine_facility_Other_latrine_Households) AS Type_of_latrine_facility_Other_latrine_Households,sum(TypeoflatrinefacilityNightsoildisposedintoopendrainHouseholds) As Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households,sum(T_LatrineFac_FP_ConOtherSys_HH) As Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households FROM census_db.census Group By state_ut")
out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("The distribution of different types of latrine facilities")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))


