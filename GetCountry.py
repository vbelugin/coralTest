import requests


def get_by_country_code(country_code):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCountryByCountryCode?CountryCode=%s' % country_code)

    fname = 'countries.xml'

    fhandle = open(fname, "w")
    fhandle.write(response.text)
    fhandle.close()

    fh = open(fname)
    countries = []
    country = ""
    for line in fh:
        if line.find("&lt;name&gt;") < 0: continue
        startpos = line.find('&gt;')
        endpos = line.find('&lt;/')
        result = line[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            if not result == country:
                country = result
                countries.append(result)
            else:
                continue
    fh.close()
    if len(countries) > 1:
        return countries
    else:
        return country


def get_currency_by_country(country):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCurrencyByCountry?CountryName=%s' % country)

    fname = 'countries.xml'

    fhandle = open(fname, "w")
    fhandle.write(response.text)
    fhandle.close()

    fh = open(fname)
    currency = ""
    for line in fh:
        if line.find("&lt;Currency&gt;") < 0: continue
        startpos = line.find('&gt;')
        endpos = line.find('&lt;/')
        result = line[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            currency = result
    fh.close()
    return currency

def get_currency_by_code(currency_code):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCountryByCurrencyCode?CurrencyCode=%s' % currency_code)

    fname = 'countries.xml'

    fhandle = open(fname, "w")
    fhandle.write(response.text)
    fhandle.close()

    fh = open(fname)
    currency = ""
    for line in fh:
        if line.find("&lt;Currency&gt;") < 0: continue
        startpos = line.find('&gt;')
        endpos = line.find('&lt;/')
        result = line[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            currency = result
    fh.close()
    return currency

def get_currency_code_by_name(currency_name):
    response = requests.get(
        'http://www.webservicex.net/country.asmx/GetCurrencyCodeByCurrencyName?CurrencyName=%s' % currency_name)

    fname = 'countries.xml'

    fhandle = open(fname, "w")
    fhandle.write(response.text)
    fhandle.close()

    fh = open(fname)
    currencyCodes = []
    currencyCode = ""
    for line in fh:
        if line.find("&lt;CurrencyCode&gt;") < 0: continue
        startpos = line.find('&gt;')
        endpos = line.find('&lt;/')
        result = line[startpos:endpos].strip('&gt;')
        if len(result) > 0:
            if not result == currencyCode:
                currencyCode = result
                currencyCodes.append(result)
            else:
                continue

    fh.close()
    if len(currencyCodes) > 1:
        return currencyCodes
    else:
        return currencyCode