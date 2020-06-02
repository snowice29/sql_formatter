#!/usr/bin/python3
###############################################################################
#   \brief: the purpose of this basic program is to format SQL code by 
#           replacing the words in the sql file with the ones in the 
#           dictionary and outputting to a new file
###############################################################################
keywords = {
    'select' : 'SELECT',
    'from' : 'FROM',
    'where' : 'WHERE',
    'in' : 'IN',
    'order by': 'ORDER BY'
    # more to be added ...
}

infile = 'test.sql'
outfile = 'converted.sql'

# open input file
with open(infile, 'r') as file:
    # open output file, create one if file DNE using 'w+'
    with open(outfile, 'w+') as output:
        inp_file = file.read()                  # read the file
        for k,v in keywords.items():            # iterate through the dict
            inp_file = inp_file.replace(k,v)    # replace the k,v pairs
        output.write(inp_file)                  # output results to file