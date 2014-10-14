#------------------------------------------------------------------------------
#           Name: enviroment_variables.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to acces enviroment
#                 variables.
#------------------------------------------------------------------------------

import os

envVar = os.environ.get( "PATHEXT" )

print( "PATHEXT = " + envVar )

raw_input( '\nPress Enter to exit...' )
