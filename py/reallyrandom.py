#!/usr/bin/python3
import numpy as np
import sys

def generate_random_value(size, multiplier, index):
    #set the random seed for reproducibility
    np.random.seed(42)

    #Generate an array of random integers between 0 and 10
    random_array = np.random.randint(0, 11, size=size)

    #Multiply each element in the array by the provided multiplier
    multiplied_array = random_array * multiplier

    #Handle case where index is larger than the array
    if index >= len(multiplied_array):
        index = len(multiplied_array) -1

    #Get the value at the specified index
    random_value = multiplied_array[index]

    #Print the result
    print(f"Your random value is {random_value}")

if __name__ == "__main__":
    #Check if exactly three arguments are provided excluding the script
    if len(sys.argv) !=4:
        print("Usage: python reallyrandom.py <size> <multiplier> <index>")
    else:
        try:
            size = int(sys.argv[1])
            multiplier = int(sys.argv[2])
            index = int(sys.argv[3])
            generate_random_value(size, multiplier, index)
        except ValueError:
            print("Please provide three integer arguments.")
