#IN CLASS EXERCISE
# Use the Texas County demographic file
# Create a field called "YouthLevel", text. Three possible categories:
# young, adult, senior
# You define the breakings but values should be based on the proportion
# of people below 17 (two fields) over total population
# Use the Texas County demographic file # Create two fields, one called "YouthLevel", text and the other "PrYouth", # float, which is the proportion of under 17 people in the total population. #  The three possible categories for YouthLevel are: # young, adult, senior # You define the breakings but values should be based on the proportion # of people below 17 (sum of two fields) over total population

import sys, string, os, arcpy
from arcpy import env
from arcpy.sa import *
path = r"/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/Lec4Files/"
env.workspace =path
# Set option to overwrite existing files
env.overwriteOutput = True
# Check out Spatial Analyst Extension
arcpy.CheckOutExtension("Spatial")

shpFile = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/Lec4Files/tx_county_demographics.shp'
fName1 = 'YouthLevel'
fName2 = 'PrYouth'
arcpy.AddField_management(shpFile, fName1, 'TEXT')
arcpy.AddField_management(shpFile, fName2, 'FLOAT')


# you can write directly but then have to count arguments correctly
#arcpy.AddField_management(fc,fName, fType, "","", 25, "Shape Geometry")
with arcpy.da.UpdateCursor(shpFile, ['POP_2000', 'AGE_UNDER5', 'AGE_5_17', fName1, fName2]) as cursor:
    for row in cursor:
    	if ((row[1] + row[2]) / row(0)) > .5:
    		row[3] = 'Young'
    	elif ((row[1] + row[2]) / row(0)) > .3:
    		row[3] = 'Adult'
    	elif ((row[1] + row[2]) / row(0)) > .15:
    		row[3] = 'Mature'
        row[4] = (row[1] + row[2]) / row(0)
        cursor.updateRow(row)