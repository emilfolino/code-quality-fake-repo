#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module with all the functions concerning the CO2 data for marvin4
"""
import emission_data as e_data
MEGA = 1000000

#Menyval12:
def search_country(fun_search_word):
    """
    function that searches the db for matching countries
    """
    country_keys = e_data.country_data.keys()
    matching_countries = []
    for country_name in country_keys:
        if fun_search_word.casefold() in country_name.casefold():
            matching_countries.append(country_name)
    if not matching_countries:
        raise ValueError("Country does not exist!")

    return matching_countries


#Menyval13:
def get_country_year_data_megaton(country, year):
    """
    finds the emissions for the input year and country in e_data and returns it
    """
    years = ["1990", "2005", "2017"]
    year_data = None

    if country not in e_data.country_data.keys():
        raise ValueError("Country doesn't exist!")
    if year not in years:
        raise ValueError("Wrong year!")

    country_id = e_data.country_data[country]["id"]
    e_data_years = [e_data.emission_1990[country_id],
                   e_data.emission_2005[country_id],
                   e_data.emission_2017[country_id]]

    for i, value in enumerate(years):
        if value == year:
            year_data = e_data_years[i]

    emissions = year_data
    return emissions*MEGA

def get_country_change_for_years(country, year1, year2):
    """
    Returns the difference of emissions between the two given years of the
    specified country.
    """
    try:
        co2_year1 = get_country_year_data_megaton(country, year1)
        co2_year2 = get_country_year_data_megaton(country, year2)
    except ValueError as e:
        raise e
    dif_years = (((co2_year2-co2_year1)/co2_year1)*100)
    return (round(dif_years, 2))


#Menyval14:

def get_country_data(country_name):
    """
    Gets the info from emission_data and creates a dict by the given country
    """
    try:
        dict_c_data = {
                        'name': country_name,
                        '1990': {'emission': None, 'population': None},
                        '2005': {'emission': None, 'population': None},
                        '2017': {'emission': None, 'population': None},
                        'emission_change': None
                       }
        e_1990 = get_country_year_data_megaton(country_name, "1990")
        e_2005 = get_country_year_data_megaton(country_name, "2005")
        e_2017 = get_country_year_data_megaton(country_name, "2017")
        population = e_data.country_data[country_name]["population"]
        #area = e_data.country_data[country_name]["area"]
        change1 = get_country_change_for_years(country_name, "1990", "2005")
        change2 = get_country_change_for_years(country_name, "2005", "2017")

        dict_c_data["1990"]["emission"] = e_1990
        dict_c_data["2005"]["emission"] = e_2005
        dict_c_data["2017"]["emission"] = e_2017
        if population:
            dict_c_data["1990"]["population"] = population[0]
            dict_c_data["2005"]["population"] = population[1]
            dict_c_data["2017"]["population"] = population[2]
        dict_c_data["emission_change"] = (change1, change2)

        return dict_c_data

    except ValueError as e:
        raise e


def print_country_data(data):
    """
    Formats and prints the data given by function get_country_data
    """
    print(data["name"])
    years = ["1990", "2005", "2017"]
    for i in years:
        print("{}: {}".format(i, data[i]["emission"]))
        popu = data[i]["population"]
        if popu is None:
            popu = "Missing population data!"
        print("{}: {}".format(i, popu))
    print("1990-2005: {}%".format(data["emission_change"][0]))
    print("2005-2017: {}%".format(data["emission_change"][1]))
