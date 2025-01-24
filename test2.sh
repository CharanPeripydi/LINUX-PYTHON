#!/bin/bash

# Create a directory and navigate into it
mkdir t2
cd t2

# Create files
touch file1.txt file2.jpg file3.py

# Open and edit a Python file (this step requires manual input in nano)
nano org_files.py

# List all files in the directory
ls

# Run the Python script
python3 org_files.py

# Check organized files
ls txt
ls jpg
ls py

# Install the tree command
sudo apt install tree -y

# Display directory structure using tree
tree
