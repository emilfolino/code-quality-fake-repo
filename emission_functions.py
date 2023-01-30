#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Functions for marvin emission logic"""

import emission_data as ed


VALID_YEARS = {
    "1990": ed.emission_1990,
    "2005": ed.emission_2005,
    "2017": ed.emission_2017
}

def search_country(search_word):
    """
    returns a list with all keys (countries) from country_data dict that matches the search word. 
    """
    filtered_countries = []
    for country in ed.country_data:
        if search_word.lower() in country.lower():
            filtered_countries.append(country)
    if not filtered_countries:
        raise ValueError("Country does not exist!") 
    return filtered_countries

def get_country_year_data_megaton(country, year):
    """
    Returns the country emission for given year
    """
    TO_TON = 1000000
    COUNTRY_ID = ed.country_data[country]["id"]

    if not year in VALID_YEARS:
        raise ValueError("Wrong year!")

    emissions = VALID_YEARS.get(year, 0)
    return emissions[COUNTRY_ID] * TO_TON 

def get_country_change_for_years(country, year1, year2):
    """
    Returns the % change in emission from year1 -> year2
    """
    emission_start = get_country_year_data_megaton(country, year1)
    emission_end = get_country_year_data_megaton(country, year2)
    change =  emission_end - emission_start
    return round((change / emission_start) * 100, 2)

def get_country_data(country_name):
    """
    Collects all data for the country and adds to dict.
    """
    country_info = {
        "name": country_name
    }

    for index, year in enumerate(VALID_YEARS):
        try:
            CURRENT_POPULATION = ed.country_data[country_name]["population"][index]
        except IndexError:
            CURRENT_POPULATION = None
        country_info[year] = {"emission": get_country_year_data_megaton(country_name, year)} 
        country_info[year]["population"] = CURRENT_POPULATION

    country_info["emission_change"] = (get_country_change_for_years(country_name, "1990", "2005"),
        get_country_change_for_years(country_name, "2005", "2017"))

    return country_info

def print_country_data(data):
    """
    Prints the country data
    """
    COUNTRY_NAME = data["name"]
    YEAR_SPAN_1990_2005 = 0
    YEAR_SPAN_2005_2017 = 1
    emission_by_year = "Emission - "
    population_by_year = "Population - "

    emission_change = "Emission change - 1990-2005: "\
        f"{data['emission_change'][YEAR_SPAN_1990_2005]}%\t" \
        f"2005-2017: {data['emission_change'][YEAR_SPAN_2005_2017]}% "

    for year in VALID_YEARS:
        emission = data[year]['emission']
        population = data[year]["population"]

        emission_by_year += f"{year}: {emission} \t"
        if population:
            population_by_year += f"{year}: {population} \t"
        else: 
            population_by_year = "Missing population data!"
    
    print(COUNTRY_NAME)
    print(emission_by_year)
    print(emission_change)
    print(population_by_year)

def get_country_and_emission(year):
    """
    Returns a list with all countries and their emission for given year
    """
    listed_country_emission = []
    for country in ed.country_data:
        emission = get_country_year_data_megaton(country, year)
        listed_country_emission.append((country, emission))
    return listed_country_emission

def get_sorted_emission(year, limitation = None):
    """
    Returns a sorted and limited list of all countries and their emission for given year
    """
    sorted_country_emission = sorted(get_country_and_emission(year), 
    key=lambda country_and_emission: country_and_emission[1], reverse=True)
        
    if limitation:
        sorted_country_emission = sorted_country_emission[0:limitation]
    return sorted_country_emission

def print_countires_emission(data):
    """
    Prints country and emission from list of data.
    """
    for country, emission in data:
        print(f"{country}: {emission}")



if __name__ == "__main__":
    pass
