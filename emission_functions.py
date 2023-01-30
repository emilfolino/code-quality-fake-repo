#!/usr/bin/env python3

"""
Different functions that handles the emission data
"""

from emission_data import (country_data, emission_1990,
                           emission_2005, emission_2017)

def search_country(search_word):
    """Search for a country in the country data"""
    countries = []
    for country in country_data:
        if search_word.lower() in country.lower():
            countries.append(country)
    if not countries:
        raise ValueError
    return countries

def get_country_year_data_megaton(country, year):
    """Find out a country's emissions for a specific year"""
    country_id = country_data[country]["id"]
    if year == "1990":
        emissions = emission_1990[country_id]
    elif year == "2005":
        emissions = emission_2005[country_id]
    elif year == "2017":
        emissions = emission_2017[country_id]
    else:
        raise ValueError("Wrong year!")
    return emissions * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Calculate the difference in emissions between two years for a
    country
    """
    if country in country_data:
        emissions_year1 = get_country_year_data_megaton(country,
        year1)
        emissions_year2 = get_country_year_data_megaton(country,
        year2)
    else:
        raise ValueError("Country does not exist!")
    emission_change_quota = emissions_year2 / emissions_year1 * 100
    emission_change = round(emission_change_quota - 100, 2)
    return emission_change

def get_country_population(country, year):
    """Get a country's population a given year"""
    if country_data[country]["population"] == []:
        return None
    if year == "1990":
        year_index = 0
    elif year == "2005":
        year_index = 1
    elif year == "2017":
        year_index = 2
    population = country_data[country]["population"][year_index]
    return population

def get_country_data(country_name):
    """Gather all data for a country and put it in a dictionary"""
    data = {"name": country_name, "1990": {}, "2005": {}, "2017": {}
    }
    for year in ["1990", "2005", "2017"]:
        data[year]["emission"] = get_country_year_data_megaton(
            country_name, year)
        data[year]["population"] = get_country_population(country_name,
            year)
    data["emission_change"] = (get_country_change_for_years(
        country_name, "1990", "2005"), get_country_change_for_years(
            country_name, "2005", "2017"))
    return data

def print_country_data(data):
    """Print all data for a country"""
    print(data["name"])
    for year in ["1990", "2005", "2017"]:
        population = data[year]['population']
        if population is None:
            population = "Missing population data!"
        print(f"{year}: {data[year]['emission']}")
        print(f"{year}: {population}")
    print(f"1990-2005: {data['emission_change'][0]}%")
    print(f"2005-2017: {data['emission_change'][1]}%")
