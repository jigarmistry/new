#------------------------------------------------------------------------------
#           Name: list_files_in_zip.py
#         Author: Jigar Mistry
#  Last Modified: 05/08/2013
#    Description: This Python script demonstrates how to use zipfile to list
#                 the files contained in a zip archive.
#------------------------------------------------------------------------------

import zipfile

myZipFile = zipfile.ZipFile( "test.zip", "r" )

# List all files contained within the zip file
for fileName in myZipFile.namelist():
    print fileName
print

# List file information
for info in myZipFile.infolist():
    print info.filename, info.date_time, info.file_size

raw_input( '\n\nPress Enter to exit...' )
