''' Import all the required libraries '''
import pandas as pd
import os

''' Create variables for input and output location --- Replace 'File_path' with the actual file path you wish to grab and store files from and to'''
path = "/File_path/"
output_path = "/File_path/"

files = os.listdir(path)

''' Initialize an empty list to store individual DataFrames '''
df_list = []

''' Consolidate the files using for loop '''
for file in files:
    if file.endswith(".xls"):
        data = pd.read_excel(os.path.join(path, file)) 
        df_list.append(data)

''' Concatenate all DataFrames in the list '''
final_df = pd.concat(df_list, ignore_index=True)

''' Save the concatenated DataFrame to an Excel file -- REPLACE the file name with the file name you are using'''
final_df.to_excel(os.path.join(output_path, "Airbnb_Data.xlsx"), index=False)
