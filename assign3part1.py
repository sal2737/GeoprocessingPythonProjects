#-------------------------------------------------------------------------------
# Name:        Homework #3, Part 1
# Purpose:     Check if input is a number
#
# Author:      Sam Limerick
#
# Created:     9/23/2016
# Copyright:   
# Licence:     <your licence>
# Modifications:
#
#-------------------------------------------------------------------------------

#initialize default value for user input
userInput = 0

#runs indefinitely, just returns the proper message depending on if input is an interger or not
while True:
    userInput = input("Pick an integer: ")
    try:
        val = int(userInput)
    except ValueError:
        print("That's not an integer! Try again.")
        continue
    else:
        print("That's an integer!")

