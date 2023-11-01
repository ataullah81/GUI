# Define the file paths for the two text files
file1_path = 'D:\Temp\pak_20231025122231_new.txt'
file2_path = 'D:\Temp\pak_202304032359.txt'

# Read the contents of the two text files
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    lines_file1 = file1.readlines()
    lines_file2 = file2.readlines()

# Find the lines that are in file1 but not in file2
missing_lines = [line for line in lines_file1 if line not in lines_file2]

# Write the missing lines to a separate file
with open('D:\Temp\missing_lines.txt', 'w') as output_file:
    output_file.writelines(missing_lines)
