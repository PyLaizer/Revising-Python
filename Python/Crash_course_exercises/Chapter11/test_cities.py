#Exercise 11.1
import unittest
from city_functions import city_info

class CityTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """A test for santiago, Chile"""
        test_city = city_info("santiago","chile")
        self.assertEqual(test_city,"Santiago, Chile-Population ")

    def test_city_country_population(self):
        """A test for Lagos, Nigeria"""
        test_city_pop = city_info("Lagos","Nigeria",150_000_000)  
        self.assertEqual(test_city_pop,"Lagos, Nigeria-Population 150000000")  

    
if __name__ == '__main__':
    unittest.main()    