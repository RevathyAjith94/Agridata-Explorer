import pandas as pd

#Load the dataset
#----------------------------------
df =pd.read_csv("D:\Agridata_Explorer\data\ICRISAT-District Level Data.csv")

print("Data load successfully")
print(df.head())
print(df.info())

#---------------------------------------
#  Data Cleaning
#---------------------------------------
# 1 Drop columns that are fully empty
df.dropna(axis=1, how='all', inplace = True)

# 2 Replace missing value (NaN) with 0
df.fillna(0, inplace = True)

# 3 Save cleaned data
df.to_csv("D:/Agridata_Explorer/data/Cleaned_data.csv", index = False)

print("Cleaning Completed Cleaned file saved as Cleaned_data.csv")