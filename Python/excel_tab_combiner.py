import pandas as pd

# Load the Excel file
file_path = 'My Excel.xlsx'  # Replace with your file path
excel_file = pd.ExcelFile(file_path)

# Initialize a list to store the DataFrames
dfs = []

# Loop through each sheet and append the data to the list
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df['SheetName'] = sheet_name  # Add a new column with the sheet name
    dfs.append(df)

# Concatenate all the DataFrames in the list
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined data to a CSV file
combined_df.to_csv('my_combined_file.csv', index=False)
