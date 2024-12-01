#!/usr/bin/python3
import sys

#Looad the arguments for the command line
loop_list = sys.argv[1:]

#Convert the string-type integers into integer types
int_list = [int(num) for num in loop_list]

# Add each number's index position to itself 
result_list = [num + idx for idx, num in enumerate(int_list)]

#Print the reuslting list
print(result_list)
