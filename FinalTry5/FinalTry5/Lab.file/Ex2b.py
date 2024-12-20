import os

# File path to check
file_path = '/Users/linawegert/Documents/GitHub/Lab5.Dic/Lab.file/survey_1000.csv'

# Check if the file exists 
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    file_size = os.path.getsize(file_path)  # Get file size
    print(f"File '{file_path}' exists and is readable.")
    print(f"File size: {file_size} bytes")
else:
    print(f"File '{file_path}' does not exist or is not readable.")
