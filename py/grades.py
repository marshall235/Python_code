#!/usr/bin/python3
import sys

def calculate_average_excluding_subject(exclude_subject):
    grades = {'Biology': 80, 'Physics': 88, 'Chemistry': 98, 'Math': 89, 'English': 79, 
              'Music': 67, 'History': 68, 'Art': 53, 'Economics': 95, 'Psychology': 88}
    #Check if the subject to exclude exists in the dictionary
    if exclude_subject in grades:
        total_score = sum(score for subject, score in grades.items() if subject != exclude_subject)
        number_of_subjects = len(grades) - 1
        average_score = total_score / number_of_subjects
        print(f"{average_score:.2f}")
    else:
        print("Subject not found in grade dictionary.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exclude_subject = sys.argv[1]
        calculate_average_excluding_subject(exclude_subject)
