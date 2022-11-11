#!/usr/bin/env python

import pandas as pd
from random import *
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-if", "--inputfile", dest = "inputfile", help="Input File as Csv")
parser.add_argument("-of", "--outputfile", dest = "outputfile", help="Output File as Csv")
parser.add_argument("-p", "--percentage", dest = "percentage", default = 10, help="Percentage")
parser.add_argument("-l", "--list", dest='list', action='store_true', help= "List")

args = parser.parse_args()

if(args.inputfile == None):
    print("Input File is Missing, use -if argument")
    sys.exit(0)
filepath = args.inputfile

df = pd.read_csv(filepath)

rows_count = len(df)
columns_count = len(df.columns)
total_missing_cells_count = df.isnull().sum().sum()
total_cells_count = df.count().sum()
current_percentage_of_missing_values = round(total_missing_cells_count/total_cells_count * 100, 2)

print("Total Number of Rows:",rows_count)
print("Total Number of Columns:",columns_count)
print("Total Number of Cells:",total_cells_count)
print("Total Number of Missing Value Cells:",total_missing_cells_count)
print("Percentage of Missing Value Cells :",current_percentage_of_missing_values,"%")

if(args.list is True):
    sys.exit(0)

if(args.outputfile == None):
    print("Output File is Missing, use -of argument")
    sys.exit(0)
output_file_name = args.outputfile 

if(args.percentage == None):
    print("Percentage is Missing, use -p argument")
    sys.exit(0)
percentage = args.percentage 

if(percentage.isnumeric() == False):
    print("Percentage should be a number")
    sys.exit(0)

percentage = int(percentage)

if(percentage < 0 or percentage >100):
    print("Percentage (",percentage,") should be within 0-100 range")
    sys.exit(0)

if(current_percentage_of_missing_values > percentage):
    print("Missing Velues Are Overfilled !!!")
    sys.exit(0)

number_of_cells_to_be_updated = (percentage/100*total_cells_count) - total_missing_cells_count;
print("Expected Percentage of Missing Value Cells :",percentage)
print("Number of Cells to be Updated :",number_of_cells_to_be_updated)

copied_df = df.copy(deep=True)
copied_total_cells = copied_df.count().sum()

while(True):
    copied_total_missing_cells = copied_df.isnull().sum().sum()
    copied_percentage = round(copied_total_missing_cells/copied_total_cells * 100,2)
    
    if(copied_percentage > percentage):
        break;

    rand_row = randint(1,rows_count-1)
    rand_column = randint(0,columns_count-1)

    if(pd.isnull(copied_df.iloc[rand_row,rand_column]) is not True):
        print("\r Missing Value Updated [Row:",rand_row, "\tColumn:",rand_column,"]\t Total Missing Cells:",copied_total_missing_cells,"\t Percentage (",copied_percentage,")")
        copied_df.iat[rand_row,rand_column] = np.nan


print("Process Completed, Output file will be saved on [",output_file_name,"]")
copied_df.to_csv(output_file_name)