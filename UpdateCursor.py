#-------------------------------------------------------------------------------
# Name:        Homework #4
# Purpose:      Practice arcpy tabular data access and manipulation
#
# Author:      Sam Limerick
#
# Created:     24/09/2016
# Copyright:   (c) ea9267 2016
# Licence:     <your licence>
# Modifications:
#
#-------------------------------------------------------------------------------

# Import system modules 
import sys, string, os, arcpy
from arcpy import env
from arcpy.da import *

# set geoprocessing environment
path = r"/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/EcosysTiffs/"
env.workspace = path
env.overwriteOutput = True

# create list of tif files
tifList = arcpy.ListRasters("", "tif")

#dictionary that relates a color scheme to the proper vegetation types
rgbDict = {
    1: [255./255,0.,0.,'Deforested'],
    2: [209./255, 255./255, 255./115,'Semi-deciduous forest'],
    3: [85./255, 255./255, 0.,'Highland Island forest'],
    4: [112./255, 168./255, 0.,'Piedmont forest'],
    5: [190./255, 255./255, 232./255.,'Flooded forest'],
    6: [0., 197./255, 255./255,'Wetland forest'],
    7: [76./255, 115./255, 0.,'Evergreen forest'],
    8: [76./255, 115./255, 0.,'Sub-Andean evergreeen forest'],
    9: [214./255, 157./255, 188./255,'Palmtree forest'],
    10:[197./255, 0., 255./255,'Successional riparian complex'],
    11:[0., 77./255, 168./255,'Water body'],
    12:[0., 132./255, 168./255,'Herbaceous dominated wetlands'],
    13:[190./255, 210./255, 255./255,'Palm dominated wetlands'],
    14:[255./255, 170./255, 0.,'White sand vegetation'],
    17:[255./255, 170./255, 0.,'White sand vegetation']
}

#creates a list of .tif files in current workspace
tifList = arcpy.ListRasters("", "tif")

#local variables for field names
fName1 = "RED"
fName2 = "GREEN"
fName3 = "BLUE"
fName4 = "VEGTYPE"

#loops through tif list and perform series of geoprocessing tasks
for tif in tifList: 
	arcpy.AddField_management(tif, fName1, 'FLOAT', field_precision = 3, field_scale = 3)
	arcpy.AddField_management(tif, fName2, 'FLOAT', field_precision = 3, field_scale = 3)
	arcpy.AddField_management(tif, fName3, 'FLOAT', field_precision = 3, field_scale = 3)
	arcpy.AddField_management(tif, fName4, 'TEXT')

	#instantiates an UpdateCursor for efficient data manipulation
	with arcpy.da.UpdateCursor(tif, ['VALUE', fName1, fName2, fName3, fName4]) as cursor:
		for row in cursor:
			dictCall = row[0] #saves vegetation numeric value for use in dictionary calls
			row[1] = rgbDict[dictCall][0] 
			row[2] = rgbDict[dictCall][1]
			row[3] = rgbDict[dictCall][2]
			row[4] = rgbDict[dictCall][3]
			cursor.updateRow(row)


