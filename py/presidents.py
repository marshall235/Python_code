#!/usr/bin/python3
import pandas as pd
import sys

def main():
    # Read in command line argunents
    start = int(sys.argv[1])
    stop = int(sys.argv[2])

    # Load the csv file
    file_path = ':president_heights.csv'
    df = pd.read_csv(file_path)

    #Slice the heights column 
    heights_slice = df['height(cm)'][start-1:stop]

    #Calculate the average height 
    average_height = heights_slice.mean()

    #Print the result
    print(f"The average height of the presidents number {start} to {stop} is {average_height:.2f}")

if __name__ == "__main__":
    main()
