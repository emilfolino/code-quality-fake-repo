
"""
Functions for calculation/displaying carbon emissions
"""

import emission_data

def search_country(search_word):
    """
    If input is in emission_data.country_data it adds the input to a list that it then returns
    """
    returnedValue = "\n"
    listOfCountries = []

    new_search_word = search_word.lower()
    for index in emission_data.country_data.items():
        new_index = index[0].lower()
        if new_search_word in new_index:
            if listOfCountries == []:
                listOfCountries = [index[0]]
            else:
                listOfCountries.append(index[0])

    if listOfCountries != []:
        returnedValue = listOfCountries
    else:
        raise ValueError

    return returnedValue


def nice_list_print(x):
    """
    Prints the input in a nice list
    """
    string_of_x = "\n"
    for y in x:
        string_of_x = string_of_x + y + "\n"
    return string_of_x


def get_country_change_for_years(country, year1, year2):
    """
    The main function that prints the result of two runs of the get_country_year_data_megaton function
    """
    firstAmount = 0
    secondAmount = 0

    try:
        firstAmount = get_country_year_data_megaton(country, year1)
        secondAmount = get_country_year_data_megaton(country, year2)
    except ValueError as wrong_year:
        raise ValueError from wrong_year

    try:
        number = round(((firstAmount - secondAmount) / firstAmount * 100) * -1, 2)
    except ZeroDivisionError:
        number = 0

    return number


def get_country_year_data_megaton(country, year):
    """
    Returns the megaton of carbon emission from emission_data
    """
    emission = ""

    country_id = emission_data.country_data[country]["id"]
    if str(year) == "1990":
        emission = emission_data.emission_1990[country_id]
    elif str(year) == "2005":
        emission = emission_data.emission_2005[country_id]
    elif str(year) == "2017":
        emission = emission_data.emission_2017[country_id]
    else:
        raise ValueError
    
    emission_ton = emission * 1000000

    return emission_ton

def read_emission_request(string):
    """
    Makes the initial input in the menu readable for the functions above
    """
    new = string.split(",")
    country = new[0]
    year1 = new[1]
    year2 = new[2]
    print(country, year1, year2)
    return country, year1, year2

def print_emission_request(country, result):
    """
    Used to print the result of get_country_change_for_years in the wished format
    """
    new = ""
    if result < 0:
        new = f"{country}:{result}%"
    else:
        new = f"{country}:+{result}%"
    return new

def get_country_data(country_name):
    """
    Using a country name as an input, it outputs a dictionary with information from emission_data
    """
    emission1990 = get_country_year_data_megaton(country_name, 1990)
    emission2005 = get_country_year_data_megaton(country_name, 2005)
    emission2017 = get_country_year_data_megaton(country_name, 2017)
    emission1990_2005 = get_country_change_for_years(country_name, 1990, 2005)
    emission2005_2017 = get_country_change_for_years(country_name, 2005, 2017)

    try:
        population1990 = emission_data.country_data[country_name]["population"][0]
    except IndexError:
        population1990 = None
    try:
        population2005 = emission_data.country_data[country_name]["population"][1]
    except IndexError:
        population2005 = None
    try:
        population2017 = emission_data.country_data[country_name]["population"][2]
    except IndexError:
        population2017 = None

    return {
        "name": country_name, 
        "1990": {"emission": emission1990, "population": population1990},
        "2005": {"emission": emission2005, "population": population2005},
        "2017": {"emission": emission2017, "population": population2017},
        "emission_change": (emission1990_2005, emission2005_2017)
            }

def print_country_data(data):
    """
    Prints the information that get_country_data gathers
    """
    country = str(data["name"])
    emi1990 = str(data["1990"]["emission"])
    emi2005 = str(data["2005"]["emission"])
    emi2017 = str(data["2017"]["emission"])
    emi1990_2005 = str(data["emission_change"][0])
    emi2005_2017 = str(data["emission_change"][1])
    pop1990 = ""
    pop2005 = ""
    pop2017 = ""
    
    if data["1990"]["population"] is None:
        pop1990 = "Missing population data!"
    else:
        pop1990 = pop1990 + str(data["1990"]["population"])

    if data["2005"]["population"] is None:
        pop2005 = pop2005 +"Missing population data!"
    else:
        pop2005 = str(data["2005"]["population"])

    if data["2017"]["population"] is None:
        pop2017 = "Missing population data!"
    else:
        pop2017 = pop2017 + str(data["2017"]["population"])

    string = f"{country}\n"
    string = string + f"Emission        - 1990: {emi1990} 2005: {emi2005} 2017: {emi2017}\n"
    string = string + f"Emission change - 1990-2005: {emi1990_2005}% 2005-2017: {emi2005_2017}%\n"
    string = string + f"Population      - 1990: {pop1990} 2005: {pop2005} 2017: {pop2017}\n"

    print(string) 

    return string
