#!/usr/bin/python3
import sys

def capCount(input_string):
    capital_count = 0
    indices_sum = 0

    for index, char in enumerate(input_string):
        if char.isupper():
            capital_count += 1
            indices_sum += index

    print(capital_count)
    print(indices_sum)

if __name__ == "__main__":
    # Read input from the command line  argument
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        capCount(input_string)
    else:
        print("Please provide a string as a command line argument")
