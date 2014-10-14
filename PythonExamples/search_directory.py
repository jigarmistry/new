#------------------------------------------------------------------------------
#           Name: search_directory.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to use os.walk()
#                 to walk through a directory hierarchy and list everything 
#                 found.
#------------------------------------------------------------------------------

import os

for root, dirs, files in os.walk( os.curdir ):
		
	print( "root = " + root )

	for file in files:
		print( "file = " + file )

	for dir in dirs:
		print( "dir = " + dir )

	print( "\n" )

raw_input( '\n\nPress Enter to exit...' )
