#!/usr/bin/env python3

"""
Emission functions for Marvin
"""

import emission_data

def search_country(search_word):
    """
    Search for countries in country_data
    """
    search_word = search_word.lower()
    countries = []
    for country in emission_data.country_data:
        if search_word in country.lower():
            countries.append(country)
    if len(countries) == 0:
        raise ValueError("Country does not exist!")
    return countries

def get_country_year_data_megaton(country, year):
    """
    Returns emissions in megaton for country and year
    """
    id_number = emission_data.country_data[country]["id"]
    if year == "1990":
        emissions = emission_data.emission_1990[id_number]
    elif year == "2005":
        emissions = emission_data.emission_2005[id_number]
    elif year == "2017":
        emissions = emission_data.emission_2017[id_number]
    else:
        raise ValueError("Wrong year!")
    return emissions * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Calculates difference in emissions between two years for country
    """
    emissions1 = get_country_year_data_megaton(country, year1)
    emissions2 = get_country_year_data_megaton(country, year2)
    return round((emissions2 - emissions1) / emissions1 * 100, 2)

def get_country_data(country_name):
    """
    Gets data for country
    """
    data = {"name": country_name}
    data["1990"] = {"emission": get_country_year_data_megaton(country_name, "1990")}
    data["2005"] = {"emission": get_country_year_data_megaton(country_name, "2005")}
    data["2017"] = {"emission": get_country_year_data_megaton(country_name, "2017")}
    population = emission_data.country_data[country_name]["population"]
    if len(population) > 0:
        data["1990"]["population"] = population[0]
        data["2005"]["population"] = population[1]
        data["2017"]["population"] = population[2]
    else:
        data["1990"]["population"] = None
        data["2005"]["population"] = None
        data["2017"]["population"] = None
    change1 = get_country_change_for_years(country_name, "1990", "2005")
    change2 = get_country_change_for_years(country_name, "2005", "2017")
    data["emission_change"] = change1, change2
    return data

def print_country_data(data):
    """
    Prints data for country
    """
    print(data["name"])
    print("Emission - 1990: {} 2005: {} 2017: {}".format(
        data["1990"]["emission"],
        data["2005"]["emission"],
        data["2017"]["emission"]
    ))
    if data["1990"]["population"]:
        print("Population - 1990: {} 2005: {} 2017: {}".format(
            data["1990"]["population"],
            data["2005"]["population"],
            data["2017"]["population"]
        ))
    else:
        print("Missing population data!")
    print("Emission change - 1990-2005: {}% 2005-2017: {}%".format(
        data["emission_change"][0],
        data["emission_change"][1]
    ))
