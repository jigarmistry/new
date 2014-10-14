#------------------------------------------------------------------------------
#           Name: read_from_zip.py
#         Author: Jigar Mistry
#  Last Modified: 05/08/2013
#    Description: This Python script demonstrates how to use zipfile to read
#                 from a zipped archive.
#------------------------------------------------------------------------------

import zipfile

myZipFile = zipfile.ZipFile( "test.zip", "r" )

for fileName in myZipFile.namelist():
    data = myZipFile.read(fileName)
    print fileName, len(data), repr(data[:50])

raw_input( '\n\nPress Enter to exit...' )
