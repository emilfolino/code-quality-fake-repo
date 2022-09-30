#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
collection of fuctions
"""

import emission_data

def search_country(in_data):
    '''Search countries in input, return all valid contries'''
    try:
        out_data = []
        for i in emission_data.country_data:
            if in_data.lower() in i.lower():
                out_data.append(i)
        if out_data == []: #no country matched input
            raise ValueError
        return out_data
    except AttributeError as e: # dictionary was inputed
        raise AttributeError from e

def get_country_year_data_megaton(country, year):
    '''Returns emission of a country at a given year'''

    if year == "1990":
        return emission_data.emission_1990[emission_data.country_data[country]['id']] * 1000000
    if year == "2005":
        return emission_data.emission_2005[emission_data.country_data[country]['id']] * 1000000
    if year == "2017":
        return emission_data.emission_2017[emission_data.country_data[country]['id']] * 1000000

    raise ValueError

def get_country_change_for_years(country, year1, year2):
    '''Returns emission change of a country between to given years'''
    try:
        country = search_country(country)[0]
    except IndexError as e: # country does not exist
        raise IndexError from e

    emission1 = get_country_year_data_megaton(country, year1)
    emission2 = get_country_year_data_megaton(country, year2)

    return round((emission2 - emission1) / emission1 * 100, 2)

def get_country_data(country_in):
    '''Gets all data about a country and returns it in a dictionary'''

    try:
        country = search_country(country_in)[0]
    except ValueError as e: #country does not exist
        raise ValueError from e
    except AttributeError as e: # dictionary was inputed
        raise AttributeError from e

    emiss_1990 = get_country_year_data_megaton(country, "1990")
    emiss_2005 = get_country_year_data_megaton(country, "2005")
    emiss_2017 = get_country_year_data_megaton(country, "2017")

    try:
        data = {
                "name": country,
                "1990": {
                        "emission": emission_data.emission_1990[emission_data.country_data[country]['id']] * 1000000, 
                        "population": emission_data.country_data[country]['population'][0]
                        }, 
                "2005": {
                        "emission": emission_data.emission_2005[emission_data.country_data[country]['id']] * 1000000, 
                        "population": emission_data.country_data[country]['population'][1]
                        }, 
                "2017": {
                        "emission": emission_data.emission_2017[emission_data.country_data[country]['id']] * 1000000, 
                        "population": emission_data.country_data[country]['population'][2]
                        }, 
                "emission_change": 
                        (
                        round((emiss_2005 - emiss_1990) / emiss_1990 * 100, 2), 
                        round((emiss_2017 - emiss_2005) / emiss_2005 * 100, 2)
                        )
                }
    except IndexError: #population of country is not listed
        data = {
                "name": country,
                "1990": {
                        "emission": emission_data.emission_1990[emission_data.country_data[country]['id']] * 1000000, 
                        "population": None
                        }, 
                "2005": {
                        "emission": emission_data.emission_2005[emission_data.country_data[country]['id']] * 1000000, 
                        "population": None
                        }, 
                "2017": {
                        "emission": emission_data.emission_2017[emission_data.country_data[country]['id']] * 1000000, 
                        "population": None
                        }, 
                "emission_change": 
                        (
                        round((emiss_2005 - emiss_1990) / emiss_1990 * 100, 2), 
                        round((emiss_2017 - emiss_2005) / emiss_2005 * 100, 2)
                        )
                }
    
    return data

def print_country_data(country):
    '''Prints info about a country in a nice way'''

    try:
        data = get_country_data(country)
        printer1 = "\nCountry: " + data["name"] + "\n\nEmission:\n1990: " + str(data["1990"]["emission"]) 
        printer2 = "\n2005: " + str(data["2005"]["emission"]) + "\n2017: " + str(data["2017"]["emission"])
        if data["1990"]["population"] is None:
            printer3 = "\n\nPopulation:\n"
            printer4 = "Missing population data!"
        else:
            printer3 = "\n\nPopulation:\n1990: " + str(data["1990"]["population"]) + "\n2005: "
            printer4 = str(data["2005"]["population"]) + "\n2017: " + str(data["2017"]["population"]) 
        printer5 = "\n\nEmission change:\n1990-2005: " + str(data["emission_change"][0])
        printer6 = "%\n2005-2017: " + str(data["emission_change"][1]) + "%\n\n"
        printer = printer1 + printer2 + printer3 + printer4 + printer5 + printer6 
        # behöver göra detta pga validatorn klagar på rader med över 120 characters

    except ValueError: # non-valid country
        printer = "Country does not exist!"
        
    except AttributeError: # dictionary was inputed
        printer1 = "\nCountry: " + country["name"] + "\n\nEmission:\n1990: " + str(country["1990"]["emission"]) 
        printer2 = "\n2005: " + str(country["2005"]["emission"]) + "\n2017: " + str(country["2017"]["emission"])
        if country["1990"]["population"] is None:
            printer3 = "\n\nPopulation:\n"
            printer4 = "Missing population data!"
        else:
            printer3 = "\n\nPopulation:\n1990: " + str(country["1990"]["population"]) + "\n2005: "
            printer4 = str(country["2005"]["population"]) + "\n2017: " + str(country["2017"]["population"]) 
        printer5 = "\n\nEmission change:\n1990-2005: " + str(country["emission_change"][0])
        printer6 = "%\n2005-2017: " + str(country["emission_change"][1]) + "%\n\n"
        printer = printer1 + printer2 + printer3 + printer4 + printer5 + printer6
        # behöver göra detta pga validatorn klagar på rader med över 120 characters

    print(printer)
