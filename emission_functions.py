#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains all functions related to emission.
"""

import emission_data

def search_country(search_word):
    """
    Searches and prints countries.
    """
    country_list = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            country_list.append(country)
    
    if not country_list:
        raise ValueError ("Country does not exist!")
    return country_list

def get_country_year_data_megaton(country, year):
    """
    Gets emission data for a country for 1990, 2005 and 2017.
    """
    country_id = emission_data.country_data[country]["id"]
    
    if year not in ("1990", "2005", "2017"):
        raise ValueError("Wrong year!")
    
    if year == "1990":
        emission = emission_data.emission_1990[country_id]
    elif year == "2005":
        emission = emission_data.emission_2005[country_id]
    else:
        emission = emission_data.emission_2017[country_id]
    emission *= 1000000
    return emission

def get_country_change_for_years(country, year1, year2):
    """
    Gets the emission change in % for a country between two years.
    """
    if country.lower() not in str(emission_data.country_data).lower():
        raise ValueError("Country does not exist!")

    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    
    percentage = round(((100 * (float(emission_year2) / float(emission_year1))) - 100), 2)

    return percentage

def get_country_data(country_name):
    """
    Generates a dictionary with data for a specific country.
    """
    if country_name.lower() not in str(emission_data.country_data).lower():
        raise ValueError("Country does not exist!")
    
    emission_1990 = get_country_year_data_megaton(country_name, "1990")
    emission_2005 = get_country_year_data_megaton(country_name, "2005")
    emission_2017 = get_country_year_data_megaton(country_name, "2017")
    
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
    
    
    country_data = {
        'name': country_name,
        '1990': {'emission': emission_1990, 'population': population_1990},
        '2005': {'emission': emission_2005, 'population': population_2005},
        '2017': {'emission': emission_2017, 'population': population_2017},
        'emission_change': (get_country_change_for_years(country_name, "1990",
                            "2005"),get_country_change_for_years(country_name, "2005", "2017"))
    }
        
    return country_data

def print_country_data(data):
    """
    Prints data from country dictionary.
    """
    if data["1990"]["population"] is None:
        population_1990 = " Missing population data!"
    else:
        population_1990 = " 1990: " + str(data["1990"]["population"])
    
    if data["2005"]["population"] is None:
        population_2005 = " Missing population data!"
    else:
        population_2005 = " 2005: " + str(data["2005"]["population"])
    
    if data["2017"]["population"] is None:
        population_2017 = " Missing population data!"
    else:
        population_2017 = " 2017: " + str(data["2017"]["population"])
    
    print(data["name"])
    print("Emissions - 1990: " + str(data["1990"]["emission"]) + "  2005: "
          + str(data["2005"]["emission"]) + "  2017: " + str(data["2017"]["emission"]))
    print("Population -" + population_1990 + population_2005 + population_2017)
    print("Emission change - 1990-2005: " + str(data["emission_change"][0])
          + "%  2005-2017: " + str(data["emission_change"][1]) + "%")
