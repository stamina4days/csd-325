"""Load, display, update, and save student records stored as JSON.

Title: Module 8.2 - JSON Practice
Author: Prince Hubbard
Date: September 7, 2026
Purpose: Demonstrate JSON load(), list processing, append(), and dump().
"""

import json
from pathlib import Path


JSON_FILE = Path(__file__).with_name("Student.json")


def print_students(student_list):
    """Print every student record in the requested display format."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , Email = {student['Email']}"
        )


def main():
    """Load the JSON data, add one student, and save the updated list."""
    with JSON_FILE.open("r", encoding="utf-8") as input_file:
        students = json.load(input_file)

    print("Original Student list:")
    print_students(students)

    new_student = {
        "F_Name": "Prince",
        "L_Name": "Hubbard",
        "Student_ID": 49261,
        "Email": "phubbard@example.com",
    }
    students.append(new_student)

    print("\nUpdated Student list:")
    print_students(students)

    with JSON_FILE.open("w", encoding="utf-8") as output_file:
        json.dump(students, output_file, indent=4)

    print("\nThe Student.json file was updated.")


if __name__ == "__main__":
    main()
