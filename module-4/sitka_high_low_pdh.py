"""
Title: sitka_high_low_pdh.py
Author: Prince Hubbard
Date: September 3, 2026
Description: Reads Sitka weather data from a CSV file and displays either
             daily high temperatures or daily low temperatures for 2018.
             The menu repeats until the user chooses to exit.
"""

import csv
from datetime import datetime
from pathlib import Path

from matplotlib import pyplot as plt


def read_weather_data():
    """Read and return dates, high temperatures, and low temperatures."""
    filename = Path(__file__).with_name("sitka_weather_2018_simple.csv")
    dates, highs, lows = [], [], []

    with filename.open(encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            dates.append(current_date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))

    return dates, highs, lows


def plot_temperatures(dates, temperatures, temperature_type, color):
    """Display a line graph for the selected temperature data."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, color=color)

    ax.set_title(
        f"Daily {temperature_type} temperatures - 2018", fontsize=24
    )
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=16)

    plt.show()


def display_menu():
    """Display instructions and return the user's menu selection."""
    print("\nSitka Weather Menu")
    print("H - View daily high temperatures")
    print("L - View daily low temperatures")
    print("E - Exit the program")
    return input("Enter H, L, or E: ").strip().lower()


def main():
    """Run the weather graph menu until the user selects exit."""
    dates, highs, lows = read_weather_data()

    while True:
        choice = display_menu()

        if choice in ("h", "high", "highs"):
            plot_temperatures(dates, highs, "high", "red")
        elif choice in ("l", "low", "lows"):
            plot_temperatures(dates, lows, "low", "blue")
        elif choice in ("e", "exit"):
            print("Thank you for using the Sitka Weather program. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter H, L, or E.")


if __name__ == "__main__":
    main()
