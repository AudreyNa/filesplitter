import pandas as pd
import os
import shutil

# Read the Excel file
excel_file = 'ddi_metadata_modified.xlsx'  # Adjust the file name and path
df = pd.read_excel(excel_file)

# Path to the folder containing all the image files
images_folder = r"C:\Users\audre\Downloads\validation"

# Create folders for each label
for label in df['label'].unique():
    os.makedirs(label, exist_ok=True)

# Move images to the corresponding folders
for index, row in df.iterrows():
    filename = row['filename']
    source_path = os.path.join(images_folder, filename)
    destination_path = os.path.join(row['label'], filename)
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print("exists")
    else:
        print("1")
print("done")