"""Unit tests for the city_functions module.

Title: Module 7.2 - Test Cases
Author: Prince Hubbard
Date: September 7, 2026
Purpose: Verify that city_country() correctly formats a city and country when
         optional information is not provided.
"""

import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Test cases for the city_country() function."""

    def test_city_country(self):
        """Verify that Santiago and Chile return the expected string."""
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
