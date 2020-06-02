#!/usr/bin/python3
###############################################################################
#   \brief: the purpose of this basic program is to format SQL code by 
#           replacing the words in the sql file with the ones in the 
#           dictionary and outputting to a new file
###############################################################################
import argparse
from argparse import ArgumentParser

keywords = {
    'select' : 'SELECT',
    'from' : 'FROM',
    'where' : 'WHERE',
    'and': 'AND',
    'or' : 'OR',
    'not': 'NOT',
    'in' : 'IN',
    'order by': 'ORDER BY',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'insert into': 'INSERT INTO',
    'create database': 'CREATE DATABASE',
    'alter database': 'ALTER DATABASE',
    'create table': 'CREATE TABLE',
    'alter table': 'ALTER TABLE',
    'drop table': 'DROP TABLE',
    'create index': 'CREATE INDEX',
    'drop index': 'DROP INDEX'
    # more to be added ...
}
#*****************************************************************************#
def init_args():
    
    """
    @brief          - function containing user args to be passed at run time
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r', encoding='UTF-8'), 
                        required=True,
                        help='argument for the input file')
    args = parser.parse_args()
    return args
#*****************************************************************************#
def convert_file(filename):

    """
    @brief          - function to perform the conversion
    """
    outfile = "converted.sql"
    # open input file
    with open(filename, 'r') as file:
        # open output file, create one if file DNE using 'w+'
        with open(outfile, 'w+') as output:
            inp_file = file.read()                  # read the file
            for k,v in keywords.items():            # iterate through the dict
                inp_file = inp_file.replace(k,v)    # replace the k,v pairs
            output.write(inp_file)                  # output results to file
#*****************************************************************************#
if __name__ == "__main__":
    
    user_args = init_args()
    infile = user_args.file.name

    if infile:
        convert_file(infile)
        print('Conversion done successfully!')
    else:
        print(f"File {infile} does not exist!")
