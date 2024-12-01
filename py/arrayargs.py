#!/usr/bin/python3
import numpy as np
import sys

def process_array(a,b,c,d):
    #Create a numpy array from the provided arguments
    arr = np.array([a,b,c,d])

    #Print the type of array
    print(type(arr))

    # Calculate the product of the array of elements
    product = np.prod(arr)

    #Print the product
    print(product)

if __name__ == "__main__":
    #Check if exactly four arguments are provided (excluding the script name)
    if len(sys.argv) != 5:
        print("Usage: python arraysargs.py <int1> <int2> <int3> <int4>")
    else:
        # Convert the arguments to integers
        try:
            args = list(map(int, sys.argv[1:5]))
            process_array(*args)
        except ValueError:
            print("Please provide four integer value")
