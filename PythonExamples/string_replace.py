#------------------------------------------------------------------------------
#           Name: string_replace.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to replace string
#------------------------------------------------------------------------------

str = 'one two three four'

print( "Before: " + str )

str = str.replace( 'one', '1' )
str = str.replace( 'two', '2' )
str = str.replace( 'three', '3' )
str = str.replace( 'four', '4' )

print( "After: " +  str )

raw_input( '\n\nPress Enter to exit...' )
