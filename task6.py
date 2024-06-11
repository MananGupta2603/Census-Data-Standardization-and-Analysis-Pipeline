from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine


# MongoDB connection details
mongo_uri = "mongodb+srv://mananngupta:manan123@cluster0.0o5bzkc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
database_name = "census_db"
collection_name = "census"

# Establishing connection to MongoDB
try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=20000)
    db = client[database_name]
    collection = db[collection_name]
    # Fetching data from MongoDB
    mongo_data = list(collection.find({}))
    print("Connected to MongoDB and fetched data successfully")
except :
    print("Failed")
    exit(1)


# Transforming data
df = pd.DataFrame(mongo_data)
if '_id' in df.columns:
    df = df.drop(columns=['_id'])

# dictionary to renameing columns which length are more than 65
column_rename_map = {
    'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car': 'Households_TV_Computer_Laptop_Telephone_mobile_phone_Scooter_Car',
    #----------------------------
    'Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households':'Type_of_latrine_facility_Night_soil_disposed_into_open_drain',
    #----------------------------
    'Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households':'Type_of_latrine_Flush_pour_connected_to_other_system_Households',
    #----------------------------
    'Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households':'Not_having_latrine_within_premises_Other_source_Open_Households',
    #----------------------------
    'Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households':'Source_of_drinking_water_Handpump_Tubewell_Borewell_Households',
    #----------------------------
    'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households':'Drinking_water_Spring_River_Canal_Tank_Pond_Lake_Other_Household'
    
}

df = df.rename(columns=column_rename_map)

# Relational database connection details
db_type = 'mysql'  
user = 'root'
password = ''
host = 'localhost'
port = '3306'
database = 'census_db'


# Creating a connection string and engine
connection_string = f"{db_type}+mysqldb://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# Uploading data to the relational database
table_name = 'census'
df.to_sql(table_name, engine, if_exists='replace', index=False)
print("Data uploaded to the relational database successfully")
