''' Import all the required libraries '''
import pandas as pd
import os

''' Create variables for input and output location '''
input_loc = "/Users/haleybengtson/Anatta Dropbox/Haley Bengtson/My Mac (anatta’s MacBook Pro)/Desktop/Airbnb Workbook/"
output_loc = "/Users/haleybengtson/Anatta Dropbox/Haley Bengtson/My Mac (anatta’s MacBook Pro)/Desktop/Airbnb Workbook Final/"

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
