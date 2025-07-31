import pandas as pd
import numpy as np

# reading the dataset
# pd.read_csv("file_path")
df = pd.read_csv("data/airlines_flights_data.csv")


#Reading the first 5 rows of a dataframe
print(df.head())


#Reading first 100 rows of a dataframe using the head function
print(df.head(100))


#Reading the last 5 rows of a dataframe
print(df.tail())


#Reading the last 100 rows of a dataframe
print(df.tail(100))


#Describing the overall structure of the dataframe 
#it gives us the detailed information of a deatframe like count,mean,median,min,max values of each column in a dataframe
#Descriptive statistics of  numerical column of a dataframe
print(df.describe())
print(df.shape)


##Describing the string object column of a dataframe


str_desc = df["flight"].describe()
print(str_desc)

#reading using the loops
# rows , columns = df.shape

# for i in range(rows):
#     print(df[i])