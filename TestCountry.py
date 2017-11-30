import unittest
from xml.etree.ElementTree import ElementTree

import GetCountry


class TestCountry(unittest.TestCase):
    def setUp(self): pass

    def test_get_country(self):
        country = GetCountry.get_by_country_code('qa')
        self.assertTrue(str(country).lower().startswith('qa'))

    def test_currency_by_country(self):
        country = GetCountry.get_by_country_code('qa')
        currency = GetCountry.get_currency_by_country(country)
        self.assertTrue(str(currency) == "Rial")

    def test_currency_by_code(self):
        country = GetCountry.get_by_country_code('qa')
        currency = GetCountry.get_currency_by_code('qar')
        self.assertTrue(str(currency) == GetCountry.get_currency_by_country(country))

    def test_currency_code_by_name(self):
        code = 'qar'
        currency_name = GetCountry.get_currency_by_code(code)
        currency_code = GetCountry.get_currency_code_by_name(currency_name)
        print(currency_code)
        check = False
        for cd in currency_code:
            if cd.lower() == code:
                check = True
        self.assertTrue(check)


if __name__ == '__main__':
    unittest.main()
