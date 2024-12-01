#!/usr/bin/python3
import sys

def count_unique_vowels(input_string):
    vowels = set("aeiou")
    found_vowels = set()

    for char in input_string.lower():
        if char in vowels:
            found_vowels.add(char)

    print(len(found_vowels))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        count_unique_vowels(input_string)
    else:
        print("Please provide string a command line argument")
