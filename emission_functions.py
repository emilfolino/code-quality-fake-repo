"""
Functions for country data and emission data
"""

import emission_data

def search_country(search_string):
    """
    Searches for a country already existing in a
    dictionary
    """
    country_list = []
    for key in emission_data.country_data:
        if search_string.lower() in key.lower():
            country_list.append(key)
    if len(country_list) == 0:
        raise ValueError("Country does not exist!")
    #country_list = ", ".join(country_list)
    return country_list

def get_country_year_data_megaton(country, year):
    """
    Prints emission for each country
    """
    if year == "1990":
        country = emission_data.country_data.get(country)
        for key, value in emission_data.emission_1990.items():
            if country['id'] == key:
                value = value * 1000000
                return value
    
    elif year == "2005":
        country = emission_data.country_data.get(country)
        for key, value in emission_data.emission_2005.items():
            if country['id'] == key:
                value = value * 1000000
                return value

    elif year == "2017":
        country = emission_data.country_data.get(country)
        for key, value in emission_data.emission_2017.items():
            if country['id'] == key:
                value = value * 1000000
                return value
    
    raise ValueError("Wrong year!")

def get_country_change_for_years(country_change, year1, year2):
    """
    Prints the change in emission between a period
    """
    year_one = get_country_year_data_megaton(country_change, year1)
    year_two = get_country_year_data_megaton(country_change, year2)

    if year_two != year_one:
        try:
            diff = year_two / year_one
            result = (diff * 100) - 100
            result = round(result, 2)
            return result
        except ZeroDivisionError:
            return "Kan inte dela med 0"
    return "0.0%"

def get_country_data(country_name):
    """
    Catches information from an existing dictionary and creates a new
    dictionary
    """
    for key, value in emission_data.country_data.items():
        if country_name in key:
            try:
                population_1990 = value['population'][0]
            except IndexError:
                population_1990 = None
            try:
                population_2005 = value['population'][1]
            except IndexError:
                population_2005 = None
            try:
                population_2017 = value['population'][2]
            except IndexError:
                population_2017 = None
            emiss_1990 = get_country_year_data_megaton(country_name, "1990")
            emiss_2005 = get_country_year_data_megaton(country_name, "2005")
            emiss_2017 = get_country_year_data_megaton(country_name, "2017")
            emiss_change_1990_2005 = get_country_change_for_years(country_name, "1990", "2005")
            emiss_change_2005_2017 = get_country_change_for_years(country_name, "2005", "2017")
    return {
        'name': country_name,
        '1990': {'emission': emiss_1990, 'population': population_1990},
        '2005': {'emission': emiss_2005, 'population': population_2005},
        '2017': {'emission': emiss_2017, 'population': population_2017},
        'emission_change': (emiss_change_1990_2005, emiss_change_2005_2017)
    }

def print_country_data(data):
    """
    Prints all the data from get_country_data
    in a readable format
    """
    if data['1990']['population'] is None:
        data['1990']['population'] = "Missing population data!"
    if data['2005']['population'] is None:
        data['2005']['population'] = "Missing population data!"
    if data['2017']['population'] is None:
        data['2017']['population'] = "Missing population data!"
    print(f"{data['name']} \n"
        f"Emission - 1990: {data['1990']['emission']} "
        f"2005: {data['2005']['emission']} 2017: {data['2017']['emission']}\n"
        f"Emission change - 1990-2005: {data['emission_change'][0]}% 2005-2017: {data['emission_change'][1]}%\n"
        f"Population - 1990: {data['1990']['population']} "
        f"2005: {data['2005']['population']} 2017: {data['2017']['population']}"
    )
