#------------------------------------------------------------------------------
#           Name: search_and_replace.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to perform a
#                 search-and-replace on a file.
#------------------------------------------------------------------------------

import os
import sys
import fileinput

print "Text to search for:"
textToSearchFor = raw_input( "> " )

print "Text to replace it with:"
textToReplaceWith = raw_input( "> " )

print "File to perfrom search-and-replace on:"
fileToSearch  = raw_input( "> " )

oldFileName  = 'old_' + fileToSearch
tempFileName = 'temp_' + fileToSearch

# If there's already an 'old_' prefixed backup file there from
# a previous run, remove it...
if os.path.isfile( oldFileName ):
	os.remove( oldFileName )

tempFile = open( tempFileName, 'w' )

for line in fileinput.input( fileToSearch ):
    tempFile.write( line.replace( textToSearchFor, textToReplaceWith ) )

tempFile.close()

# Rename the original file by prefixing it with 'old_'
os.rename( fileToSearch, oldFileName )

# Rename the temporary file to what the original was named...
os.rename( tempFileName, fileToSearch )

raw_input( '\n\nPress Enter to exit...' )

