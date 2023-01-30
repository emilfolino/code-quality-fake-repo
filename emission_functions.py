
"""
Contains the functions used by main.py that are countrydata-related.
"""
import emission_data
def search_country(search_word):
    """
    Checks if the inputted string is a country name or a substring of a country name.
    If it is not, it raises a ValueError, that has to be caught outside of this module.
    """
    results_list = []
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            results_list.append(key)
    if results_list == []:
        raise ValueError
    return results_list

def get_country_year_data_megaton(country, year):
    """
    Returns the emission amount as a floatvalue for the entered country and year.
    If the year is not 1990, 2005 or 2017 it raises a ValueError.
    """
    emission = ""
    if year == "1990":
        emission = 1000000 * emission_data.emission_1990[emission_data.country_data[country]["id"]]
    if year == "2005":
        emission = 1000000 * emission_data.emission_2005[emission_data.country_data[country]["id"]]
    if year == "2017":
        emission = 1000000 * emission_data.emission_2017[emission_data.country_data[country]["id"]]
    if emission == "":
        raise ValueError
    return emission


def get_country_change_for_years(country, year1, year2):
    """
    Returns how many percent the year2 emission has changed from year1's emission.
    Returns a floatvalue with two decimals.
    """
    unrounded = (get_country_year_data_megaton(country, year2)/get_country_year_data_megaton(country, year1) - 1)*100
    change = round(unrounded, 2)
    return change

def get_country_data(country_name):
    """
    Creates a dictionary with five keys for argument's country:
    name, that contains the country's name, 1990, 2005 and 2017 that contains dictionaries with the emission data
    for the aforementioned years and the population for them. If no population data is available,
    the value for the population data is None.
    The last key contains a tuple with the argument's country's emissionchange, first between 1990 and 2005,
    then between 2005 and 2017. This is done by using the aforedefined function get_country_change_for_years().
    """
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
    countrydict = {
        "name" : country_name,
        "1990" : {"emission" : get_country_year_data_megaton(country_name, "1990"), "population" : population1990},
        "2005" : {"emission" : get_country_year_data_megaton(country_name, "2005"), "population" : population2005},
        "2017" : {"emission" : get_country_year_data_megaton(country_name, "2017"), "population" : population2017},
        "emission_change" : (get_country_change_for_years(country_name, "1990", "2005"), 
        get_country_change_for_years(country_name, "2005", "2017"))
    }
    return countrydict
def print_country_data(data):
    """
    Prints the data from the dictionary entered. The dictionary must have the format of the dictionary
    created in get_country_data().
    """
    print(data["name"])
    print("Emission:")
    print("1990: " + str(data["1990"]["emission"]))
    print("2005: " + str(data["2005"]["emission"]))
    print("2017: " + str(data["2017"]["emission"]))
    print("Emission change:")
    print("1990-2005: " + str(data["emission_change"][0]) + "%")
    print("2005-2017: " + str(data["emission_change"][1]) + "%")
    print("Population:")
    if data["1990"]["population"] is not None:
        print("1990: " + str(data["1990"]["population"]))
        print("2005: " + str(data["2005"]["population"]))
        print("2017: " + str(data["2017"]["population"]))
    else:
        print("Missing population data!")

if __name__ == "__main__":
    print_country_data("Sweden")
