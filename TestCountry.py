import unittest

import GetCountry


class TestCountry(unittest.TestCase):
    def setUp(self): pass

    # Step#1 Invoke GetCountryByCountryCode to get country by CountryCode = "qa", assert test results
    def test_get_country(self):
        country = GetCountry.get_by_country_code('qa')
        self.assertTrue(str(country).lower().startswith('qa'))

    # Step#2 Using data from Step#1 invoke GetCurrencyByCountry, assert test results
    def test_currency_by_country(self):
        country = GetCountry.get_by_country_code('qa')
        currency = GetCountry.get_currency_by_country(country)
        self.assertTrue(str(currency) == "Rial")

    # Step#3 Using data from step#2 invoke GetCountryByCurrencyCode, assert that data from step#2 are equal to data from step#3
    def test_currency_by_code(self):
        country = GetCountry.get_by_country_code('qa')
        currency = GetCountry.get_currency_by_code('qar')
        self.assertTrue(str(currency) == GetCountry.get_currency_by_country(country))

    # Step#4 Using data from step#3 invoke GetCurrencyCodeByCurrencyName, assert that    CurrencyCode for requested Currency is present in Response
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
