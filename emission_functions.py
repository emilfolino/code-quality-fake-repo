#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for emission data
"""
from emission_data import country_data
from emission_data import emission_1990
from emission_data import emission_2005
from emission_data import emission_2017
emission_years = { "1990" : emission_1990, "2005" : emission_2005, "2017" : emission_2017}

def search_country(search_word):
    """Returns list of countries matching"""
    matching_list = []
    for _, val in enumerate(country_data):
        if val.lower().__contains__(search_word.lower()):
            matching_list.append(val)
    if len(matching_list) <= 0:
        raise ValueError("Country does not exist!")
    return matching_list
def get_country_year_data_megaton(country, year):
    """Returns megaton for provided country"""
    result = 0
    if country in country_data:
        countryid = country_data[country]["id"]
        #if "emission_" + str(year) in locals():
        #    result = locals()["emission_" + str(year)][countryid] * 1000000
        if year in emission_years:
            result = emission_years[year][countryid] * 1000000
        else:
            raise ValueError(f"Wrong year!({year})")
    else:
        raise ValueError("Country does not exist!")
    return result
def get_country_change_for_years(country, year1, year2):
    """Gets emission change"""
    megaton1 = get_country_year_data_megaton(country, year1)
    megaton2 = get_country_year_data_megaton(country, year2)
    return round(((megaton2 / megaton1) * 100) - 100, 2)

def handle_search():
    """Handles terminal input for search country"""
    search_word = input("Enter word to search countries for: ")
    try:
        matching_list = search_country(search_word)
        print("Following countries were found: " + ", ".join(matching_list))
    except ValueError as e:
        print(e)

def handle_country_change():
    """Handles input for get country etc namn lång"""
    args = input("Enter [country],[year1],[year2]").split(",")
    if len(args) == 3:
        try:
            percentage = get_country_change_for_years(args[0], args[1], args[2])
            print(f"{args[0]}:{percentage}%")
        except ValueError as e:
            print(e)
    else:
        print("Invalid arguments")    

def get_country_data(country):
    """Returns country data"""
    c_data = {}
    if country in country_data:
        c_data["name"] = country
        emission_tuple = ()
        keylist = list(emission_years.keys())
        for i, year in enumerate(keylist):
            c_data[year] = {}
            if len(country_data[country]["population"]) > i:
                c_data[year]["population"] = country_data[country]["population"][i]
            else:
                c_data[year]["population"] = None
            if i + 1 < len(emission_years):
                emission_tuple += (get_country_change_for_years(country, year, keylist[i + 1]), )
            c_data[year]["emission"] = get_country_year_data_megaton(country, year)
        c_data["emission_change"] = emission_tuple
    else:
        raise ValueError("Country does not exist!")
    return c_data

def print_country_data(data):
    """Prints data from get country data"""
    yearkey_list = list(emission_years.keys())
    for _, key in enumerate(data):
        if key == "name":
            print(data[key])
        if key in emission_years:
            keylist = list(data[key].keys())
            for yearkey in keylist:
                if not data[key][yearkey] is None:
                    print(f"{yearkey}: {key}: {data[key][yearkey]}", end = " ")
                else:
                    print(f"Missing {yearkey} data!", end = " ")
        if key == "emission_change":
            print("emission change: ", end = "")
            for i, yearchange in enumerate(data[key]):#Loop emission changes, map to year + next year
                if i + 1 < len(yearkey_list):
                    print(f"{yearkey_list[i]}-{yearkey_list[i + 1]}: {yearchange}%", end = " ")
        print("")


def handle_country_data():
    """Handles input for country data functions"""
    try:
        country_name = input("Enter country name to fetch data: ")
        print_country_data(get_country_data(country_name))
    except ValueError as e:
        print(e)
