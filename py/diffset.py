#!/usr/bin/python3
import sys
def find_difference(set_a, set_b):
    #Convert lists to sets
    set_a = set(set_a)
    set_b = set(set_b)

    #Find the words that are in set_a but not in set_b
    difference = set_a - set_b

    #Print the output in set format
    print(difference)

if __name__ == "__main__":
    #Load the command line arguments into set_a

    set_a = sys.argv[1:]

    #Define set_b
    set_b  = ['apple', 'banana', 'mango', 'orange']

    #Find and print the difference
    find_difference(set_a, set_b)
