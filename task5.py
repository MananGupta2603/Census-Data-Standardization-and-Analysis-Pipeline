import pandas as pd

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

#----creating census collection in test db---
client=MongoClient("mongodb+srv://mananngupta:manan123@cluster0.0o5bzkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").project.census
#------------------------------
#-------------------------------
census_data=pd.read_csv("Clean_Data\Clean_Data.csv")
census_dict=census_data.to_dict("records")
# client.insert_many(census_dict)
print("Data inserted successfully!")