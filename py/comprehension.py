#!/usr/bin/python3
import sys

loop_list = sys.argv[1:]

#Convert the strings to integers and apply the required transformation 

result = [int(value) + index for index, value in enumerate(loop_list)]

#Print the results
print(result)
