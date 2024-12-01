#!/usr/bin/python3
import sys

def find_divisibles(n):
    # Create an empty list to store the results
    results = []
    
    #Loop through the range from 3000 to  5000
    for i in range(3000, 5001):
        #Check  if i is divisible by n, n+7  or n^2
        if i % n == 0 or i % (n + 7) == 0  or i % (n ** 2) == 0:
            results.append(i)

        #Print the resulting list
        print(results)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inrange,py <integer>")
    else:
        try:
            n = int(sys.argv[1])
            find_divisibles(n)
        except ValueError:
            ("Please provide a valid integer")
