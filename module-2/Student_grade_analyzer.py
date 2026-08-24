"""Analyze a student's test scores and report an average and letter grade."""


def calculate_average(scores):
    """Return the arithmetic mean of a nonempty list of scores."""
    total = sum(scores)
    average = total / len(scores)
    return average


def assign_letter_grade(average):
    """Convert a numeric average to a standard letter grade."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main():
    """Run the grade analyzer with a sample set of scores."""
    scores = [88, 94, 79, 91]
    average = calculate_average(scores)
    letter_grade = assign_letter_grade(average)

    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Letter grade: {letter_grade}")


if __name__ == "__main__":
    main()
