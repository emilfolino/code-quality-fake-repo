#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Emission Functions
"""
import emission_data
"""
Import module emission_data
"""

def search_country(search_word):
    """
    Takes user input and checks if string matches one or several country names.
    Returns a list of matching countries.
    Function raises ValueError if string does not match a country.
    """
    countries = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            countries.append(country)
    if not bool(countries):
        raise ValueError
    return countries

def get_country_year_data_megaton(country, year):
    """
    Takes user input (name of country and year) and gets the emissions for that
    year. If year does not exist, a ValueError is raised.
    The function returns the emission in tons.
    """
    emissionId = emission_data.country_data[country]["id"]
    if year == "1990":
        emission = emission_data.emission_1990[emissionId]
    elif year == "2005":
        emission = emission_data.emission_2005[emissionId]
    elif year == "2017":
        emission = emission_data.emission_2017[emissionId]
    else:
        raise ValueError
    return emission * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Takes user input (name of country and two years) and calculates the
    emission change.
    The function returns the emission change with two decimals.
    """
    part1 = get_country_year_data_megaton(country, year1)
    part2 = get_country_year_data_megaton(country, year2)
    diff = (part2 - part1) / part1
    return round(diff * 100, 2)

def get_country_data(country_name):
    """
    Takes user input (name of country) and creates a dictionary (data) with
    all data of the country.
    Function returns dictionary.
    """
    data = {"name": country_name}
    population = emission_data.country_data[country_name]["population"]
    if population:
        popDict = {"1990": population[0], "2005": population[1], "2017": population[2]}
    else:
        popDict = {"1990": None, "2005": None, "2017": None}
    years = ("1990", "2005", "2017")
    for year in years:
        data[year] = {
            "emission": get_country_year_data_megaton(country_name, year),
            "population": popDict[year]
            }
    data["emission_change"] = (get_country_change_for_years(country_name, "1990", "2005"),
    get_country_change_for_years(country_name, "2005", "2017"))
    return data

def print_country_data(data):
    """
    Creates temporary strings and uses them to print information about the
    country that the user inputs.
    """
    emission = "1990: " + str(data["1990"]["emission"]) + "  "
    emission += "2005: " + str(data["2005"]["emission"]) + "  "
    emission += "2017: " + str(data["2017"]["emission"])
    emissionChange = "1990-2005: " + str(data["emission_change"][0]) + "%  "
    emissionChange += "2005-2017: " + str(data["emission_change"][1]) + "%"
    if data["1990"]["population"] is None:
        population = "Missing population data!"
    else:
        population = "1990: " + str(data["1990"]["population"]) + "  "
        population += "2005: " + str(data["2005"]["population"]) + "  "
        population += "2017: " + str(data["2017"]["population"])
    print(data["name"])
    print("Emission        - " + emission)
    print("Emission change - " + emissionChange)
    print("Population      - " + population)
