
# Census Data Standardization and Analysis Pipeline

This project aims to clean, process and analyzing census data. Standardization ensures data uniformity, accuracy, and accessibility of the census data for further analysis and visualization.

**Key functionalities:**

 * **1)Data Acquisition:** The pipeline will retrieve census data from the designated source. This might involve handling different data formats.

* **2)Data Cleaning:**
   * **Renaming:** Rename columns to consistent and meaningful names across datasets.
  * **Missing Data Handling:** Address missing values through imputation techniques (e.g., mean or percentage filling) or removal based on specific rules.

* **3)Data Standardization:**
  * **State/UT Name Normalization:** Standardize state and union territory (UT) names to a consistent format (e.g., changing name or remove spaces).
  * **New State/UT Formation Handling:** Account for newly formed states or UTs by incorporating them into the data structure or mapping them to existing entities.

* **4)Data Transformation:** Create new features or derived variables if necessary for analysis.Perform scaling or normalization to ensure features are on a similar scale.

* **5)Data Storage:** Choose a suitable storage solution for the cleaned and processed data based on project requirements (e.g., relational database, MongoDB, CSV files).Implement secure data storage practices.

* **6)Database Connection and Querying:** Establish a connection to the database storage system.Develop functions or queries to efficiently retrieve specific data subsets for analysis.
## Libraries To Install
    !pip install pandas
    !pip install mysql.connector.python
    !pip install streamlit
    !python -m pip install "pymongo[srv]"
**Note:** If you are running this commands in cmd[Command prompt], so remove this (!) sign.

## Data Cleaning,Modifying and Processing
* **Task 1:** Rename the Column names
    * [Task1.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/task1.py)

* **Task 2:**  Rename State/UT Names
    * [Task2.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/task2.py)

* **Task 3:** New State/UT formation
    * [Task3](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/tree/main/Task%203)
        * **Task 3.1:** Rename the State/UT From **“Andhra Pradesh”** to **“Telangana”**
            * [Task3_1.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%203/task3_1.py)
        * **Task 3.2:** Rename the State/UT From **“Jammu and Kashmir”** to **“Ladakh”**
            * [Task3_2.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%203/task3_2.py)

* **Task 4:** Find and process Missing Data
    * [Task4.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/task4.py)
## Storing Cleaned Census Data with MongoDB 

* [Task5.ipynb](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/task5.ipynb)

## SQL 

* **Task 7:** Run Query on the database and show output on streamlit
    * **Note:** To run Query on streamlit write:
      
             streamlit run file_name.py
        
    * [Task 7](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/tree/main/Task%207)
        * 1)What is the total population of each district?

            * [Task7.1.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/Task7.1.py)
        * 2)How many literate males and females are there in each district?

            * [Task7.2.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.2.py)
        * 3)What is the percentage of workers (both male and female) in each district?
            * [Task7.3.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.3.py)
        * [Task7.4.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.4.py)
        * [Task7.5.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.5.py)
        * [Task7.6.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.6.py)
        * [Task7.7.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.7.py)
        * [Task7.8.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.8.py)
        
## Documentation

[Documentation](https://linktodocumentation)

