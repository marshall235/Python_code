#!/usr/bin/python3
import sys

def letter_counter(word):
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1
    return letter_dict

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python counter.py <word>")
    else:
        word = sys.argv[1]
        result = letter_counter(word)
        print(result)
