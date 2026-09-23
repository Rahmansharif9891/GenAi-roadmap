
import pandas as pd
df = pd.read_csv("patient.csv", sep="\t")

# print(df.head())    # Display the first 5 rows of the DataFrame

# print(df.info())    # Display information about the DataFrame, including data types and non-null counts

# print(df.describe())  # Display summary statistics for numerical columns in the DataFrame

# print(df.isnull().sum())  # Display the count of missing values for each column in the DataFrame

# print(df.duplicated().sum())  # Display the count of duplicate rows in the DataFrame

# print(df['age'].unique())  # Display the unique values in the 'age' column of the DataFrame

# print(df['age'].value_counts())  # Display the count of each unique value in the 'age' column of the DataFrame

print(df.dropna()) # remove duplicate values

print(df.info())