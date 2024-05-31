
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

    !pip install tabulate
**Note:** If you are using vs code to run codes, so you can install this to display your DB(database) data in table formate inside vs code. 
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

## Data Analysis

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
        * 4)How many households have access to LPG or PNG as a cooking fuel in each district?
          * [Task7.4.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.4.py)
        * 5)What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?
          * [Task7.5.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.5.py)
        * 6)How many households have internet access in each district?
          * [Task7.6.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.6.py)
        * 7)What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?
          * [Task7.7.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.7.py)
        * 8)How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?
          * [Task7.8.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.8.py)
        * 9)What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?
          * [Task7.9.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.9.py)
        * 10)How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?
          * [Task7.10.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.10.py)
        * 11)What is the total number of households in each state?
          * [Task7.11.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.11.py)
        * 12)How many households have a latrine facility within the premises in each state?
          * [Task7.12.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.12.py)
        * 13)What is the average household size in each state?
          * [Task7.13.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.13.py)
        * 14)How many households are owned versus rented in each state?
          * [Task7.14.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.14.py)
        * 15)What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?
          * [Task7.15.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.15.py)
        * 16)How many households have access to drinking water sources near the premises in each state?
          * [Task7.16.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.16.py)
        * 17)What is the average household income distribution in each state based on the power parity categories?
          * [Task7.17.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.17.py)
        * 18)What is the percentage of married couples with different household sizes in each state?
          * [Task7.18.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.18.py)
        * 19)How many households fall below the poverty line in each state based on the power parity categories?
          * [Task7.19.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.19.py)
        * 20)What is the overall literacy rate (percentage of literate population) in each state?
          * [Task7.20.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/Task%207/task7.20.py)

        
