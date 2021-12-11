# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:52:31 2021

@author: togneva
"""

# Add dependencies
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

   # Read the file object with the reader function.
   file_reader = csv.reader(election_data)

   # Print the header row.
   headers = next(file_reader)
   print(headers)
   
    
   

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
    txt_file.write("Counties in the Election\
                   \n-------------------------\
                   \nArapahoe\nDenver\nJefferson")