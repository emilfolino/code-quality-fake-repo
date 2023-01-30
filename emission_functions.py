"""holds all the functions for emissions"""

import emission_data as emda

def search_country(search_word):
    """searches for a list of matching countries"""
    country_list = []

    for i in emda.country_data:
        if str(search_word).lower() in i.lower():
            country_list.append(i)
    if len(country_list) < 1:
        raise ValueError("No country found")
    return country_list

def get_country_year_data_megaton(country, year):
    """returns the year data of a country"""
    countryid = emda.country_data[country]["id"]
    emission = 0
    if int(year) == 1990:
        emission += emda.emission_1990[countryid]
    elif int(year) == 2005:
        emission += emda.emission_2005[countryid]
    elif int(year) == 2017:
        emission += emda.emission_2017[countryid]
    else: 
        raise ValueError

    megaton = emission * 1000000
    return megaton

def get_country_change_for_years(country, year1, year2):
    """calculates the change in percent between 2 years"""
    year1_data = get_country_year_data_megaton(country, year1)
    year2_data = get_country_year_data_megaton(country, year2)
    percent = (year2_data - year1_data) / year1_data * 100
    return round(percent, 2)

def get_country_data(country):
    """Gets the data of a country"""
    name = country
    emission1990 = get_country_year_data_megaton(country, 1990)
    emission2005 = get_country_year_data_megaton(country, 2005)
    emission2017 = get_country_year_data_megaton(country, 2017)
    if(len(emda.country_data[country]["population"]) != 0):
        population1990 = emda.country_data[country]["population"][0]
        population2005 = emda.country_data[country]["population"][1]
        population2017 = emda.country_data[country]["population"][2]
    else:
        population1990 = None
        population2005 = None
        population2017 = None
    
    change90to05 = get_country_change_for_years(country, 1990, 2005)
    change05to17 = get_country_change_for_years(country, 2005, 2017)
    data = dict({"name": name,
            "1990": {"emission": emission1990, "population": population1990},
            "2005": {"emission": emission2005, "population": population2005},
            "2017": {"emission": emission2017, "population": population2017},
            "emission_change": (change90to05, change05to17)})
    return data

def print_country_data(data):
    """Prints the data of a country"""
    if data["1990"]["population"] is None:
        toprint = f"""
        Name: {data["name"]}
        Emission        - 1990: {data["1990"]["emission"]}       2005: {data["2005"]["emission"]}     2017: {data["2017"]["emission"]}
        Population      - Missing population data!
        Emission change - 1990-2005: {data["emission_change"][0]}%   2005-2017: {data["emission_change"][1]}%
        """
        print(toprint)
    else:
        toprint = f"""
        Name: {data["name"]}
        Emission        - 1990: {data["1990"]["emission"]}       2005: {data["2005"]["emission"]}     2017: {data["2017"]["emission"]}
        Population      - 1990: {data["1990"]["population"]}       2005: {data["2005"]["population"]}     2017: {data["2017"]["population"]}
        Emission change - 1990-2005: {data["emission_change"][0]}%   2005-2017: {data["emission_change"][1]}%
        """
        print(toprint)
