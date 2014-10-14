#------------------------------------------------------------------------------
#           Name: string_to_array.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to modify a string by
#                 converting it to an array
#------------------------------------------------------------------------------

import array

str = 'My name is Jigar'

print( 'String = ' + str )

# We're not allowed to modify strings so we'll need to convert it to a
# character array instead...

charArray        = array.array( 'B', str )     # assignment
charArray[11:16] = array.array( 'B', 'Mistry' ) # replacement

str = charArray.tostring() # assignment back to the string object
print charArray
print( 'str = ' + str )

raw_input( '\n\nPress Enter to exit...' )
