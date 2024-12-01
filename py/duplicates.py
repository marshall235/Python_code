#!/usr/bin/python3
import sys

def remove_duplicates_and_sort(words):
    #Remove duplicates by converting the list to a set, then back to a list
    unique_words = list(set(words))
    #sort the list in descending order
    unique_words.sort(reverse=True)
    return unique_words

if __name__ == "__main__":
    #Load the command line arguments into a duplicate_words
    duplicated_words = sys.argv[1:]

    #Remove duplicates and sort the list
    result = remove_duplicates_and_sort(duplicated_words)

    #Print the resulting values
    print(result)
