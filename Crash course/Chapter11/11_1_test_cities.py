import unittest
from city_functions_11_1 import get_formatted_name


class FullNameTest(unittest.TestCase):

    def test_city_country_name(self):
        names = {'rotterdam': 'Nederland', 'Sumy': 'Oekraine', 'New York': 'United States of America'}
        for city in names:
            formatted_string = get_formatted_name(city, names[city])
            self.assertEqual(formatted_string, f"{city.title()}, {names[city].title()}")


if __name__ == '__main__':
    unittest.main()
