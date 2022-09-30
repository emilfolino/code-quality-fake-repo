#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Emission functions for Marin
"""
import emission_data as em_data

def search_country(search_word):
    """ Takes a string as an argument and searches
    the keys in the dictionary em_data.country_data for matches.
    All matches are added to a list and returned. If no matches
    are found a ValueError is raised"""

    country_list = []
    for key in em_data.country_data:
        if search_word.lower() in key.lower():
            country_list.append(key)
    
    if not country_list:
        raise ValueError("Country does not exist!")
    
    return country_list

def get_country_year_data_megaton(country, year):
    """Takes two arguments and fetches the amount 
    of pollution in megaton for a country and year. Raises 
    a value error if data for the year or the country does
    not exist."""
    if year == "1990":
        pollution_data = em_data.emission_1990[em_data.country_data[country]["id"]] 
    elif year == "2005":
        pollution_data = em_data.emission_2005[em_data.country_data[country]["id"]]
    elif year == "2017":
        pollution_data = em_data.emission_2017[em_data.country_data[country]["id"]]
    else: 
        raise ValueError("Wrong year!")

    return pollution_data * 1000000


def get_country_change_for_years(country, year1, year2):
    """Takes three arguments, country, year1 and year2. Fetches pollution data for country 
    for year1 and year2 and calculates the percentage change, returning the result. 
    Raises a value error if country is not found in emission_data.country_data. And raises
    value error from get_country_year_data_megaton if data for year does not exist.
    """

    if country in em_data.country_data:
        try:
            poll_year1 = get_country_year_data_megaton(country, year1)
            poll_year2 = get_country_year_data_megaton(country, year2)

            pollution_change = (poll_year2 / poll_year1 - 1) * 100 
            return round(pollution_change, 2)
        except ValueError as e:
            raise ValueError(str(e)) from e
    else:
        raise ValueError("Country does not exist!")

def get_country_data(country_name):
    """Fetches country data for arg. country_name from emission_data.country_data and adds this data
    together with data about emissions for each year from emission_data and emission change using
    get_country_change_for_years to a dictionary which is returned. 
    """
    data = {}
    if country_name in em_data.country_data:
        data['name'] = country_name
        data['1990'] = {}
        data['2005'] = {}
        data['2017'] = {}
        data['1990']['emission'] = get_country_year_data_megaton(country_name, '1990')
        data['1990']['population'] = \
            em_data.country_data[country_name]['population'][0] if \
                (em_data.country_data[country_name]['population']) else None
        data['2005']['emission'] = get_country_year_data_megaton(country_name, '2005')
        data['2005']['population'] = \
            em_data.country_data[country_name]['population'][1] if \
                (em_data.country_data[country_name]['population']) else None
        data['2017']['emission'] = get_country_year_data_megaton(country_name, '2017')
        data['2017']['population'] = \
            em_data.country_data[country_name]['population'][2] if \
                (em_data.country_data[country_name]['population']) else None
        data['emission_change'] = \
            (get_country_change_for_years(country_name,'1990','2005'), \
                get_country_change_for_years(country_name,'2005','2017'))

    else:
        raise ValueError("Country does not exist!")
    
    return data


def print_country_data(data):
    """Takes a dictionary containing data created by get_country data as argument. 
    Formats and prints the data from the dictionary.
    """
 
    print_string = "{:<15}\n{:<20}{:<25}{:<25}{:<25}\n"\
        .format(data['name'], "Emission:", "- 1990: " + str(data['1990']['emission']), \
            "2005: " + str(data['2005']['emission']), "2017: " + str(data['2017']['emission']))

    if data['1990']["population"]:
        print_string += "{:<20}{:<25}{:<25}{:<25}\n"\
            .format("Population: ", "- 1990: " + str(data['1990']['population']),\
                "2005: " + str(data['2005']['population']), "2017: " + str(data['2017']['population']))
    else:
        print_string += "Missing population data!\n"
        
    print_string += "{:<20}{:<25}{:<25}"\
        .format("Emission change", "- 1990-2005: " + str(data['emission_change'][0]) + "%", \
            "2005-2017: " + str(data['emission_change'][1]) + "%")
    print(print_string)

def print_top_emitters(year, number_of_countries = None):
    """Prints top emitting countries and emission data for a given year.
    Year and number of countries is given as arguments.
    """

    emissions = {}
    
    if year == '1990':
        for key, value in em_data.country_data.items():
            if em_data.emission_1990[value['id']]:
                em_data_temp = em_data.emission_1990[value['id']] * 1000000
                emissions[em_data_temp] = key
    elif year == '2005':
        for key, value in em_data.country_data.items():
            if em_data.emission_2005[value['id']]:
                em_data_temp = em_data.emission_2005[value['id']] * 1000000
                emissions[em_data_temp] = key

    elif year == '2017':
        for key, value in em_data.country_data.items():
            if em_data.emission_2017[value['id']]:
                em_data_temp = em_data.emission_2017[value['id']] * 1000000
                emissions[em_data_temp] = key
    else:
        raise ValueError("No data for year!")

    if not number_of_countries:
        number_of_countries = len(emissions)

    for key in sorted(emissions.keys(), reverse=True)[:number_of_countries]:
        print(emissions[key] + ": " + str(round(key, 2)))

def print_emission_per_capita(year, number_of_countries = None):
    """Prints top emissions per capita for all or a given number of countries for a given year.
    Year and number of countries is given as arguments, number of countries is optional.
    """

    emission_per_capita = {}
    
    if year == '1990':
        for key, value in em_data.country_data.items():
            if value['population']:
                per_capita_em = (em_data.emission_1990[value['id']] * \
                        1000000 / value['population'][0])
                emission_per_capita[per_capita_em] = key
    elif year == '2005':
        for key, value in em_data.country_data.items():
            if value['population']:
                per_capita_em = (em_data.emission_2005[value['id']] * \
                        1000000 / value['population'][1])
                emission_per_capita[per_capita_em] = key
    elif year == '2017':
        for key, value in em_data.country_data.items():
            if value['population']:
                per_capita_em = (em_data.emission_2017[value['id']] * \
                        1000000 / value['population'][2])
                emission_per_capita[per_capita_em] = key
    else:
        raise ValueError("No data for year!")

    if not number_of_countries:
        number_of_countries = len(emission_per_capita)
  
    for key in sorted(emission_per_capita.keys(), reverse=True)[:number_of_countries]:
        print(emission_per_capita[key] + ": " + str(round(key, 2)))

def print_emission_per_area(year, number_of_countries = None):
    """Prints top emissions per area for all or a given number of countries for a given year.
    Year and number of countries is given as arguments, number of countries is optional.
    """
    
    emission_per_area = {}
    
    if year == '1990':
        for key, value in em_data.country_data.items():
            if value['area']:
                per_area_em = (em_data.emission_1990[value['id']] * \
                        1000000 / value['area'])
                emission_per_area[per_area_em] = key

    elif year == '2005':
        for key, value in em_data.country_data.items():
            if value['area']:
                per_area_em = (em_data.emission_2005[value['id']] * \
                        1000000 / value['area'])
                emission_per_area[per_area_em] = key
    elif year == '2017':
        for key, value in em_data.country_data.items():
            if value['area']:
                per_area_em = (em_data.emission_2017[value['id']] * \
                        1000000 / value['area'])
                emission_per_area[per_area_em] = key
    else:
        raise ValueError("No data for year!")

    if not number_of_countries:
        number_of_countries = len(emission_per_area)
  
    for key in sorted(emission_per_area.keys(), reverse=True)[:number_of_countries]:
        print(emission_per_area[key] + ": " + str(round(key, 2)))
