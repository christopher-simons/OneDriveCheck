# onedrivecheck.py
# 27 October 2018
# Author: Chris Simons

# Script to check Microsoft OneDrive for any 'illegal' files. 

# Specification of what is deemed to be an 'illegal' file is taken from:
# https://support.office.com/en-us/article/invalid-file-names-and-file-types-in-onedrive-onedrive-for-business-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa

# Set the path to the OneDrive root on line 

import os
import glob

os.chdir( '/Users/Chris/OneDrive - UWE Bristol (Staff)' )  # set the path to OneDrive root here

# Provide some feedback on where we're starting from
print( 'OneDrive root is: ' )
print( os.getcwd( ) )
print( )

# the root from where we will be searching
my_path = os.getcwd( )

# Quick test of recursive traversal of all .txt files under specified root
# my_path/     the dir
# **/       every file and dir under my_path
# *.txt     every file that ends with '.txt'
#files = glob.glob( my_path + '/**/*.*', recursive=True )
#print( files ) 

# Firstly, filter a list of files based on the OneDrive size limit

print( 'Checking for files whose size exceeds 15GB...' )
FILE_SIZE = 15000000000		# 15GB
info1 = [ f for f in glob.glob( my_path + '/**/*.*', recursive = True ) if os.stat( f ).st_size > FILE_SIZE ]

if len( info1 ) == 0:
	print( 'no files found with size > 15GB' )
else:
	print( 'illegally large files are: {0}'.format( info1 ) )
print( ) 

# Secondly, filter some lists based on 'illegal' characters

print( 'Checking for file names will illegal characters' ) 
patterns = [ '/**/*"*.*', '/**/*<*.*', '/**/*>*.*', '/**/*|*.*', '/**/*%*.*', '/**/*&*.*', '/**/*{*.*', '/**/*}*.*', '/**/*~*.*', '/**/*"*.*"*', '/**/*<*.*<*', '/**/*>*.*>*', '/**/*|*.*|*', '/**/*%*.*%*', '/**/*&*.*&*', '/**/*{*.*{*', '/**/*}*.*}*', '/**/*~*.*~*' ]

for pattern in patterns:
	info = [ f for f in glob.glob( my_path + pattern, recursive = True ) ]
	if len( info ) == 0:
		print( 'no files found for illegal character pattern {0}'.format( pattern ) )
	else:
		print( 'file names with illegal character {0} are: {1}'.format( pattern, info ) )
print( )

# Thirdly, check the length of all file names is less than 400 characters for OneDrive for Business
# Note that "SharePoint Server versions only support up to 260 characters for file and path lengths."

print( 'checking for files with names that exceed 260 characters...' )
files = glob.glob( my_path + '/**/*.*', recursive = True ) 

MAX_CHARS = 260
i = 0
number_found = 0

for f in files:
	if len( files[ i ] ) > MAX_CHARS:
		print( files[ i ] )
		number_found = number_found + 1
	i = i + 1 

# Provide some summary information of third check
print( 'number of files examined is: {0}'.format( i ) )
print( 'number of files with names that are too long is: {0}'.format( number_found) )
print( )




