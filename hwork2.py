#-------------------------------------------------------------------------------
# Name:        Geoprocessing Homework 2
# Purpose:     Complete the code below. You will import a series of file names,
#   store them in a list, change the name of the file, and record it back to
#    an output txt file. The name change should be based on a dictionary. You
#   will also make use of loops to go through the list of files.
#   The original name of the file is 3B43.YYYYMMDD.7.tif, where YYYY is the
#   4-digit year, MM is the 2-digit month and DD is the 2-digit day. The 2-digit
#   day is fixed '01' but the month varies from '01-12' and year from '2000-
#   2005.
#   The output file should be named: 3B43.YYYYXXXDD.7.tif, where the XXX is the
#   3-letter month (e.g. Jan, Feb, Mar, etc).
#   Example. Original file name 3B43.20010201.7.tif should be renamed
#       3B43.2001Feb01.7.tif
#   You will practice: string manipulation, loops, dictionaries, read and write
#    files.
# Author: Sam Limerick
#
# Created: 9/16/2016
# Copyright:
# Licence:     <your licence>
# Modifications:
#
#-------------------------------------------------------------------------------
# Import system modules
import sys, string, os

# write the complete path of where 'file_list.txt' is located
read_fpath = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/file_list.txt'

#define where finaloutput is to be written
write_fpath = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/output.txt'

# reads in filenames using the with .... read....close structure.
with open(read_fpath) as f_in:
    fnames = f_in.readlines() # readline by default reads each line as its own element into a list for easy access and manipulation

#dictionary of months for use in rewriting file names
month = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}    

# opens a new file to write edited filenames into 
out = open(write_fpath, 'w') 

# Loop used to go through each element of the fnames list 
for f in fnames:
    f.strip()
    out.write(f[0:9] + month[f[9:11]] + f[11:] + '\n') #writes corrected filename string to output file piece by piece within the loop, starts a new line for each filename
    
print 'Outfile %s saved' %write_fpath #writes a message to let us know program's work is done and that edited list of filenames in now available at specified path
out.close()
