import pandas as pd
import os

input_path = "/File_path/"
output_path = "/File_path/New_Workbook.xlsx"

files = os.listdir(input_path)
combined_data = pd.DataFrame()  # Initialize an empty DataFrame to store combined data
sheet_counter = 1

with pd.ExcelWriter(output_path) as writer:
    for file in files:
        if file.endswith(".xls"):
            sheet_name = "Sheet" + str(sheet_counter)
            data = pd.read_excel(os.path.join(input_path, file))  # Read each Excel file
            combined_data = pd.concat([combined_data, data], ignore_index=True)  # Concatenate data
            data.to_excel(writer, sheet_name=sheet_name, index=False)  # Write each sheet to the combined workbook
            sheet_counter += 1
