""" To run, enter the directory name containing all the files whose box positions and numbers you want to get and also the output file name
    Example: python3 file_directory output_file.csv
"""

import sys
import os

original_stdout = sys.stdout # init original standard output

files_list = os.listdir(sys.argv[1])  # list of files
abs_path_dir = os.path.abspath(sys.argv[1])# get absolute path for the directory entered
output_file = sys.argv[2] # output file

# for file in files_list: # loop through the file list getting the absolute path and adding thm to the file path list
    # file_path_list.append(os.path.abspath(file.replace(' ', '\ '))) # replacing so that the script can understand spaces in the file path (putting "\ " at places where we have spaces)

def print_and_output_columns(files): # function to print and output columns to file
    with open(output_file, 'w') as f: # open file to put outputs that are printed
        sys.stdout = f
    
        for file in files:
            with open(abs_path_dir + '/' + file, 'r') as f1:
                lines = f1.readlines() # read all lines
                for line in lines:      # loop through line by line             
                    if 'UG_PID' in line: # check if line is header or title line. (in all my files, 'UG_PID' is in the header)
                        columns = line.split(',')  # the for loop gets each row separated by comma
                        name_index = columns.index('UG_PID') # gets index of Name column
                        box_index = columns.index('Box') # gets index of Box column
                        continue  # skip to next iteration after processing header row
                    
                    columns = line.split(',') # the for loop gets each row separated by comma
                    print(columns[name_index], columns[box_index], columns[-1] , sep=",")  # prints selected columns using the indexes got columns
    sys.stdout = original_stdout  # set stdout back to original 

print_and_output_columns(files_list)