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

mycursor.execute('''SELECT State_UT,SUM(CASE WHEN Ownership_Owned_Households = 'Y' THEN 1 ELSE 0 END) AS Households_Owned,SUM(CASE WHEN Ownership_Rented_Households = 'Y' THEN 1 ELSE 0 END) AS Households_Rented FROM census_db.census GROUP BY State_UT;
''')

out=mycursor.fetchall()

df=pd.DataFrame(out,columns=[i[0]for i in mycursor.description])

st.header("Households are owned versus rented in each state")
st.table(df)

# print(tabulate(out,headers=[i[0] for i in mycursor.description],tablefmt='psql'))



