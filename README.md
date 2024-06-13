Census Data Standardization and Analysis Pipeline

A streamlined process for cleaning, processing, and analyzing census data to ensure uniformity, accuracy, and accessibility for further analysis and visualization.

Table of Contents

Overview

Installation

Data Processing Workflow

Data Storage

Data Analysis

Contributing

License

Overview

This project involves:

Data Acquisition: Retrieving census data from various sources.

Data Cleaning and Standardization: Renaming columns, handling missing data, and normalizing state/UT names.

Data Transformation: Creating new features and scaling data for analysis.

Data Storage: Storing processed data securely in databases.

Data Analysis: Efficiently retrieving and analyzing data subsets.

Installation

Install the necessary libraries using the following command:

sh

Copy code

pip install pandas mysql.connector.python streamlit pymongo[srv] sqlalchemy tabulate

Note: Remove the ! sign if running these commands in a command prompt.

Data Processing Workflow

Tasks

Rename Columns: Task1.py

Rename State/UT Names: Task2.py

Handle New State Formations:

Andhra Pradesh to Telangana: Task3\_1.py

Jammu and Kashmir to Ladakh: Task3\_2.py

Process Missing Data: Task4.py

Save Data Into MongoDB: Task5.py

Fetch Data from MongoDB and Upload to MySQL: Task6.py

Detailed implementation can be found in main.ipynb.

Data Storage

MongoDB

Save cleaned data into MongoDB using Task5.py.

MySQL

Fetch data from MongoDB and upload it to MySQL using Task6.py.

Data Analysis

Run queries on the database and display results using Streamlit:

sh

Copy code

streamlit run file\_name.py

Example Queries

Total population of each district: Query

Literate males and females in each district: Query

Percentage of workers in each district: Query

Households with access to LPG/PNG: Query

Religious composition of each district: Query

More queries are available in the SQL script.

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

License

This project is licensed under the MIT License.
