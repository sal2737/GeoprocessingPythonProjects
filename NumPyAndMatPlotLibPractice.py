#-------------------------------------------------------------------------------
# Name:        Homework #8
# Purpose:     Practice numpy module functions
#
# Author:
#
# Created:     11/04/2016
# Copyright:   (c) sal2737 2016
# Licence:     <your licence>
# Modifications:
#
#-------------------------------------------------------------------------------

# Your goal is to create line graphs showing total precipitation in the last
# 11 years in five cities around the world: Austin, TX; Marrakesh, Morocco;
# Jakarta, Indonesia; Sydney, Australia; and Honolulu, Hawaii.

#Step 2 - Python Code

# Import relevant modules
import numpy as np
import matplotlib.pyplot as plt
import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy.da import *

#set path
path = r"C:/Users/sal2737/Desktop/Lab8/LocationData"
env.workspace = path

#set environment variables
file = "3B43.2006_v7_year_total.tif"
env.extent = file
env.cellSize = file
env.outputCoordinateSystem = file
env.overwriteOutput = True

#Specifications for raster conversion
cityRaster = "LocationRast.tif"
bottomLeft = arcpy.Point(-157.98588, -33.99376)
ncols = 1237
nrows = 263

# Convert city raster to numpy array
cities = arcpy.RasterToNumPyArray(cityRaster, bottomLeft, ncols, nrows, 0) #OPTIONAL: specify final parameter nodata_to_value as 0?

#convert 11 years of precipitation rasters into individual numpy arrays
precip05 = arcpy.RasterToNumPyArray("3B43.2005_v7_year_total.tif")
precip06 = arcpy.RasterToNumPyArray("3B43.2006_v7_year_total.tif")
precip07 = arcpy.RasterToNumPyArray("3B43.2007_v7_year_total.tif")
precip08 = arcpy.RasterToNumPyArray("3B43.2008_v7_year_total.tif")
precip09 = arcpy.RasterToNumPyArray("3B43.2009_v7_year_total.tif")
precip10 = arcpy.RasterToNumPyArray("3B43.2010_v7_year_total.tif")
precip11 = arcpy.RasterToNumPyArray("3B43.2011_v7_year_total.tif")
precip12 = arcpy.RasterToNumPyArray("3B43.2012_v7_year_total.tif")
precip13 = arcpy.RasterToNumPyArray("3B43.2013_v7_year_total.tif")
precip14 = arcpy.RasterToNumPyArray("3B43.2014_v7_year_total.tif")
precip15 = arcpy.RasterToNumPyArray("3B43.2015_v7_year_total.tif")

#Stacks the 11 years into one 3-D array
precip_array = np.dstack((precip05, precip06, precip07, precip08, precip09, precip10, precip11, precip12, precip13, precip14, precip15))

#grabs array indices for locations of cities
city_locator = np.where(city_np)

#slices 3-D array into a reduced product with precipitation values for each city over the 11 years 
citiesYearsPrecip = precip_array[city_locate[0], city_locate[1], :]
print citiesYearsPrecip

# plot results using matplotlib
years = np.arange(2005, 2016)

# Austin
austin_precip = citiesYearsPrecip[0,:]
print austin_precip
plt.plot(years, austin_precip)
plt.xlabel('Year')
plt.ylabel('Precipitation')
plt.title('Austin Precipitation')
plt.show()

# Marrakesh
marrakesh_precip = citiesYearsPrecip[1,:]
print marrakesh_precip
plt.plot(years, marrakesh_precip)
plt.xlabel('Year')
plt.ylabel('Precipitation')
plt.title('Marrakesh Precipitation')
plt.show()

# Honolulu
honolulu_precip = citiesYearsPrecip[2,:]
print honolulu_precip
plt.plot(years, honolulu_precip)
plt.xlabel('Year')
plt.ylabel('Precipitation')
plt.title('Honolulu Precipitation')
plt.show()

# Jakarta
jakarta_precip = citiesYearsPrecip[3,:]
print jakarta_precip
plt.plot(years, jakarta_precip)
plt.xlabel('Year')
plt.ylabel('Precipitation')
plt.title('Jakarta Precipitation')
plt.show()

# Sydney
sydney_precip = citiesYearsPrecip[4,:]
print sydney_precip
plt.plot(years, sydney_precip)
plt.xlabel('Year')
plt.ylabel('Precipitation')
plt.title('Sydney Precipitation')
plt.show()

