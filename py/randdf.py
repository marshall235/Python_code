#!/usr/bin/python3
import pandas as pd
import numpy as np
import sys

def create_random_dataframe(rows, cols):
    #set random seed for reproducibility
    np.random.seed(56)

    #Generate random integers between 0 and 100
    data = np.random.randint(0, 101, size=(rows, cols))

    #Create a Pandas Dataframe from the generated data
    df = pd.DataFrame(data)

    #Print the dataframe
    print(df)

if __name__ == "__main__":
    #Chek if exactly two arguments are provided excluding the script name)
    if len(sys.argv) !=3:
        print("Usage: Python randf.py <rows> <columns>")
    else:
        try:
            rows = int(sys.argv[1])
            cols = int(sys.argv[2])
            create_random_dataframe(rows, cols)
        except ValueError:
            print("Please provided two integer arguments")
