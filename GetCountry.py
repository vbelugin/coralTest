import requests


def get_by_country_code(country_code):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCountryByCountryCode?CountryCode=%s' % country_code)

    countries = []
    country = ""
    for line in response.iter_lines():
        if str(line).find("&lt;name&gt;") < 0: continue
        startpos = str(line).find('&gt;')
        endpos = str(line).find('&lt;/')
        result = str(line)[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            if not result == country:
                country = result
                countries.append(result)
            else:
                continue
    if len(countries) > 1:
        return countries
    else:
        return country


def get_currency_by_country(country):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCurrencyByCountry?CountryName=%s' % country)

    currency = ""
    for line in response.iter_lines():
        if str(line).find("&lt;Currency&gt;") < 0: continue
        startpos = str(line).find('&gt;')
        endpos = str(line).find('&lt;/')
        result = str(line)[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            currency = result
    return currency


def get_currency_by_code(currency_code):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCountryByCurrencyCode?CurrencyCode=%s' % currency_code)

    currency = ""
    for line in response.iter_lines():
        if str(line).find("&lt;Currency&gt;") < 0: continue
        startpos = str(line).find('&gt;')
        endpos = str(line).find('&lt;/')
        result = str(line)[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            currency = result

    return currency


def get_currency_code_by_name(currency_name):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCurrencyCodeByCurrencyName?CurrencyName=%s' % currency_name)

    currencyCodes = []
    currencyCode = ""
    for line in response.iter_lines():
        if str(line).find("&lt;CurrencyCode&gt;") < 0: continue
        startpos = str(line).find('&gt;')
        endpos = str(line).find('&lt;/')
        result = str(line)[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            if not result == currencyCode:
                currencyCode = result
                currencyCodes.append(result)
            else:
                continue

    if len(currencyCodes) > 1:
        return currencyCodes
    else:
        return currencyCode
