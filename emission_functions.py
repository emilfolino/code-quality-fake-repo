#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains all the fuctions for dealing with emissions.
"""

import marvin
import emission_data

def search_country(search_word):
    """Function to search for countries containing characters provided by user, case insensitive!"""
    search_results = [country_name for country_name in emission_data.country_data \
        if search_word.lower() in country_name.lower()]
    if not search_results:
        raise ValueError ("Country does not exist!")
    return(search_results)

def get_country_info(country_search_name):
    """Function to get area, id and population of a country from emission_data.py"""
    country_info_tuple_list = [country_tuple for country_tuple in emission_data.country_data.items() \
        if country_search_name.lower() == country_tuple[0].lower()]
    if country_info_tuple_list:
        country_info_dict = country_info_tuple_list[0][1]
        country_info_dict["name"] = country_info_tuple_list[0][0]
    return country_info_dict

def get_country_data(country_search_name):
    """Function to get country data from emission_data.py"""
    country_info = get_country_info(country_search_name)
    country_name = country_info["name"]
    country_data = {"name": country_info["name"]}
    if country_info["population"]:
        country_population_tuple = country_info["population"]
    else:
        country_population_tuple = (None, None, None)

    emission_change_list = []
    emission_years = ("1990", "2005", "2017")
    for i, year in enumerate(emission_years):
        country_data[year] = {"emission": get_country_year_data_megaton(country_name, year), \
            "population": country_population_tuple[i]}
        if i:
            emission_change_list.append(get_country_change_for_years(country_name, emission_years[i-1], year))
    country_data["emission_change"] = tuple(emission_change_list)
    return country_data

def print_country_data(data):
    """Function to present the data from the get_country_data function"""
    marvinu_message = data["name"]
    marvinu_message += "\n  Emission:\t"
    emission_years = ("1990", "2005", "2017")
    emission_change_string = "Emission change:"
    population_string = "Population:\t"
    for i, year in enumerate(emission_years):
        marvinu_message += f"\t{year}: {data[year]['emission']}"
        if i:
            emission_change_string += f" {emission_years[i-1]}-{emission_years[i]}: "
            emission_change_string += f"{float(data['emission_change'][i-1])}%"
        try:
            population_string += f"\t{year}: {int(data[year]['population'])}"
        except TypeError:
            population_string = "Missing population data!"

    marvinu_message += f"\n  {emission_change_string}"
    marvinu_message += f"\n  {population_string}"
    marvin.redraw_marvinu(marvinu_message)

def get_country_year_data_megaton(country, year):
    """Function to get a country's emissions of a specified year, in TONS despite the name of the function!"""
    country_index = get_country_info(country)["id"]
    if not hasattr(emission_data, f"emission_{year}"):
        raise ValueError ("Wrong year!")

    if not country_index:
        raise ValueError ("Country does not exist!")
    emission_tons = getattr(emission_data, f"emission_{year}")[country_index] * 1000000
    return emission_tons

def get_country_change_for_years(country, year1, year2):
    """Function to compare a country's emissions of to specified years"""
    if not hasattr(emission_data, f"emission_{year1}") or not hasattr(emission_data, f"emission_{year2}"):
        raise ValueError ("Wrong year!")

    year_1_emission = get_country_year_data_megaton(country, year1)
    year_2_emission = get_country_year_data_megaton(country, year2)
    return round(year_2_emission / year_1_emission * 100 - 100, 2)

def get_emission_toplist(year, limit):
    """Function to get at toplist of emissions per country"""
    if not hasattr(emission_data, f"emission_{year}"):
        raise ValueError ("Wrong year!")

    emission_toplist = sorted(
        [(getattr(emission_data, f"emission_{year}")[country_data_tuple[1]["id"]], country_data_tuple[0]) \
        for country_data_tuple in emission_data.country_data.items()], reverse = True)
    return(emission_toplist[:limit])

def get_country_year_population(country, year):
    """Function to get the population of a country a specific year"""
    emission_years = ["1990", "2005", "2017"]
    country_population_tuple = emission_data.country_data[country]["population"]
    try:
        return country_population_tuple[emission_years.index(year)]
    except IndexError:
        return None

def get_emission_per_capita_list(year, limit):
    """Function to get a list of emission per capita"""
    if not hasattr(emission_data, f"emission_{year}"):
        raise ValueError ("Wrong year!")

    emission_country_list = [(getattr(emission_data, f"emission_{year}")[country_data_tuple[1]["id"]], \
        country_data_tuple[0]) for country_data_tuple in emission_data.country_data.items()]
    # population_country_list =
    emission_per_capita_list = sorted([(country_tuple[0] / get_country_year_population(country_tuple[1], year), \
        country_tuple[1]) \
        for country_tuple in emission_country_list \
        if get_country_year_population(country_tuple[1], year)], reverse= True)
    return(emission_per_capita_list[:limit])



def get_emission_per_area_list(year, limit):
    """Function to get a list of emission per capita"""
    if not hasattr(emission_data, f"emission_{year}"):
        raise ValueError ("Wrong year!")

    emission_country_list = [(getattr(emission_data, f"emission_{year}")[country_data_tuple[1]["id"]], \
        country_data_tuple[0]) for country_data_tuple in emission_data.country_data.items()]
    # population_country_list =
    emission_per_area_list = sorted([(round(country_tuple[0] / country_tuple[1]["population"], 2), country_tuple[1]) \
        for country_tuple in emission_country_list], reverse = True)
    return(emission_per_area_list[:limit])


def items_to_clean_str(items_list):
    """Function to convert a list of tuple items to a string with line breaks"""
    return "\n  ".join([f"{tuple_item[1]}: {tuple_item[0]}" for tuple_item in items_list])
