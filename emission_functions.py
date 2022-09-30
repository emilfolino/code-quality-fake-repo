#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for Marvin4
"""

from operator import itemgetter
import emission_data as e_data


YEARS_WITH_DATA = ['1990', '2005', '2017']


def search_country(search_word):
    """
    search for all countries that matches search_word.
    throws ValueError('Country does not exist!') if no match.
    """

    every_match = [
        country for country in e_data.country_data
        if search_word.lower() in country.lower()]

    if not every_match:
        raise ValueError('Country does not exist!')
    return every_match


def get_country_year_data_megaton(country, year):
    """
    get co2 emissions for a specific year/country
    throws ValueError('Wrong year!') or ValueError('Country does not exist!')
    """

    try:
        country_id = e_data.country_data[country]['id']
    except KeyError as e:
        raise ValueError('Country does not exist!') from e

    emission = 0
    if year == '1990':
        emission = e_data.emission_1990[country_id] * 1000000
    elif year == '2005':
        emission = e_data.emission_2005[country_id] * 1000000
    elif year == '2017':
        emission = e_data.emission_2017[country_id] * 1000000
    else:
        raise ValueError('Wrong year!')

    return emission


def get_country_change_for_years(country, year1, year2):
    """
    Get difference in emissions from year2 relative to year1 in %.
    throws ValueError('Wrong year!') or ValueError('Country does not exist!')
    """ 

    first_year = 0
    second_year = 0
    try:
        first_year = get_country_year_data_megaton(country, year1)
        second_year = get_country_year_data_megaton(country, year2)
    except ValueError as e:
        raise ValueError(e) from e 

    # multiplied by -1 for correct output
    difference = round((first_year - second_year) * (-100) / first_year, 2)
    
    return difference


def get_country_data(country_name):
    """
    get all data about a country.
    Throws ValueError('Country does not exist!')
    """

    if country_name in e_data.country_data.keys():
        country_data = {'name': country_name}
    else:
        raise ValueError('Country does not exist!')

    for i, year in enumerate(YEARS_WITH_DATA):
        try:
            pop_data = e_data.country_data[country_name]['population'][i]
        except IndexError:
            pop_data = None

        country_data[year] = {
            'emission' : get_country_year_data_megaton(country_name, year),
            'population' : pop_data
        }

    country_data['emission_change'] = (
        get_country_change_for_years(country_name, '1990', '2005'),
        get_country_change_for_years(country_name, '2005', '2017')
    )

    return(country_data)


def print_country_data(data):
    """
    print all the data about a country.
    """

    country_data = data
    country_output = 'name: ' + country_data['name']
    emission_output = 'Emission   - '
    pop_output = 'Population - '
    emission_change_output = 'Emission change - '

    for year in (YEARS_WITH_DATA):
        emission_output += year + ': ' + str(country_data[year]['emission']) + '  '
        size_of_pop = country_data[year]['population']
        if size_of_pop is None:
            pop_output += year + ': ' + 'Missing population data!'
        else:
            pop_output += year + ': ' + str(size_of_pop) + '  '

    emission_change_output += (
        '1990-2005: ' + str(country_data['emission_change'][0]) + '%   ' + \
        '2005-2017: ' + str(country_data['emission_change'][1]) + '%')

    print(f"{country_output}\n")
    print(f"{emission_output}\n")
    print(f"{pop_output}\n")
    print(f"{emission_change_output}\n")


def print_sorted_values(unsorted_dict, nr_of_countries):
    """
    format output
    """
    output_string = ''
    list_unsorted = unsorted_dict.items()
    sorted_list = sorted(list_unsorted, key=itemgetter(1), reverse=True)

    if nr_of_countries == 1:
        for country, value in sorted_list:
            output_string += country + ': ' + str(value) + '\n'
    else:
        for i in range(nr_of_countries):
            output_string += str(sorted_list[i][0]) + ': ' \
                        + str(sorted_list[i][1]) + '\n'

    return output_string


def get_emission_area(year, nr_of_countries=1):
    """
    return name of country : emmision/area of specified values
    """
    if nr_of_countries < 1 or not isinstance(nr_of_countries, int):
        raise ValueError('Value need to be an int >= 1')

    dict_with_names = {}
    country_id = int
    emission = float
    area = float
    emission_data_x = {}

    if year == '1990':
        emission_data_x = e_data.emission_1990
    elif year == '2005':
        emission_data_x = e_data.emission_2005
    elif year == '2017':
        emission_data_x = e_data.emission_2017
    else:
        raise ValueError('No data for that year')

    for key in e_data.country_data.items():
        country_id = key[1]['id']
        emission = emission_data_x[country_id] * 1000000
        area = key[1]['area']
        if area > 0:
            emission_area = emission / area
            dict_with_names[key[0]] = round(emission_area, 2)

    return print_sorted_values(dict_with_names, nr_of_countries)


def get_emission_capita(year, nr_of_countries):
    """
    return name of country : emission/capita of specified values
    """
    if nr_of_countries < 1 or not isinstance(nr_of_countries, int):
        raise ValueError('Value need to be an int >= 1')

    dict_with_names = {}
    country_id = int
    emission = float
    population = int
    population_index = 0
    emission_data_x = {}

    if year == '1990':
        emission_data_x = e_data.emission_1990
    elif year == '2005':
        emission_data_x = e_data.emission_2005
        population_index = 1
    elif year == '2017':
        emission_data_x = e_data.emission_2017
        population_index = 2
    else:
        raise ValueError('No data for that year')
    
    for key in e_data.country_data.items():
        country_id = key[1]['id']
        emission = emission_data_x[country_id] * 1000000
        try:
            population = key[1]['population'][population_index]
            emission_capita = emission / population
            dict_with_names[key[0]] = round(emission_capita, 2)
        except IndexError:
            continue
    return print_sorted_values(dict_with_names, nr_of_countries)


def get_emission_max_value(year, nr_of_countries):
    """
    return name of country : emission of specified values
    """
    if nr_of_countries < 1 or not isinstance(nr_of_countries, int):
        raise ValueError('Value need to be an int >= 1')

    dict_with_names = {}
    country_id = int
    emission = float
    emission_data_x = {}

    if year == '1990':
        emission_data_x = e_data.emission_1990
    elif year == '2005':
        emission_data_x = e_data.emission_2005
    elif year == '2017':
        emission_data_x = e_data.emission_2017
    else:
        raise ValueError('No data for that year')
    
    for key in e_data.country_data.items():
        country_id = key[1]['id']
        emission = emission_data_x[country_id] * 1000000
        dict_with_names[key[0]] = round(emission, 2)

    return print_sorted_values(dict_with_names, nr_of_countries)
