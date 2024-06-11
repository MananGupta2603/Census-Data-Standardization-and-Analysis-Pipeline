
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
    !pip install sqlalchemy"
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
* **Note:** The [main.ipynb](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/main.ipynb) file contains the first four tasks.
 
## Save Data Into MongoDB 

* [Task5.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/task5.py)
  
## Fetch data from MongoDB and upload it to MySQL.

* [Task6.py](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/task6.py)

## Data Analysis

* **Task 7:** Run Query on the database and show output on streamlit
    * **Note:** To run Query on streamlit write:
      
             streamlit run file_name.py
    * [Task 7]
        * 1)What is the total population of each district?
            * [Task7.1](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L30-L34)
        * 2)How many literate males and females are there in each district?
            * [Task7.2](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L35-L40)
        * 3)What is the percentage of workers (both male and female) in each district?
            * [Task7.3](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L41-L47)
        * 4)How many households have access to LPG or PNG as a cooking fuel in each district?
          * [Task7.4](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L48-L53)
        * 5)What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?
          * [Task7.5](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L54-L68)
        * 6)How many households have internet access in each district?
          * [Task7.6](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L69-L74)
        * 7)What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?
          * [Task7.7](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L75-L82)
        * 8)How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?
          * [Task7.8](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L83-L89)
        * 9)What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?
          * [Task7.9](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L93-L103)
        * 10)How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?
          * [Task7.10](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L104-L114)
        * 11)What is the total number of households in each state?
          * [Task7.11](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L117-L122)
        * 12)How many households have a latrine facility within the premises in each state?
          * [Task7.12](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L123-L131)
        * 13)What is the average household size in each state?
          * [Task7.13](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L132-L147)
        * 14)How many households are owned versus rented in each state?
          * [Task7.14](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L148-L155)
        * 15)What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?
          * [Task7.15](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L156-L166)
        * 16)How many households have access to drinking water sources near the premises in each state?
          * [Task7.16](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L167-L175)
        * 17)What is the average household income distribution in each state based on the power parity categories?
          * [Task7.17](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L176-L193)
        * 18)What is the percentage of married couples with different household sizes in each state?
          * [Task7.18](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L194-L208)
        * 19)How many households fall below the poverty line in each state based on the power parity categories?
          * [Task7.19](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L209-L215)
        * 20)What is the overall literacy rate (percentage of literate population) in each state?
          * [Task7.20](https://github.com/MananGupta2603/Census-Data-Standardization-and-Analysis-Pipeline/blob/main/sql.py#L216-L224)
        
