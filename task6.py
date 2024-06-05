import pandas as pd
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mananngupta:manan123@cluster0.0o5bzkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#------------ upload data------
client=MongoClient("mongodb+srv://mananngupta:manan123@cluster0.0o5bzkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").census_db.census
#-------------------------------
census_data=pd.read_csv("Clean_Data\Clean_Data.csv")
census_dict=census_data.to_dict("records")
# client.insert_many(census_dict)

#------to print data----------
result=client.find({},{"_id":False})
data=list(result)
df=pd.DataFrame(data)
st.header("Main_Data")
st.table(df)

