"""Module 9 API Assignment.

Author: Prince Hubbard
Course: CSD-325 Advanced Python
Assignment: Module 9 APIs

This program retrieves JSON data from the Open Notify and JSONPlaceholder
APIs. It tests each connection, prints the unformatted response, and then
prints selected fields in a readable format.
"""

import json

import requests


ASTRONAUT_URL = "http://api.open-notify.org/astros.json"
USER_URL = "https://jsonplaceholder.typicode.com/users/1"


def request_json(url):
    """Request JSON data and return the response and decoded object."""
    response = requests.get(url, timeout=15)
    print(f"Connection status for {url}: {response.status_code}")
    response.raise_for_status()
    return response, response.json()


def show_astronauts():
    """Retrieve and display the people currently reported in space."""
    print("OPEN NOTIFY ASTRONAUT TUTORIAL")
    response, astronaut_data = request_json(ASTRONAUT_URL)

    print("\nUnformatted response:")
    print(response.text)

    print("\nFormatted astronaut response:")
    print(f"Number of people in space: {astronaut_data['number']}")
    for person in astronaut_data["people"]:
        print(f"{person['name']} - {person['craft']}")


def show_jsonplaceholder_user():
    """Retrieve and display one sample user from JSONPlaceholder."""
    print("\nJSONPLACEHOLDER USER API")
    response, user_data = request_json(USER_URL)

    print("\nUnformatted response:")
    print(response.text)

    address = user_data["address"]
    company = user_data["company"]
    print("\nFormatted user response:")
    print(f"Name: {user_data['name']}")
    print(f"Username: {user_data['username']}")
    print(f"Email: {user_data['email']}")
    print(
        "Address: "
        f"{address['street']}, {address['suite']}, "
        f"{address['city']} {address['zipcode']}"
    )
    print(f"Phone: {user_data['phone']}")
    print(f"Website: {user_data['website']}")
    print(f"Company: {company['name']}")


def main():
    """Run both API demonstrations without hiding connection failures."""
    try:
        show_astronauts()
    except requests.RequestException as error:
        print(f"Open Notify request failed: {error}")
        print("Verify the URL and internet connection, then run again.")

    try:
        show_jsonplaceholder_user()
    except requests.RequestException as error:
        print(f"JSONPlaceholder request failed: {error}")


if __name__ == "__main__":
    main()
