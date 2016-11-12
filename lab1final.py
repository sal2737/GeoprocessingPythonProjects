#define start and end time variables in seconds
t0 = 1000 
t1 = 108953

#total time difference in seconds - do all calculations starting from here
difference = t1 - t0

#Remainder of seconds - i.e number of seconds to be written at final calculation
secsRemain = difference % 60

#total number of full minutes for the duration - use to calculate hours and consequently days
minTotal = difference / 60

#Remainder of minutes - i.e. number of minutes to be written at final calculation
minsRemain = minTotal % 60

#total number of full hours for the duration - use to calculate days
hoursTotal = minTotal / 60

#Remainder of hours - i.e number of hours to be written at final calculation
hoursRemain = hoursTotal % 24

#total number of full days for the duration, print at final calculation
daysTotal = hoursTotal / 24

print "Total processing time is equal to: %s days, %s hours, %s minutes, and %s seconds." %(daysTotal, hoursRemain, minsRemain, secsRemain)
