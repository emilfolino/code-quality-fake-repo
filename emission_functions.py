
 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
modul dokument kmom05
"""
import emission_data

def search_country(search_word):
    """
    search for country
    """

    countries = list(emission_data.country_data.keys())
    new_list = []
    for country in countries:
        if search_word.lower() in country.lower():
            new_list.append(country)
    if new_list == []:
        raise ValueError
    return new_list

def get_country_year_data_megaton(country, year = None):
    """
    calculates emission for a country a specific year
    """
    c_data = emission_data.country_data
    e_1990 = emission_data.emission_1990
    e_2005 = emission_data.emission_2005
    e_2017 = emission_data.emission_2017 

    get_id = c_data[country]["id"]
    get_year = int(year)
    year_to_list = [1990, 2005, 2017]

    if get_year not in year_to_list:
        raise ValueError
    if int(get_year) == 1990:
        result = e_1990[get_id] * 1000000
    if int(get_year) == 2005:
        result =  e_2005[get_id] * 1000000
    if int(get_year) == 2017:
        result =  e_2017[get_id] * 1000000
    return result

def get_country_change_for_years(country, year1, year2):
    """
    calculates difference of emission of two diffrent years
    """
    emission1 = get_country_year_data_megaton(country, year1)
    
    emission2 = get_country_year_data_megaton(country, year2)
    
    difference = (emission2 - emission1) * 100
    result = round(difference / emission1, 2)
    return result



def get_country_data(country_name):
    """
    shows all the country data for a specific country
    """
    get_popu = emission_data.country_data[country_name]["population"]
    if get_popu != []:
        popu = get_popu[0]
        popu1 = get_popu[1]
        popu2 = get_popu[2]
    else: popu, popu1, popu2 = [None, None, None]


    data = {
    "name": country_name,
    "1990": {"emission": get_country_year_data_megaton(country_name, 1990), "population": popu},
    "2005": {"emission": get_country_year_data_megaton(country_name, 2005), "population": popu1},
    "2017": {"emission": get_country_year_data_megaton(country_name, 2017), "population": popu2},
    "emission_change": (get_country_change_for_years(country_name, 1990, 2005), 
    get_country_change_for_years(country_name, 2005,2017))
    }
    return data


def print_country_data(data):
    """
    prints data from function get_country_data
    """

    data_name = data["name"]
    emission_1990 = str(data["1990"]["emission"])
    emission_2005 = str(data["2005"]["emission"])
    emission_2017 = str(data["2017"]["emission"])
    e_change1 = str(data["emission_change"][0])
    e_change2 = str(data["emission_change"][1])
    popu_1990 = str(data["1990"]["population"])
    popu_2005 = str(data["2005"]["population"])
    popu_2017 = str(data["2017"]["population"])
    
    print(data_name)
    print("Emission - 1990: " + emission_1990 + " 2005: " + emission_2005 + " 2017: " + emission_2017)
    print("Emission change - 1990-2005: " + e_change1 + "%" + " 2005-2017: " + e_change2 + "%")
    if data["1990"]["population"] is None:
        print("Missing population data!")
    elif data["2005"]["population"] is None:
        print("Missing population data!")
    elif data["2017"]["population"] is None: 
        print("Missing population data!")
    else:
        print("Population - 1990: " + popu_1990 + " 2005: " + popu_2005 + " 2017: " + popu_2017)
        