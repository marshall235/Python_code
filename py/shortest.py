#!/usr/bin/python3
import sys
def find_shortest_word(input_string):
    #Split the string into words
    words = input_string.split()

    #Find the shortest word
    shortest_word = min(words, key=len)

    #Print the results
    print(f"The shortest word is {shortest_word.upper()}")

if __name__ == "__main__":
    #Read Input from the command line
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        find_shortest_word(input_string)
    else:
        print("Please provide string as a command line argument")
