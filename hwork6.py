#-------------------------------------------------------------------------------
# Name:        Homework #6
# Purpose:     Use geoprocessing functions to 'recreate' original ecosystems
#               of Loreto, Peru.
#
# Author:      Sam Limerick, UT Austin
#
# Created:     11/10/2016
# Copyright:   (c) ea9267 2016
# Licence:     <your licence>
# Modifications:
#
#-------------------------------------------------------------------------------
# Suppose you want to study the impact of deforestation on the provision of
# ecoystem services (ES) in a tropical region. You want to calculate how much ES
# were lost with respect to a benchmark of zero deforestation or "pristine"
# landscape. The problem is that the earliest information we have for the area
# already contains 'deforestation'. Thus, we do not know how the ecosystems
# looked like prior to the onset of deforestation.
# You are given the raster 'ecosystemsvs2_900m.tif' where the cells = 1
# are cells that were deforested. Your job is to think about a strategy to
# switch the values of cells that are deforested back to a natural ecosystem.
# All other categories in this raster (e.g. semi-decidious forest, piedmont
# forest) are valid substitutes, with the exception of water cells.
# All other cells that are not 'deforested' must maintain their current
# classification.

# The first law of geography says that near things are more related than
# distant things. Therefore, it seems natural that we should use information
# about the neighbors of each deforested cells to inform what type of
# ecosystem is more likely to substitute for deforestation. For example if most
# of the neighbors of one particular deforested cell are 'evergreen forest' we
# would convert that cell to evergreen forest.

# Write a pseudocode of your procedure. Try to include as much detail as
# possible, without actually writing the code. Try also to envision potential
# problems that you may encounter. If you are thinking about running a loop,
# when is the loop going to stop?

#Submit your pseudocode with brief text explaining each step.

#START 

#import necessary modules, check out SA extension, set environment
import arcpy, os, sys
from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

path = r'C:/Users/sal2737/Desktop/Lec6Files'
env.workspace = path
env.overwriteOutput = True

inRaster = 'ecosystemsvs2_900m.tif'
# Use RasterToNumPyArray to transform the raster into a 2-D array for easy processing
rasterArray = arcpy.RasterToNumPyArray(inRaster, )

#initialize row and column variables using .shape 
rows, cols = rasterArray.shape

#initialize a loop that iterates over each row of the array (i.e. horizontal bands of the raster)
for rowNum in xrange(rows):
	#initialize an inner loop to iterate over each element of each row (i.e each individual cell)
	for colNum in xrange(cols):   
		#use rasterArray.item(rowNum, colNum) to parse raster and find values == 1 to initialize analysis of neighbors
		#if == 1, do something
			# check value of all neighbors and keep track of counts of each type
			# Three "up top" neighbors, that is to say, row - 1, column plus or minus 1
			# Side neighbors, that is, row = row, column + or - 1
			# "down below" neighbors, that is, row + 1
			# reassign the cellValue (previously 1 == deforested) to the value held by the most neighbors

		#else, on to the next cell

outRaster = 'ecosystemsvs2_900mEDIT.tif' #output file definition
#utilize NumPyArrayToRaster to transform this edited array back into a raster format
arrayRaster = NumPyArrayToRaster(rasterArray, )

# save arrayRaster into the file defined by outRaster











