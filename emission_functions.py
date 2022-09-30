#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""this module holds functions for getting data"""

import emission_data



def search_country(search_word):
    """Get country indexdes"""
    countries = []
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            countries.append(key)

    if bool(countries) is False:
        raise ValueError("Country does not exist!")

    print(countries)
    return countries

def get_country_year_data_megaton(country, year):
    """function getting emission for year"""
    country_id = emission_data.country_data[country]["id"]
    my_tuple = (emission_data.emission_1990, emission_data.emission_2005, emission_data.emission_2017)

    rel_years = "1990, 2005, 2017"
    if year not in rel_years:
        raise ValueError("Wrong Year!")

    if str(year) == "1990":
        emission = my_tuple[0][country_id]
    elif str(year) == "2005":
        emission = my_tuple[1][country_id]
    elif str(year) == "2017":
        emission = my_tuple[2][country_id]

    return emission * 1000000

def get_country_change_for_years(country, year1, year2):
    """function to calculate difference"""
    year1 = get_country_year_data_megaton(country,year1)
    year2 = get_country_year_data_megaton(country,year2)

    emission_dif = year2 / year1
    emission_dif = (emission_dif - 1) * 100
    return round(emission_dif,2)

def get_country_data(country_name):
    """function getting getting data from country"""
    if bool(emission_data.country_data[country_name]["population"]) is not False:
        pop1990 = emission_data.country_data[country_name]["population"][0]
    else:
        pop1990 = None

    if bool(emission_data.country_data[country_name]["population"]) is not False:
        pop2005 = emission_data.country_data[country_name]["population"][1]
    else:
        pop2005 = None

    if bool(emission_data.country_data[country_name]["population"]) is not False:
        pop2017 = emission_data.country_data[country_name]["population"][2]
    else:
        pop2017 = None

    change_one = get_country_change_for_years(country_name, "1990", "2005")
    change_two = get_country_change_for_years(country_name, "2005", "2017")
    my_tuple = (change_one, change_two)

    dictionary = {
    "name" : country_name,
    "1990" : {"emission" : get_country_year_data_megaton(country_name, "1990"),
    "population" : pop1990},
    "2005" : {"emission" : get_country_year_data_megaton(country_name, "2005"),
    "population" : pop2005},
    "2017" : {"emission" : get_country_year_data_megaton(country_name, "2017"),
    "population" : pop2017},
    "emission_change" : my_tuple
    }
    return dictionary


def print_country_data(dictionary):
    """function for printing data of country"""
    ett = dictionary["name"] + "\nEmission " + "1990: " + str(dictionary["1990"]["emission"])
    två = " 2005: " + str(dictionary["2005"]["emission"])
    tre = " 2017: " + str(dictionary["2017"]["emission"])
    diff_90_05 = str(dictionary["emission_change"][0])
    diff_05_17 = str(dictionary["emission_change"][1])
    fyra = "\nemission change " + "1990-2005: " + str(diff_90_05) + "% 2005-2017: " + str(diff_05_17) + "%"

    if dictionary["1990"]["population"] is None:
        dictionary["1990"]["population"] = "Missing population data!"
    if dictionary["2005"]["population"] is None:
        dictionary["2005"]["population"] = "Missing population data!"
    if dictionary["2017"]["population"] is None:
        dictionary["2017"]["population"] = "Missing population data!"

    fem = "\nPopulation " + "1990: " + str(dictionary["1990"]["population"])
    sex = " 2005: " + str(dictionary["2005"]["population"])
    sju = " 2017: " + str(dictionary["2017"]["population"])
    utskrift = ett + två + tre + fyra + fem + sex + sju
    print(utskrift)
    return(utskrift)
