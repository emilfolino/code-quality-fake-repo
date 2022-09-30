#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Emission functions for marvin"""

import emission_data

def search_country(search_word):
    """Search for part of country name in dictionary and returns matching results"""
    countries_found = []  
    for i in emission_data.country_data:
        if search_word.upper() in i.upper():
            countries_found.append(i)
    if countries_found == []:
        raise ValueError
    return countries_found
    
def get_country_year_data_megaton(country, year):
    """Fetches emission data for a given country in a given year"""
    emission_value = 0

    #Checks if country is in dict and sets emission value per year
    countries = list(emission_data.country_data.keys())
    if country in countries:
        country_id = (emission_data.country_data.get(country, {}).get("id"))
        year_list = ["1990", "2005", "2017"]
        if year == "1990":
            emission_value = emission_data.emission_1990.get(country_id)
        if year == "2005":
            emission_value = emission_data.emission_2005.get(country_id)
        if year == "2017":
            emission_value = emission_data.emission_2017.get(country_id)
        if year not in year_list:
            raise ValueError

    emission_value_multiplied = emission_value * 1000000
    return emission_value_multiplied

def get_country_change_for_years(country, year1, year2):
    """Calculates a country's change of emissions in percentage between to given years"""

    #Gets values for year1 and year2
    first_year = get_country_year_data_megaton(country, year1)
    second_year = get_country_year_data_megaton(country, year2)

    #Calculates difference between year1 and year2 value and converts it to a rounded percentage
    year_difference = ((int(second_year) / int(first_year)) - 1) * 100
    year_difference_clean = round(year_difference, 2)
    
    return year_difference_clean

def get_country_data(country_name):
    """Builds a dictionary with data about a given country"""
    
    #Gets emission data for each year
    emission_1990 = get_country_year_data_megaton(country_name, "1990")
    emission_2005 = get_country_year_data_megaton(country_name, "2005")
    emission_2017 = get_country_year_data_megaton(country_name, "2017")

    #Checks if country is in list and if population is blank it sets value to none, else gets value for each year
    countries = list(emission_data.country_data.keys())
    if country_name in countries:
        population_list = (emission_data.country_data.get(country_name, {}).get("population"))
        if population_list == []:
            population_1990 = None
            population_2005 = None
            population_2017 = None
        else:
            population_1990 = population_list[0]
            population_2005 = population_list[1]
            population_2017 = population_list[2]
    else:
        raise ValueError

    #Parameters holding values for emission change between two years
    diff_1990_2005 = get_country_change_for_years(country_name, "1990", "2005")
    diff_2005_2017 = get_country_change_for_years(country_name, "2005", "2017")
    
    #Creates a dictionary from the data retrieved
    country_data_dict = {
        "name": country_name,
        "1990": {"emission": emission_1990, "population": population_1990},
        "2005": {"emission": emission_2005, "population": population_2005},
        "2017": {"emission": emission_2017, "population": population_2017},
        "emission_change": (diff_1990_2005, diff_2005_2017)
    }
    return country_data_dict

def print_country_data(data):
    """Prints emission data"""

    #Sets display text if population is None
    if data.get("1990", {}).get("population") is None:
        data["1990"]["population"] = "Missing population data!"
    if data.get("2005", {}).get("population") is None:
        data["2005"]["population"] = "Missing population data!"
    if data.get("2017", {}).get("population") is None:
        data["2017"]["population"] = "Missing population data!"

    #Prints the data
    print(str(data.get("name"))
     + "\nEmission        - 1990: " + str(data.get("1990", {}).get("emission"))
     + "   2005: " + str(data.get("2005", {}).get("emission"))
     + "   2017: " + str(data.get("2017", {}).get("emission"))
     + "\nEmission change - 1990-2005: " + (str(list(data.values())[4][0])) + "%"
     + "   2005-2017: " + (str(list(data.values())[4][1])) + "%"
     + "\nPopulation      - 1990: " + str(data.get("1990", {}).get("population"))
     + "   2005: " + str(data.get("2005", {}).get("population"))
     + "   2017: " + str(data.get("2017", {}).get("population")))
