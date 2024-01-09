''' Import all the required libraries '''
import pandas as pd
import os

''' Create variables for input and output location --- Replace 'File_path' with the actual file path you wish to grab and store files from and to'''
input_loc = "/File_path/"
output_loc = "/File_path/"

''' Create variable for list of input files '''
fileList = os.listdir(input_loc)
fileList

''' Consolidate the files using for loop '''
finalDf = pd.DataFram()

for file in fileList:
	if file.endswith(".xls"):
		df = pd.read_excel(input_loc+file)
		finalDf = finalDf.append(df)

finalDf.to_excel(output_loc+"Airbnb_Data.xls")
