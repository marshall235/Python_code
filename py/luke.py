#!/usr/bin/python3
import sys
def identify_relation(key):
    relations ={'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}
    #Check if the key is Dartch Vader for the special message
    if key in relations:
        message = "No, I am your father" if key == "Darth Vader" else f"Luke, I am  your {relations[key]}"
        print(message)
    else:
        print("Key not found in the relations dictionary")

if __name__ == "__main__":
     if len(sys.argv) > 1:
         key = sys.argv[1]
         identify_relation(key)
