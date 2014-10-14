#------------------------------------------------------------------------------
#           Name: string_split.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to split a string into
#                 tokens based on some delimiter like a comma.
#------------------------------------------------------------------------------

str = "one,two,three,four,five"

print( "String = " + str )
print

tokens = str.split( ',' )

for i in range( len(tokens) ):
    print( "token %d = %s" % ( i, tokens[i] ) )

raw_input( '\n\nPress Enter to exit...' )
