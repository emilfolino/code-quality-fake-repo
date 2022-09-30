#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Funktionerna som har med utsläppen att göra."""

import emission_data

def search_country(search_word):
    """Searches data for a country."""
    country_list = []
    for x in emission_data.country_data:
        if search_word.lower() in x.lower():
            country_list.append(x)
    if country_list == []:
        raise ValueError("Country does not exist!")
    return country_list

def get_country_year_data_megaton(country, year):
    """Gets emission data."""
    if year not in ("1990", "2005", "2017"):
        raise ValueError("Wrong year!")
    country_id = emission_data.country_data[country]["id"]
    if year == "1990":
        return emission_data.emission_1990[country_id] * 1000000
    if year == "2005":
        return emission_data.emission_2005[country_id] * 1000000
    return emission_data.emission_2017[country_id] * 1000000
    
def get_country_change_for_years(country, year1, year2):
    """Gets the percentual emission change."""
    return round(((get_country_year_data_megaton(country, year2) - get_country_year_data_megaton(country, year1)) / 
    get_country_year_data_megaton(country, year1))*100, 2)
    
def get_country_data(country_name):
    """Returns all data of a country in a dictionary."""

    none_list = []
    if not emission_data.country_data[country_name]["population"]:
        for _ in range(3):
            none_list.append(None)
    else:
        none_list.append(emission_data.country_data[country_name]["population"][0])
        none_list.append(emission_data.country_data[country_name]["population"][1])
        none_list.append(emission_data.country_data[country_name]["population"][2])

    country_data = {
        "name": country_name,
        "1990": {"emission": get_country_year_data_megaton(country_name, "1990"), "population": none_list[0]},
        "2005": {"emission": get_country_year_data_megaton(country_name, "2005"), "population": none_list[1]}, 
        "2017": {"emission": get_country_year_data_megaton(country_name, "2017"), "population": none_list[2]},
        "emission_change": (get_country_change_for_years(country_name, "1990", "2005"), 
        get_country_change_for_years(country_name, "2005", "2017"))
    }
    return country_data

def print_country_data(data):
    """Prints the country data."""
    
    output = f"{data['name']}\nEmission               - 1990: {data['1990']['emission']}    \
            2005: {data['2005']['emission']}    2017: {data['2017']['emission']}\nEmission change\
        - 1990-2005: {data['emission_change'][0]}%    2005-2017: {data['emission_change'][1]}%\nPopulation (Missing population data!)\
            - 1990: {data['1990']['population']}    2005: {data['2005']['population']}    \
            2017: {data['2017']['population']}"

    if data['1990']['population'] is None:
        print(output)
    else:
        output_else = output.replace("(Missing population data!)", "")
        print(output_else)
