"""
This module is for functions connected to marvins emission choices
"""
import emission_data
#import emission_data_small

def search_country(search_word):
    """
    This function searches for countries in the country_data dictionary
    """
    countries_containing_search_word = []
    data = emission_data.country_data
    for country in data:
        if search_word.lower() in country.lower():
            countries_containing_search_word.append(country)
    if countries_containing_search_word == []:
        raise ValueError
    return countries_containing_search_word

def get_country_year_data_megaton(country, year):
    """
    This function gets a countries data
    """
    country_id = emission_data.country_data[country]["id"]
    if year == "1990":
        emission = emission_data.emission_1990[country_id] * 1000000
    elif year == "2005":
        emission = emission_data.emission_2005[country_id] * 1000000
    elif year == "2017":
        emission = emission_data.emission_2017[country_id] * 1000000
    else:
        raise ValueError
    return emission


def get_country_change_for_years(country, year1, year2):
    """
    This function calculates the emission change between two different years
    """
    year1_data = get_country_year_data_megaton(country, year1)
    year2_data = get_country_year_data_megaton(country, year2)
    if year2_data > year1_data:
        result = round(100 * ((year2_data / year1_data) - 1), 2)
    else:
        result = round(-100 * (1 - (year2_data / year1_data)), 2)
    return result

def get_country_data(country_name):
    """
    This function gets all data from a country
    """
    if emission_data.country_data[country_name]["population"] != []:
        population_data_1990 = emission_data.country_data[country_name]["population"][0]
        population_data_2005 = emission_data.country_data[country_name]["population"][1]
        population_data_2017 = emission_data.country_data[country_name]["population"][2]
        
    else:
        population_data_1990 = None
        population_data_2005 = None
        population_data_2017 = None

    country_id = emission_data.country_data[country_name]["id"]

    emission_in_ton_1990 = emission_data.emission_1990[country_id] * 1000000
    emission_in_ton_2005 = emission_data.emission_2005[country_id] * 1000000
    emission_in_ton_2017 = emission_data.emission_2017[country_id] * 1000000

    emission_change_1990_to_2005 = get_country_change_for_years(country_name, "1990", "2005")
    emission_change_2005_to_2017 = get_country_change_for_years(country_name, "2005", "2017")

    return_data = {
        "name": f"{country_name}",
        "1990": {"emission": emission_in_ton_1990, "population": population_data_1990},
        "2005": {"emission": emission_in_ton_2005, "population": population_data_2005},
        "2017": {"emission": emission_in_ton_2017, "population": population_data_2017},
        "emission_change": (emission_change_1990_to_2005, emission_change_2005_to_2017)
    }
    return return_data

def print_country_data(data):
    """
    This function prints all data from a country
    """
    print(data["name"])
    print(f"Emission        - 1990: {data['1990']['emission']}\
            2005: {data['2005']['emission']}    2017: {data['2017']['emission']}")
    print(f"Emission change - 1990-2005: {data['emission_change'][0]}%   2005-2017: {data['emission_change'][1]}%")
    if data['1990']['population'] is not None:
        print(f"Population      - 1990: {data['1990']['population']}\
                   2005: {data['2005']['population']}       2017: {data['2017']['population']}")
    else:
        print("Population      - Missing population data!")
