#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Emission functions
"""
import emission_data

def search_country(search_word):
    """
    Searches for countris that are similar to the search word in country_data
    """
    country_matches = []
    for key in emission_data.country_data:
        if ''.join(list(search_word.lower())) in ''.join(list(key.lower())):
            country_matches.append(key)

    if country_matches == []:
        raise ValueError

    return country_matches

def get_country_year_data_megaton(country, year):
    """
    Returns a country's emissions for a given year
    """

    valid_years = ['1990', '2005', '2017']
    country_id = emission_data.country_data[country]['id']
    country_emission = 0
    megaton_to_ton_multiplier = 1000000

    if year == '1990':
        country_emission = emission_data.emission_1990[country_id]
    elif year == '2005':
        country_emission = emission_data.emission_2005[country_id]
    else:
        country_emission = emission_data.emission_2017[country_id]


    if year not in valid_years:
        raise ValueError

    country_emission = country_emission * megaton_to_ton_multiplier

    return country_emission



def get_country_change_for_years(country, year1, year2):
    """
    Returns the difference in emissions for a given country between two years
    """
    year1 = get_country_year_data_megaton(country, year1)
    year2 = get_country_year_data_megaton(country, year2)

    percent_difference = round((((year2 - year1) / year1) * 100), 2)

    return percent_difference

def get_country_data(country_name):
    """
    Collects datta for a given country
    """
    valid_years = ['1990', '2005', '2017']
    country_data = {
    'name': 'name',
    '1990': {'emission': 0, 'population': None},
    '2005': {'emission': 0, 'population': None},
    '2017': {'emission': 0, 'population': None},
    'emission_change': ""
    }

    country_data['name'] = country_name

    counter = 0

    for year in valid_years:
        country_data[year]['emission'] = get_country_year_data_megaton(country_name, year)
        try:
            country_data[year]['population'] = emission_data.country_data[country_name]['population'][counter]
        except IndexError:
            continue
        counter += 1


    country_data['emission_change'] = (get_country_change_for_years(
        country_name, '1990', '2005'), get_country_change_for_years(country_name, '2005', '2017'))

    return country_data


def print_country_data(data):
    """
    Prints out the data for a given country
    """

    country_name = data['name']
    emission1990 = data['1990']['emission']
    emission2005 = data['2005']['emission']
    emission2017 = data['2017']['emission']

    population1990 = ""
    population2005 = ""
    population2017 = ""

    if data['1990']['population'] is None:
        population1990 = "Missing population data!"
        population2005 = "Missing population data!"
        population2017 = "Missing population data!"
    else:
        population1990 = data['1990']['population']
        population2005 = data['2005']['population']
        population2017 = data['2017']['population']

    emission_change1 = data['emission_change'][0]
    emission_change2 = data['emission_change'][1]

    data_print = f"""
    {country_name}
    Emission    1990: {emission1990} 2005: {emission2005} 2017: {emission2017}
    Population  1990: {population1990} 2005: {population2005} 2017: {population2017}
    Emission change     1990-2005: {emission_change1}% 2005-2017: {emission_change2}%

    """
    print(data_print)
