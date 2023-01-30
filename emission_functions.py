"""Emission data fuinctions"""

import emission_data


def parseData():
    """Parses data"""
    cData = emission_data.country_data.copy()
    for _, c in cData.items():
        c["emission_1990"] = emission_data.emission_1990[c["id"]] or -1
        c["emission_2005"] = emission_data.emission_2005[c["id"]] or -1
        c["emission_2017"] = emission_data.emission_2017[c["id"]] or -1
    return cData


def search_country(search: str):
    """Seaches for countries"""
    countries = list(parseData().keys())
    countries = list(
        filter(lambda x: (search.lower() in x.lower()), countries))
    if(len(countries) == 0):
        raise ValueError
    return list(countries)


def get_country_year_data_megaton(country: str, _year: str):
    """Get tons of emmisssion"""
    year = int(_year)
    if(year in [1990, 2017, 2005]):
        data = parseData()
        return data[country]["emission_{}".format(year)]*1000000
    raise ValueError


def get_country_change_for_years(country: str, _year1: str, _year2: str):
    """Get difftrancve in porecent"""
    year1 = int(_year1)
    year2 = int(_year2)
    year1Data = get_country_year_data_megaton(country, year1)
    year2Data = get_country_year_data_megaton(country, year2)
    diff = ((year2Data - year1Data)/year1Data)*100
    return round(diff, 2)


def get_country_data(country: str):
    """Get data for country"""
    data = parseData()
    out = {}
    out["name"] = country
    out["1990"] = {"emission": get_country_year_data_megaton(
        country, 1990)}
    out["2005"] = {"emission": get_country_year_data_megaton(
        country, 2005)}
    out["2017"] = {"emission": get_country_year_data_megaton(
        country, 2017)}

    if(data[country]["population"]):
        out["1990"]["population"] = data[country]["population"][0]
        out["2005"]["population"] = data[country]["population"][1]
        out["2017"]["population"] = data[country]["population"][2]
    else:
        out["1990"]["population"] = None
        out["2005"]["population"] = None
        out["2017"]["population"] = None
    out["emission_change"] = (get_country_change_for_years(
        country, 1990, 2005), get_country_change_for_years(country, 2005, 2017))
    return out


def print_country_data(data):
    """Prints data"""
    print(data["name"])
    print(f"1990: {data['1990']['emission']}")
    print(f"1990: {data['1990']['population'] or 'Missing population data!'}")
    print(f"2005: {data['2005']['emission']}")
    print(f"2005: {data['2005']['population']or 'Missing population data!'}")
    print(f"2017: {data['2017']['emission']}")
    print(f"2017: {data['2017']['population']or 'Missing population data!'}")
    print(f"1990-2005: {data['emission_change'][0]}%")
    print(f"2005-2017: {data['emission_change'][1]}%")
