#-------------------------------------------------------------------------------
# Name:        Homework #5
# Purpose:      Implement Goodchild & Hunter's (GH) accuracy method for linear
#               features raster operations only. There are some advantages
#               in using rasters (easy to figure out how many cells are within
#               a buffer) but there are some disadvantages (will need to do
#                one buffer at a time).
# Author:      Sam Limerick, UT Austin
#
# Created:     04/10/2016
# Copyright:   (c) sal2737 2016
# Licence:     <your licence>
# Modifications:
#
#-------------------------------------------------------------------------------

# Import all necessary modules and submodules, check out Spatial Analyst extension
import sys, string, os, arcpy
from arcpy import env
from arcpy.sa import *
# Check spatial analyst extension (complete)
arcpy.CheckOutExtension("Spatial")

# set environment variables
path = 'C:/Users/sal2737/Desktop/EpsilonBand' #working directory path
env.workspace = path
env.extent = 'actualrd.tif' #constrains ArcPy operations to just this file
env.cellSize = 'actualrd.tif' # nabs cellsize of the raster actualrd.tif
env.outputCoordinateSystem = 'actualrd.tif' # ensures output CS is same as this file
outTable = 'epsilonCalcs.dbf' # Creates name for the dbf table that will store the values 
env.overwriteOutput = True

#create table to populate with results of epsilon band analysis
arcpy.CreateTable_management(path, outTable)

#variables for specification of fields
widthName = 'Width'
numCellsName = 'NumCells'
propInName = 'PropIn'
widthPrec = 5
numCellsPrec = 9
propInPrec = 3
propInScale = 2 #floats need precision and scale

#add and specify fields
arcpy.AddField_management(outTable, widthName, 'SHORT', widthPrec)
arcpy.AddField_management(outTable, numCellsName, 'LONG', numCellsPrec, field_is_nullable = 'NULLABLE')
arcpy.AddField_management(outTable, propInName, 'FLOAT', propInPrec, propInScale)

simRd = 'OT1.tif' #filename of simulated roads
totRd = 0
with arcpy.da.SearchCursor(simRd, ['Value', 'Count']) as cursor:  #complete
    for row in cursor:
        if row[0] == 1:
            totRd = float(row[2]) #Why float?? To be able to do decimal division

#Create a cursor to record the values on your table
actualRd = 'actualrd.tif'
with arcpy.da.InsertCursor(outTable,['Width', 'NumCells', 'PropIn']] as tabcur: 
    buffDist = 500.0
    while buffDist < 5100: #iterates up to 5000
        tempEuc = 'temp_dist.tif'  
        outEucDist = EucDistance(actualRd,buffDist) 
        outEucDist.save(tempEuc) #saves Euclidean distance to temp_dist.tif
        tempCon = 'counts.tif' #specifies output file for conditional statement
        #creates an output raster w/value = 1 where the simulated road is encapsulated by the specified buffer size
        outCon = Con(((Raster(tempEuc) >= 0) & (Raster(simRd) == 1)), 1)
        outCon.save(tempCon)
        #Create cursor to obtain count of simRd cells encapsulated in buffer
        thisRd = 0
        with arcpy.da.SearchCursor(tempCon,['Value', 'Count']] as countCur:
            for count in countCur:
                if count[0] == 1:
                    thisRd = float(count[1])
        #specify a list of relevant values to be written as a row to output .dbf
        proportion = thisRd/totRd
        outRowValues = [buffDist, thisRd, proportion]
        tabcur.insertRow(outRowValues)
        buffDist += 500.0
# after the loop is completed, you can delete your intermediate files
arcpy.Delete_management(tempEuc)
arcpy.Delete_management(tempCon)

#This should work...
# Plot the results in Excel (need to open Excel first and then, from within
# Excel, open the dbf table)
# As always, if you want to use matplotlib the better.
# Submit: your PY code, your DBF table, your Figure.


