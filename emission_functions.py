#!/usr/bin/env python3

"""
Emission functions
"""
import emission_data

country_data = emission_data.country_data.copy()
emission_1990 = emission_data.emission_1990.copy()
emission_2005 = emission_data.emission_2005.copy()
emission_2017 = emission_data.emission_2017.copy()


def search_country(search_word):
    """searches emission data for country"""

    found_countries = []
    search_word = search_word.lower()
    
    for keys in country_data: #loops through keys as string
        temp_key_str = str(keys).lower()
        if search_word in temp_key_str:
            found_countries.append(keys)
        
    if len(found_countries) == 0:
        raise ValueError("Country does not exist!")
    
    return found_countries

def get_country_year_data_megaton(country, year1):
    """gets country emission data for year and return megaton"""
    country_id = get_country_id(country)
    emission = 0
    print(year1)
    year1 = int(year1)
    if year1 == 1990:
        emission = emission_1990[country_id]
    elif year1 == 2005:
        emission = emission_2005[country_id]
    elif year1 == 2017:
        emission = emission_2017[country_id]
    else:
        raise ValueError("Wrong year!")
    print(emission * 1000000)
    return emission * 1000000

def get_country_year_data(country, year1):
    """gets emission data returns not megaton"""
    country_id = get_country_id(country)
    emission = 0
    year1 = int(year1)

    if year1 == 1990:
        emission = emission_1990[country_id]
    elif year1 == 2005:
        emission = emission_2005[country_id]
    elif year1 == 2017:
        emission = emission_2017[country_id]
    else:
        raise ValueError("Wrong year!")
    print(emission * 1000000)
    return emission * 1000000

def get_country_change_for_years(country, year1, year2):
    """calculates emission change between two years, return %chg"""
    available_years = [1990, 2005, 2017]
    year1 = int(year1)
    year2 = int(year2)
    if year1 not in available_years or year2 not in available_years:
        raise ValueError("Wrong year!")
    emission_year_1 = get_country_year_data_megaton(country, year1)
    emission_year_2 = get_country_year_data_megaton(country, year2)
#    return_change = round((float(emission_year_2)/float(emission_year_1))*100-100, 2)
    return_change = round(((emission_year_2-emission_year_1) / emission_year_1)*100, 2)
    return return_change

def get_country_id(country): 
    """finds id for specified country"""
    try:
        search_country(country) #checks if country ok
        id_from = int(country_data[country]["id"])
    except KeyError as e:
        print(str(e))

    return id_from
def get_country_data(country_name): 
    """gets country data, returns dict"""
    country_name = str(country_name)
    emission_90 = get_country_year_data_megaton(country_name, 1990)
    emission_05 = get_country_year_data_megaton(country_name, 2005)
    emission_17 = get_country_year_data_megaton(country_name, 2017)
    pop90 = get_country_population(country_name, 1990)
    pop05 = get_country_population(country_name, 2005)
    pop17 = get_country_population(country_name, 2017)
    ec9005 = get_country_change_for_years(country_name, 1990, 2005)
    ec0517 = get_country_change_for_years(country_name, 2005, 2017)
    
    return_dict = {"name": country_name, 
    "1990" : {"emission": emission_90 , "population" : pop90},
    "2005" : {"emission": emission_05 , "population" : pop05},
    "2017" : {"emission": emission_17 , "population" : pop17},
    "emission_change" : (ec9005, ec0517)
    }
    return return_dict

def print_country_data(data): 
    """gets dict and prints it"""
    if data["1990"]["population"] is None:
        print("""{country_name} \n Emission: 1990: {emission_1990} 2005: {emission_2005} 2017: {emission_2017} \n 
        Emission change: 1990-2005: {emission_c_1}% 2005-2017: {emission_c_2}% \n 
        Population: Missing population data!""".format(
            country_name = data["name"],
            emission_1990 = data["1990"]["emission"],
            emission_2005 = data["2005"]["emission"],
            emission_2017 = data["2017"]["emission"],
            emission_c_1 = data["emission_change"][0],
            emission_c_2 = data["emission_change"][1]
        ))
    else:
        print("""{country_name} \n Emission: 1990: {emission_1990} 2005: {emission_2005} 2017: {emission_2017} \n 
        Emission change: 1990-2005: {emission_c_1}% 2005-2017: {emission_c_2}% \n 
        Population: 1990: {population_1990} 2005: {population_2005} 2017: {population_2017}""".format(
            country_name = data["name"],
            emission_1990 = data["1990"]["emission"],
            emission_2005 = data["2005"]["emission"],
            emission_2017 = data["2017"]["emission"],
            emission_c_1 = data["emission_change"][0],
            emission_c_2 = data["emission_change"][1],
            population_1990 = data["1990"]["population"],
            population_2005 = data["2005"]["population"],
            population_2017 = data["2017"]["population"],
        ))
    

def get_country_population(country, year):
    """finds country population"""
    population = None

    if len(country_data[country]["population"]) == 0:
        population = None
    elif year == 1990:
        population = country_data[country]["population"][0]
    elif year == 2005:
        population = country_data[country]["population"][1]
    elif year == 2017:
        population = country_data[country]["population"][2]

    return population
