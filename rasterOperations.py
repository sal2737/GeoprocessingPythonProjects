#-------------------------------------------------------------------------------
# Name:        Lecture 10, Homework #7
# Purpose:     Reassign the value of all cells shown as "deforested" to the value of the majority of adjacent cells. This predictive model leverages the 1st law of geography -- that near things are more similar than far things -- to attempt to model what an area looked like before deforestation occurred.
#            
# Author:      Sam Limerick
#
# Created:     10/21/2016
# Copyright:   (c) Sam 2016
# Licence:     <your licence>
# Modifications: To be continued?
#-------------------------------------------------------------------------------

################################################################################
# GIS Raster Operations
#   1. Cell-by-Cell: Applied to each cell
#   2. Global Operations: (ex. flow accumulation, accumlation cost) reliant on
#       other cells for value
#   3. Neighborhood Operations (Moving window operations, sliding window
#       operations): Define window or kernel where weights are assigned
#           - Must assign size of window
#           - Must assign weights of window
#           - Centers window at cell of evaluation, "slides" to next cell
#                       -Cellular Automata (CA) Models: used for fire modeling
################################################################################

#import all necessary modules, submodules, and licenses.
import sys, string, os, arcpy
from arcpy import env
from arcpy.da import *
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')

#define environment variables
path = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T'
in_raster = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/ecosystemvs2_900m.tif/'
env.workspace = path
env.extent = in_raster
env.cellSize = in_raster
env.outputCoordinateSystem = in_raster
env.overwriteOutput =  True

#file paths for analysis
thisRas = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/thisRas.tif'
forestRas = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/forested.tif'
finalraster = '/Users/sam_limerick/Desktop/Fall 2016/GRG 356T/finalraster.tif'

# Gives 'water' cells a value of "NoData" and saves "pre-analysis" raster to thisRas
outRaster = Con(Raster(in_raster) != 11, in_raster)  # Assign NoData to water cells, if raster
outRaster.save(thisRas)

#default values; only assigned so that nCell-lastCount doesn't equal 0 from the get-go
lastCount = 0
nCell = 1 

while (nCell-lastCount) != 0: #run the neighborhood analysis until no 1s are being changed by furhter iterations (i.e nCell-lastCount = 0)
    #opens search cursor to obtain the number of 1s -- deforested cells -- befor neighborhood analysis
    with arcpy.da.SearchCursor(thisRas, ['VALUE', 'COUNT']) as rows:
        for row in rows:
            if row[0] == 1:
                nCell = row[1]
                break #breaks from the 1st row once we get the one relevant number (count of cells for 1st row - deforestation)
    neigh = NbrRectangle(7, 7, "CELL") #defines a 7x7 neighborhood (210 x 210 meters) to analyze cells surrounding deforested cells

    #constructs a conditional raster that performs one iteration of FocalStatistics using MAJORITY rules -- i.e deforested cell values are reassigned based on the status of the majority of their neighbors. We can view the creation of this new raster as one iteration of our analysis. The while loop repeats this until no more deforested cells are reassigned (I.e the algorithm has reached its limits.)
    conFile = Con(Raster(thisRas) == 1, (FocalStatistics(thisRas, neigh, "MAJORITY")), thisRas)  
    conFile.save('confile.tif')

    #Append_management allows us to cast the results of the analysi back to a raster wfrom which we can see how many cells were changed
    forestRas = arcpy.Append_management(conFile, thisRas, "TEST")

    # Use a new SearchCursor within loop to recount deforested cells after neighborhood analysis is ran
    with arcpy.da.SearchCursor(forestRas, ['VALUE', 'COUNT']) as rows:
        for row in rows:
            if row[0] == 1:
                lastCount = row[1]
                print lastCount

#final raster puts the water cells "back in" using a conditional statement
finalraster = Con(Raster(in_raster) != 11, thisRas, in_raster)

#list of fields to be repopulated in the completed analyzed product raster
fieldlist = ["RED", 'GREEN', 'BLUE', 'VEGTYPE']

#join the relevant fields from original raster back to the final, analyzed raster
arcpy.JoinField_management(finalraster, "Value", in_raster, "Value", fieldlist)

#saves the final product
finalraster.save("finalraster.tif")

# Bugs and Solutions:
#       - Before I discovered FocalStatistics, I spent a great deal of time trying to figure out the solution usiong RasterToNumPyArray and NumPyArrayToRaster. I essentially tried to do what ESRI's software engineers did when they created FocalStatistics!! If there is anything I've learned while developing coding skills, its that if something has been done before, typically the best course of action is to repurpose the original or use a pre-defined fucntion rather than starting from the ground up.
#       - Another solution I tried utilize a nested UpdateCursor within a SearchCursor. At a high level, I attempted to read in the values from the FocalStatistics and write it back (using UpdateCursor) to the orginal raster. From there, I planned on further iterations of the while loop using a similar condition as this successful solution. However, I ran into the roadblock of traversing an iterator of lists (the data structure that cursors return). Going row by row in this manner was difficult for a variety of reasons
#       - Controlling which row of the cursor I looked at was difficult. Each reset of the loop always led me back to the first line of the cursor. I attempted to use .next to raverse the loop, but even that reset because we used 'with' for opening the cursor (thereby closing and erasing this traversal of the loop)
#       - .next() vs .next (difference by Python versioning) was also confusing when I attempted to run a "one-to-one" solution with cursors
#       - Finding out how best to save the temporary values nCell and lastCount within the context of a while loop was an exercise in the scoping of variables. Before we figured it out, our while loop would run infinitely, redoing the analysis over and over again even though a 7x7 NbrRectangle was no longer grabbing majority values for vlaues other than deforested. 




