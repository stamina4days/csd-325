"""City and country formatting functions.

Title: Module 7.2 - Test Cases
Author: Prince Hubbard
Date: September 7, 2026
Purpose: Format city and country information with optional population and
         language details.
"""


def city_country(city, country, population=None, language=None):
    """Return a neatly formatted city and country description."""
    location = f"{city.title()}, {country.title()}"

    if population is not None:
        location += f" - population {population}"

    if language:
        location += f", {language.title()}"

    return location


if __name__ == "__main__":
    # Demonstrate the function with each accepted combination of arguments.
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 14094034))
    print(city_country("san juan", "puerto rico", 342259, "spanish"))
