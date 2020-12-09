#!/usr/bin/env python3
#
# Script to merge multiple DBCs
#

import os
import cantools

#Provide file names for the DBC files which are to be merged. 
#Store input DBC files in same folder of the script location.
dbc_files = ['abc.dbc', xyz.dbc']
INPUT_DBC_PATH = []    

#Get relative path of the script   
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
#Get relative path for the merged output dbc file 'MergedCAN.dbc'
OUTPUT_DBC_PATH = os.path.join(SCRIPT_DIR, 'MergedCAN.dbc')

print("Writing modified DBC database to '{}'.".format(OUTPUT_DBC_PATH))
#Create a database 
db = cantools.db.Database()

#Append rest of DBC files to dbc component
for file in range(len(dbc_files)):
    #Get relative path of the input dbc files
    INPUT_DBC_PATH.append(os.path.join(SCRIPT_DIR, dbc_files[file]))
    print("Adding DBC database from '{}'.".format(INPUT_DBC_PATH[file]))
    #Append dbc component to the database
    db.add_dbc_file(INPUT_DBC_PATH[file], encoding='cp1252')
    
#Write dbc component to output dbc
with open(OUTPUT_DBC_PATH, 'w', newline="\r\n") as fout:
    fout.write(db.as_dbc_string())

#Refresh the database
db.refresh()   