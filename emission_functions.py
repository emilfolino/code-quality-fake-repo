"""
Functions for emission
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import emission_data


def search_country(search_word):
    """
    Search for the country in emissions data and return as a list
    """

    country_list =[]
    dict_contry= emission_data.country_data

    for key in dict_contry:
        if search_word.lower() in key.lower():
            country_list.append(key)

    if country_list== []:
        raise ValueError("Country does not exist!")

    return country_list


def get_country_year_data_megaton(country, year):
    """
    Return the emission from a country a specific year, in ton
    """

    if year == "1990":
        emission = emission_data.emission_1990[emission_data.country_data[country]["id"]]
        emission_ton = emission*1000000

    elif year== "2005":
        emission = emission_data.emission_2005[emission_data.country_data[country]["id"]]
        emission_ton = emission*1000000

    elif year== "2017":
        emission = emission_data.emission_2017[emission_data.country_data[country]["id"]]
        emission_ton = emission*1000000

    else:
        raise ValueError("Wrong year!")


    return emission_ton


def get_country_change_for_years(country, year1, year2):
    """
    Return the difference in emission between two years for a specific country
    """

    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2= get_country_year_data_megaton(country, year2)

    difference= emission_year2 -emission_year1
    difference_perc= (difference/emission_year1)*100


    return round(difference_perc, 2)

def get_country_data(country_name):
    """
    Return a dictionary with information of the specific country
    """

    try:
        population_1990= emission_data.country_data[country_name]["population"][0]
        population_2005= emission_data.country_data[country_name]["population"][1]
        population_2017= emission_data.country_data[country_name]["population"][2]

    except IndexError:
        population_1990=None
        population_2005=None
        population_2017=None


    emission_1990= get_country_year_data_megaton(country_name, "1990")
    emission_2005= get_country_year_data_megaton(country_name, "2005")
    emission_2017= get_country_year_data_megaton(country_name, "2017")

    emission_change1= get_country_change_for_years(country_name, "1990", "2005")
    emission_change2= get_country_change_for_years(country_name, "2005", "2017")

    country_info = {
    'name': country_name,
    '1990': {'emission': emission_1990, 'population':population_1990 },
    '2005': {'emission': emission_2005, 'population':population_2005 },
    '2017': {'emission':emission_2017 , 'population': population_2017},
    'emission_change': (emission_change1, emission_change2)
    }

    return country_info


def print_country_data(data):
    """
    Format the data from a dictionary and print it out
    """
    name = data["name"]
    emission_1990= data["1990"]["emission"]
    emission_2005=data["2005"]["emission"]
    emission_2017=data["2017"]["emission"]

    emission_ch_1990_2005=data["emission_change"][0]
    emission_ch_1990_2017= data["emission_change"][1]

    population_1990= data["1990"]["population"]
    population_2005= data["2005"]["population"]
    population_2017= data["2017"]["population"]

    if population_1990 and population_2005 and population_2017 is not None:
        country_data_string = f"{name} \n\
Emission - 1990: {emission_1990}  2005: {emission_2005}  2017: {emission_2017}\n\
Population - 1990: {population_1990}  2005: {population_2005}  2017: {population_2017}\n\
Emission_change - 1990-2005: {emission_ch_1990_2005}%   2005-2017: {emission_ch_1990_2017}%"

    else:
        country_data_string= f"{name} \n\
Emission - 1990: {emission_1990}  2005: {emission_2005}  2017: {emission_2017}\n\
Population - Missing population data!\n\
Emission_change - 1990-2005: {emission_ch_1990_2005}%   2005-2017: {emission_ch_1990_2017}%"


    print(country_data_string)

"""
     {
        name: "",
        "Emission":{"1990": data["1990"]["emission"], "2005":data["2005"]["emission"], "2017":data["2017"]["emission"]},
        "Population": {"1990": data["1990"]["population"], "2005": data["2005"]["population"],"2017": data["2017"]["population"]},
        "Emission change": {"1990-2005":data["emission_change"][0], "2005-2017":data["emission_change"][1]}
        }

    if country_data["Population"]["1990"] is None:
        country_data["Population"]["1990"] = "Missing population data!"

    if country_data["Population"]["2005"] is None:
        country_data["Population"]["2005"] = "Missing population data!"

    if country_data["Population"]["2017"] is None:
        country_data["Population"]["2017"] = "Missing population data!"

    for key, value in country_data.items():
        print(key, value)
"""
