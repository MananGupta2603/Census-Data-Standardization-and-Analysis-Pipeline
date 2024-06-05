import streamlit as st
import pandas as pd

df=pd.read_csv("Original_Data\census-2011.csv")
st.header("Sum of Null Values in each column")
a=df.isnull().sum()
st.write(a)
st.divider()
st.dataframe(df)

st.header("After Filling Data")

# # Calculate a percentage of the initial sum of each column with missing values 
missing_initial = (df.isnull().mean() * 100).round(4)

#  # Fill missing values using the formula: 
df['Population'].fillna(df['Male'].fillna(0) + df['Female'].fillna(0),inplace=True)

df['Literate'].fillna(df['Male_Literate'].fillna(0) + df['Female_Literate'].fillna(0),inplace=True)
df['Population'].fillna(df['Age_Group_0_29'].fillna(0)+ df['Age_Group_30_49'].fillna(0) + df['Age_Group_50'].fillna(0) + df['Age not stated'].fillna(0),inplace=True)
df['Households'].fillna(df['Rural_Households'].fillna(0) + df['Urban_Households'].fillna(0),inplace=True )

# # Calculate a percentage of the final sum of each column after filling missing values
final_sum = (df.isnull().mean() * 100).round(4)


# Create a new DataFrame to display the results

new_df=pd.DataFrame({
'Before_filling%': missing_initial,
'After_filling%': final_sum
})
st.write(df)
st.header("Comparesion Of Both Dataes")
st.write(new_df) #transpose df
a=df.isnull().sum()
st.write(a)
