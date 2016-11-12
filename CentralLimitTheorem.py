import random
import numpy as np
import csv

#creates ndarray with 50 iterations of 5 random dice rolls, calculated means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (50,5)) 
dmean50 = []
for dice in diceArray:
	dmean50.append(np.mean(dice, out = None))
np.savetxt('csv50draws_5.csv', dmean50, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 100 iterations of 5 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (100,5)) 
dmean100 = []
for dice in diceArray:
	dmean100.append(np.mean(dice, out = None))
np.savetxt('csv100draws_5.csv', dmean100, fmt = '%.1f', delimiter = ' ')
    
#creates ndarray with 200 iterations of 5 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (200,5)) 
dmean200 = []
for dice in diceArray:
	dmean200.append(np.mean(dice, out = None))
np.savetxt('csv200draws_5.csv', dmean200, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 500 iterations of 5 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (500,5)) 
dmean500 = []
for dice in diceArray:
	dmean500.append(np.mean(dice, out = None))
np.savetxt('csv500draws_5.csv', dmean500, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 1000 iterations of 5 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (1000,5)) 
dmean1000 = []
for dice in diceArray:
	dmean1000.append(np.mean(dice, out = None))
np.savetxt('csv1000draws_5.csv', dmean1000, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 50 iterations of 10 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (50,10)) 
dmean50 = []
for dice in diceArray:
	dmean50.append(np.mean(dice, out = None))
np.savetxt('csv50draws_10.csv', dmean50, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 100 iterations of 10 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (100,10)) 
dmean100 = []
for dice in diceArray:
	dmean100.append(np.mean(dice, out = None))
np.savetxt('csv100draws_10.csv', dmean100, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 200 iterations of 10 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (200,10)) 
dmean200 = []
for dice in diceArray:
	dmean200.append(np.mean(dice, out = None))
np.savetxt('csv200draws_10.csv', dmean200, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 500 iterations of 10 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (500,10)) 
dmean500 = []
for dice in diceArray:
	dmean500.append(np.mean(dice, out = None))
np.savetxt('csv500draws_10.csv', dmean500, fmt = '%.1f', delimiter = ' ')

#creates ndarray with 1000 iterations of 10 random dice rolls, calculates means and writes to a CSV
diceArray = np.random.randint(1, high=7, size = (1000,10)) 
dmean1000 = []
for dice in diceArray:
	dmean1000.append(np.mean(dice, out = None))
np.savetxt('csv1000draws_10.csv', dmean1000, fmt = '%.1f', delimiter = ' ')
