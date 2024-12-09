import os
import pandas as pd

def scan_directory(root_folder, output_csv):
    # Initialize an empty list to store file and directory information
    records = []

    # Recursive function to process files and directories
    def process_folder(folder, parent_name):
        for entry in os.scandir(folder):
            if entry.is_file():
                records.append({
                    "File or Directory Name": entry.name,
                    "Type": "File",
                    "File Size": entry.stat().st_size,
                    "Parent Name": parent_name
                })
            elif entry.is_dir():
                records.append({
                    "File or Directory Name": entry.name,
                    "Type": "Directory",
                    "File Size": 0,
                    "Parent Name": parent_name
                })
                # Drill down into the directory
                process_folder(entry.path, entry.name)

    # Start processing the root folder
    process_folder(root_folder, os.path.basename(root_folder))

    # Convert the records into a DataFrame
    df = pd.DataFrame(records, columns=["File or Directory Name", "Type", "File Size", "Parent Name"])

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    print(f"Data saved to {output_csv}")

# Define the root folder to scan and the output CSV file
root_folder = r".\myfolder"  # Replace with your folder path
output_csv = r".\output.csv"    # Replace with your desired CSV output path

# Execute the script
scan_directory(root_folder, output_csv)
