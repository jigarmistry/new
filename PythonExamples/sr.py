#------------------------------------------------------------------------------
#           Name: sr.py
#         Author: Jigar Mistry
#  Last Modified: 05/08/2013
#    Description: This Python script demonstrates how to perform a
#                 search-and-replace on a file via the command line.
#------------------------------------------------------------------------------

import os
import sys
import fileinput

usage = "usage: %s search_text replace_text [infile [outfile]]" % os.path.basename(sys.argv[0])

if len( sys.argv ) < 3:
    	print usage
else:
	#print "There are %s args " %len( sys.argv )
	
    	textToSearchFor   = sys.argv[1]
	textToReplaceWith = sys.argv[2]
    	fileToSearch      = sys.argv[3]
    	fileToOutput      = sys.stdout # This defaults to stdout if no file name is passed in.
    	
    	if len( sys.argv ) > 4:
		fileToOutput = open( sys.argv[4], 'w' )
		#print "outfile = ", fileToOutput

	for line in fileinput.input( fileToSearch ):
	    fileToOutput.write( line.replace( textToSearchFor, textToReplaceWith ) )
	    
	if len( sys.argv ) > 4:
		fileToOutput.close()
