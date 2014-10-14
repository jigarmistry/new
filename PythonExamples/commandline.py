#------------------------------------------------------------------------------
#           Name: commandline.py
#         Author: Jigar Mistry
#  Last Modified: 05/08/2013
#    Description: This Python script demonstrates how to use
#                 command line arguments.
#------------------------------------------------------------------------------

import sys

usage='[file name] [your argument]';
if len( sys.argv ) < 2:
    	print usage
else:
    print sys.argv[0]
    print sys.argv[1]
