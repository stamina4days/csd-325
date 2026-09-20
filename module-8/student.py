"""Module 8.2 JSON Practice.

Author: Prince Hubbard
Course: CSD-325 Advanced Python
Assignment: Module 8.2

This program reads student records from a JSON file, displays the original
records, appends one fictional student, displays the updated records, and
writes the updated list back to the JSON file.
"""

import json
from pathlib import Path


JSON_FILE = Path(__file__).with_name("student.json")


def print_students(student_list):
    """Print each student record in the required display format."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , Email = {student['Email']}"
        )


def main():
    """Load, display, update, and save the student JSON data."""
    with JSON_FILE.open("r", encoding="utf-8") as json_file:
        students = json.load(json_file)

    print("This is the original Student list.")
    print_students(students)

    new_student = {
        "F_Name": "Prince",
        "L_Name": "Hubbard",
        "Student_ID": 8675309,
        "Email": "prince.hubbard@example.com",
    }

    if new_student not in students:
        students.append(new_student)

    print("\nThis is the updated Student list.")
    print_students(students)

    with JSON_FILE.open("w", encoding="utf-8") as json_file:
        json.dump(students, json_file, indent=4)

    print("\nThe student.json file was updated.")


if __name__ == "__main__":
    main()
