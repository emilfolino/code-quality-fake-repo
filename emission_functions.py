#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Emission functions
"""

import emission_data

def search_country(word):
    """Returns countries that contains the search string"""
    word = str(word.lower())

    countries = []
    for key in emission_data.country_data:
        countries.append(key)

    countries_searched = []
    for country in countries:
        if word in country.lower():
            countries_searched.append(country)

    if bool(countries_searched):
        return countries_searched
    raise ValueError

def get_country_year_data_megaton(country, year):
    """Gives emission per country and year"""
    try:
        id_ = emission_data.country_data[country]["id"]
    except KeyError:
        return KeyError

    if (year == "1990"):
        result = emission_data.emission_1990[id_]
    elif (year == "2005"):
        result = emission_data.emission_2005[id_]
    elif (year == "2017"):
        result = emission_data.emission_2017[id_]
    else:
        raise ValueError

    result *= 1000000
    return result


def get_country_change_for_years(country, year1, year2):
    """Returns emission change between two years"""
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    change = (emission_year2 - emission_year1)/emission_year1*100
    return round(change, 2)

def get_country_data(country_name):
    """Creates a dictionary with country data"""
    data = {}

    emission_data_1990 = get_country_year_data_megaton(country_name, "1990")
    emission_data_2005 = get_country_year_data_megaton(country_name, "2005")
    emission_data_2017 = get_country_year_data_megaton(country_name, "2017")

    try: 
        population_1990 = emission_data.country_data[country_name]["population"][0]
    except IndexError:
        population_1990 = None
    try:
        population_2005 = emission_data.country_data[country_name]["population"][1]
    except IndexError:
        population_2005 = None
    try:
        population_2017 = emission_data.country_data[country_name]["population"][2]
    except IndexError:
        population_2017 = None

    change1 = get_country_change_for_years(country_name, "1990", "2005")
    change2 = get_country_change_for_years(country_name, "2005", "2017")

    data["name"] = country_name
    data["1990"] = {"emission": emission_data_1990, "population": population_1990}
    data["2005"] = {"emission": emission_data_2005, "population": population_2005}
    data["2017"] = {"emission": emission_data_2017, "population": population_2017}
    data["emission_change"] = (change1, change2)

    return data

def print_country_data(data):
    """Prints data about a country"""
    pop_1990 = data["1990"]["population"]
    if (pop_1990 is None):
        pop_1990 = "Missing population data!"
    pop_2005 = data["2005"]["population"]
    if (pop_2005 is None):
        pop_2005 = "Missing population data!"
    pop_2017 = data["2017"]["population"]
    if (pop_2017 is None):
        pop_2017 = "Missing population data!"

    print(data["name"])
    print("Emission: - 1990: " + str(data["1990"]["emission"]) +
    " 2005: " + str(data["2005"]["emission"]) + " 2017: "  + str(data["2017"]["emission"]))
    print("Emission change: - 1990-2005: " + str(data["emission_change"][0])
    + "% 2005-2017: " + str(data["emission_change"][1]) + "%")
    print("Population: - 1990: " + str(pop_1990) + " 2005: "
    + str(pop_2005) + " 2017: "  + str(pop_2017))

def print_countries_CO2(year, number=False):
    """Prints CO2 emission for countries, in order"""
    data = {}
    for key in emission_data.country_data:
        data[key] = get_country_year_data_megaton(key, year)

    data = dict(sorted(data.items(), key=lambda item: item[1], reverse = True))

    counter = 0
    if (number):
        for key, value in data.items():
            counter += 1
            if (counter <= int(number)):
                print(key + ": " + str(value))
            else:
                break
    else:
        for key, value in data.items():
            print(key + ": " + str(value))


def print_emission_per_capita(year, number=False):
    """Prints emission for countries per capita"""

    data = emission_data.country_data.copy() # Keys: "Sweden", .....

    for key in data.keys():
        emission_1990 = emission_data.emission_1990[data[key]["id"]]
        emission_2005 = emission_data.emission_2005[data[key]["id"]]
        emission_2017 = emission_data.emission_2017[data[key]["id"]]
        emission_tuple = (emission_1990, emission_2005, emission_2017)
        data[key]["emission"] = emission_tuple

    data_copy = data.copy()

    for key in data_copy.keys(): # Pga att data ändrar strl
        if (data[key]["population"] == []):
            data.pop(key)

    if (year == "1990"):
        for key in data.keys():
            data[key]["capita"] = round((data[key]["emission"][0]*1000000 / data[key]["population"][0]), 2)
    elif (year == "2005"):
        for key in data.keys():
            data[key]["capita"] = round((data[key]["emission"][1]*1000000 / data[key]["population"][1]), 2)
    elif (year == "2017"):
        for key in data.keys():
            data[key]["capita"] = round((data[key]["emission"][2]*1000000 / data[key]["population"][2]), 2)
    else:
        raise ValueError

    new_data = {}
    for country in data.keys():
        new_data[country] = data[country]["capita"]

    new_data = dict(sorted(new_data.items(), key=lambda item: item[1], reverse = True))

    counter = 0
    if (number):
        for key, value in new_data.items():
            counter += 1
            if (counter <= int(number)):
                print(key + ": " + str(value))
            else:
                break
    else:
        for key, value in new_data.items():
            print(key + ": " + str(value))

def print_emission_per_area(year, number=False):
    """Prints emission for countries per area"""

    data = emission_data.country_data.copy() # Keys: "Sweden", .....

    for key in data.keys():
        emission_1990 = emission_data.emission_1990[data[key]["id"]]
        emission_2005 = emission_data.emission_2005[data[key]["id"]]
        emission_2017 = emission_data.emission_2017[data[key]["id"]]
        emission_tuple = (emission_1990, emission_2005, emission_2017)
        data[key]["emission"] = emission_tuple

    data_copy = data.copy()

    for key in data_copy.keys(): # Pga att data ändrar strl
        if (data[key]["area"] == 0):
            data.pop(key)

    if (year == "1990"):
        for key in data.keys():
            data[key]["em_ar"] = round((data[key]["emission"][0]*1000000 / data[key]["area"]), 2)
    elif (year == "2005"):
        for key in data.keys():
            data[key]["em_ar"] = round((data[key]["emission"][1]*1000000 / data[key]["area"]), 2)
    elif (year == "2017"):
        for key in data.keys():
            data[key]["em_ar"] = round((data[key]["emission"][2]*1000000 / data[key]["area"]), 2)
    else:
        raise ValueError

    new_data = {}
    for country in data.keys():
        new_data[country] = data[country]["em_ar"]

    new_data = dict(sorted(new_data.items(), key=lambda item: item[1], reverse = True))

    counter = 0
    number = int(number)
    if (number):
        for key, value in new_data.items():
            counter += 1
            if (counter <= int(number)):
                print(key + ": " + str(value))
            else:
                break
    else:
        for key, value in new_data.items():
            print(key + ": " + str(value))
