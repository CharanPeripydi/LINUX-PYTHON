import os
import shutil

#Define the path to the directory
directory = "."

#Get all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

#Organize files by type
for file in files:
    # Extract the file extension
    file_extension = file.split('.')[-1]
    folder_name = os.path.join(directory, file_extension)

    # Create a folder for each file type if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    #Move the file to the respective folder
    shutil.move(os.path.join(directory, file), os.path.join(folder_name, file))

print(f"Files in '{directory}' have been organized by type.")
