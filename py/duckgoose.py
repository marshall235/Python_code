#!/usr/bin/python3
import sys

def remove_goose(words):
    return [word for word in words  if word != 'goose']

if __name__ == "__main__":
    #Load the command-line arguments into duck_goose
    duck_goose = sys.argv[1:]

    #Remove 'goose from the list
    result = remove_goose(duck_goose)

    #Print the resulting list
    print(result)
