#!/usr/bin/python3
import sys

def find_common_words(set_a, set_b):
    #Convert lists to sets
    set_a = set(set_a)
    set_b = set(set_b)

    #Find the common words
    common_words  = set_a & set_b

    #Print output in a set format
    print(common_words)

    #Print the output in set format
if __name__ == "__main__":
    #Load the command line arguments in set a
    set_a = sys.argv[1:]

    #Define set_b
    set_b = ['apple', 'banana', 'mango', 'orange']

    #Find and print common words
    find_common_words(set_a, set_b)
