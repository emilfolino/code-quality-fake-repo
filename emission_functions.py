#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module that contains the functions for emission commands in main.py
"""
from operator import itemgetter
from emission_data import emission_1990, emission_2005, emission_2017, country_data

def search_country(search_word):
    """
    Function that returns a list of all countries containing search_word
    """
    hit_list = []
    for countries in country_data:
        if str(search_word).lower() in str(countries).lower():
            hit_list.append(countries)
        
    if len(hit_list) < 1:
        raise ValueError("Country does not exist!")

    return hit_list

def get_country_year_data_megaton(country, year):
    """
    Function that returns emission of a country based on year
    """
    getter_function = itemgetter(0)
    emissions = 0
    
    country_dataList = country_data.items()

    for countries in country_dataList:
        if country == getter_function(countries):
            if year == "1990":
                emissions = emission_1990[country_data[getter_function(countries)]["id"]] * 1000000
                break
            elif year == "2005":      
                emissions = emission_2005[country_data[getter_function(countries)]["id"]] * 1000000
                break
            elif year == "2017":
                emissions = emission_2017[country_data[getter_function(countries)]["id"]] * 1000000
                break
            else:
                raise ValueError("Wrong year!")
    return emissions

def get_country_change_for_years(country, year1, year2):
    """
    Function that returns emission change of a country based on two years
    """
    change = 0.0
    emissionYear1 = get_country_year_data_megaton(country, year1)
    emissionYear2 = get_country_year_data_megaton(country, year2)
    change = emissionYear2 / emissionYear1 - 1
    change = change * 10000
    change = round(change) / 100
    return change 

def get_country_data(country_name):
    """
    Function that returns a dictionary containing data of a country
    """
    for countries in country_data:
        if country_name == countries:
            try:
                population1990 = country_data[country_name]["population"][0]
                population2005 = country_data[country_name]["population"][1]
                population2017 = country_data[country_name]["population"][2]
            except IndexError:
                population1990 = None
                population2005 = None
                population2017 = None

            countryInfoDict = {"name": country_name,
                            "1990": {"emission": get_country_year_data_megaton(country_name, 
                                                                               "1990"), 
                                     "population": population1990
                                    },
                            "2005": {"emission": get_country_year_data_megaton(country_name, 
                                                                               "2005"), 
                                     "population": population2005
                                    },
                            "2017": {"emission": get_country_year_data_megaton(country_name, 
                                                                               "2017"),
                                     "population": population2017
                                    },
                            "emission_change": (get_country_change_for_years(country_name, "1990", "2005"), 
                                                get_country_change_for_years(country_name, "2005", "2017"))
                                }

            return countryInfoDict
    raise ValueError("No such country!")

def print_country_data(data):
    """
    Function that takes a dictionary and prints data of a country
    doesnt return anything
    """
    populationString = ""
    if data["1990"]["population"] is None:
        populationString = "Missing population data!"
    else:
        populationString = ("1990: " + str(data["1990"]["population"]) + "\t"
                           "2005: " + str(data["2005"]["population"]) + "\t"
                           "2017: " + str(data["2017"]["population"]))

    print(data["name"] + "\n" +
          "Emission\t\t- " + "1990: " + str(data["1990"]["emission"]) + "\t" +
                               "2005: " + str(data["2005"]["emission"]) + "\t" + 
                               "2017: " + str(data["2017"]["emission"]) + "\n" + 
          "Emission change\t\t- " + "1990-2005: " + str(data["emission_change"][0]) + "%\t" +
                                    "2005-2017: " + str(data["emission_change"][1]) + "%\n" +
          "Population\t\t- " + populationString)
