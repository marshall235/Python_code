#!/usr/bin/python3
import sys
def is_palindrome(input_string):
    #Remove non-alphanumeric characters and convert to lowercase manually
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    #Check if the cleaned string is equal to its reverse 
    if cleaned_string  == cleaned_string[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome!")

if __name__ == "__main__":
    #Read input from the command line
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        is_palindrome(input_string)
