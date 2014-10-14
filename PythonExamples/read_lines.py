#------------------------------------------------------------------------------
#           Name: read_lines.py
#         Author: Jigar Mistry
#  Last Modified: 05/08/2013
#    Description: This Python script demonstrates how to use fileinput to read
#                 each line of a given file.
#------------------------------------------------------------------------------

import fileinput

for line in fileinput.input( "test.txt" ):
    print line,

raw_input( '\n\nPress Enter to exit...' )
