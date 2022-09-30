#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions to handle data from emission_data.py to main.py
"""

from operator import itemgetter
from emission_data import country_data
from emission_data import emission_1990, emission_2005, emission_2017


# def error_handler_country(search_word):
#     """
#     Throws exception if country name not in country list
#     """

#     comp_list = [key for key in country_data if search_word.lower()
#                  in key.lower()]

#     if len(comp_list) == 0:
#         raise ValueError


# def error_handler_year(year):
#     """
#     Throws exception if year not in dataset
#     """
#     years_present = ['1990', '2005', '2017']
#     if year not in years_present:
#         raise ValueError

def country_data_year(country_id, year):
    """
    Returns emission for country in year
    """
    result = 0
    if year == '1990':
        result = emission_1990[country_id]
    elif year == '2005':
        result = emission_2005[country_id]
    elif year == '2017':
        result = emission_2017[country_id]
    return result * 1000000


def get_population(country, index):
    """
    Returns population if present else return null
    """
    if len(country_data[country]['population']) > 0:
        return country_data[country]['population'][index]

    return None


def population_check(population):
    """
    checks if population data exists, if not, returns string
    """
    if population is None:
        return 'Missing population data!'

    return population


def search_country(search_word):
    """
    Searches keys in dict country_data and returns all keys where search_word is
    present. Returns list of all keys where string was found
    """
    country_list = []

    for key in country_data:

        if search_word.lower() in key.lower():
            country_list.append(key)

    if len(country_list) == 0:
        raise ValueError

    return country_list


def get_country_year_data_megaton(country, year):
    """
    Finds and returns the emission data for a given country in given year
    """
    country_id = country_data[country]['id']

    years_present = ['1990', '2005', '2017']
    if year not in years_present:
        raise ValueError

    return country_data_year(country_id, year)


def get_country_change_for_years(country, year1, year2):
    """
    Finds emission for a country for two given years and returns change in %
    """
    country_id = country_data[country]['id']

    years_present = ['1990', '2005', '2017']
    if year1 not in years_present or year2 not in years_present:
        raise ValueError

    year1_data = country_data_year(country_id, year1)
    year2_data = country_data_year(country_id, year2)
    result = (year2_data - year1_data) / year1_data

    return round(result * 100, 2)


def get_country_data(country):
    """
    Constructs a dict with data for the country
    """
    country_id = country_data[country]['id']

    country_dict = {
        'name': country,
        '1990': {'emission': country_data_year(country_id, '1990'),
                 'population': get_population(country, 0)},
        '2005': {'emission': country_data_year(country_id, '2005'),
                 'population': get_population(country, 1)},
        '2017': {'emission': country_data_year(country_id, '2017'),
                 'population': get_population(country, 2)},
        'emission_change': (get_country_change_for_years(country, '1990', '2005'),
                            get_country_change_for_years(country, '2005', '2017'))
    }

    print_country_data(country_dict)
    return country_dict


def print_country_data(dataset):
    """
    Prints data in set format
    """
    print(dataset['name'])

    print(f"Emission            - 1990: {dataset['1990']['emission']}   " +
          f"2005: {dataset['2005']['emission']}    " +
          f"2017: {dataset['2017']['emission']}")

    print(f"Emission change     - 1990-2005: {dataset['emission_change'][0]}%" +
          f"    2005-2017: {dataset['emission_change'][1]}%")

    print(f"Population - 1990: {population_check(dataset['1990']['population'])}"
          + f"  2005: {population_check(dataset['2005']['population'])}"
          + f"  2017: {population_check(dataset['2017']['population'])}")


def country_data_toplist(year, top=None):
    """
    Prints emission data for all countries for given year sorted
    by most and descending
    """
    dataset = {}

    years_present = ['1990', '2005', '2017']
    if year not in years_present:
        raise ValueError

    # Use country_data to get country names and country ids
    # Use country id to get emissions for given year using country_year_data
    # Populate dataset dict as key=countryname and value=emission
    for key, item in country_data.items():
        country_id = item['id']
        emissions = round(country_data_year(country_id, year), 2)
        dataset[key] = emissions

    sorted_dataset = sorted(
        dataset.items(), key=itemgetter(1), reverse=True)

    # If no value for top was given, print entire list
    if top is None:

        for i, _ in enumerate(sorted_dataset):
            print(f"{sorted_dataset[i][0]}: {sorted_dataset[i][1]}")

    # If value for top is given, print range(top) from dataset
    else:
        for i in range(int(top)):
            print(f"{sorted_dataset[i][0]}: {sorted_dataset[i][1]}")


def emission_capita(year, top=None):
    """
    Prints emissions per capita for all countries in given year if top not given
    Prints emission per capitta for countries in range(top) if top given
    """
    dataset = {}

    years_present = ['1990', '2005', '2017']
    if year not in years_present:
        raise ValueError

    # If population data is present, do following:
    # Use country_data to get country names and country ids
    # Use country id to get emissions for given year using country_year_data
    # Divide emissions with population
    # Populate dataset dict as key=countryname and value=emission/population
    if year == '1990':
        index_year = 0
    elif year == '2005':
        index_year = 1
    else:
        index_year = 2

    for key, item in country_data.items():
        if get_population(key, index_year) is not None:
            country_id = item['id']
            emissions = country_data_year(country_id, year)
            population = get_population(key, index_year)
            dataset[key] = round((emissions / population), 2)

    sorted_dataset = sorted(
        dataset.items(), key=itemgetter(1), reverse=True)

    # If no value for top was given, print entire list
    if top is None:

        for i, _ in enumerate(sorted_dataset):
            print(f"{sorted_dataset[i][0]}: {sorted_dataset[i][1]}")

    # If value for top is given, print range(top) from dataset
    else:
        for i in range(int(top)):
            print(f"{sorted_dataset[i][0]}: {sorted_dataset[i][1]}")


def emission_area(year, top=None):
    """
    Prints emissions per area for all countries in given year i top not given
    Prints emissions per are for countries in range(top) if top given
    """

    dataset = {}

    years_present = ['1990', '2005', '2017']
    if year not in years_present:
        raise ValueError

    # If area data is present, do following:
    # Use country_data to get country names and country ids
    # Use country id to get emissions for given year using country_year_data
    # Divide emissions with are
    # Populate dataset dict as key=countryname and value=emission/area

    for key, item in country_data.items():
        if item['area'] != 0:
            country_id = item['id']
            emissions = country_data_year(country_id, year)
            area = item['area']
            dataset[key] = round((emissions / area), 2)

    sorted_dataset = sorted(
        dataset.items(), key=itemgetter(1), reverse=True)

    # If no value for top was given, print entire list
    if top is None:

        for i, _ in enumerate(sorted_dataset):
            print(f"{sorted_dataset[i][0]}: {sorted_dataset[i][1]}")

    # If value for top is given, print range(top) from dataset
    else:
        for i in range(int(top)):
            print(f"{sorted_dataset[i][0]}: {sorted_dataset[i][1]}")
