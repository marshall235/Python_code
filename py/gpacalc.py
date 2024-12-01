#!/usr/bin/python3
import sys

gpa_dict = {'A': 4.0, 'A-': 3.66, 'B+': 3.33, 'B': 3.0, 'B-': 2.66, 'C+': 2.33, 'C': 2.0, 'C-': 1.66, 'D+': 1.33, 'D': 1.0, 'D-': 0.66, 'F': 0.0}
#Convert all the arguments to upper
grades = [grade.upper() for grade in sys.argv[1:]]
#Calculate the GPA
gpa = sum(gpa_dict[grade]  for grade in grades) / len(grades)

#Print the results with two decimal places
print(f"My GPA is {gpa:.2f}")
