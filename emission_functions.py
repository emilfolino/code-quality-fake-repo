"""
module for emission data functions
"""

import emission_data


def search_country(search_word):
    """
    Lets user search for one or more countries
    :param search_word:
    :return:
    """
    plchldr = 0
    country_search_list = []
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            country_search_list.append(key)
            plchldr += 1
    if plchldr == 0:
        raise ValueError
    return country_search_list


def country_name_to_id(country):
    """
    Converts the country name to the id of that country
    """
    country_as_list = search_country(country)
    country_as_string = country_as_list.pop(0)
    try:
        data_of_country = emission_data.country_data[country_as_string]
    except KeyError:
        return None
    else:
        id_of_country = data_of_country["id"]
        return id_of_country


def get_country_year_data_megaton(country, year):
    """
    Gets the emission of a country for a specific year
    """
    id_of_country = country_name_to_id(country)
    if year == "1990":
        emission_for_year = emission_data.emission_1990[id_of_country]
    elif year == "2005":
        emission_for_year = emission_data.emission_2005[id_of_country]
    elif year == "2017":
        emission_for_year = emission_data.emission_2017[id_of_country]
    else:
        raise ValueError
    return emission_for_year * 1000000


def get_country_change_for_megaton(year1, year2):
    """
    Gets change in emission for two megaton values
    :param year1:
    :param year2:
    :return:
    """
    change = int(year2) - int(year1)
    change_in_percent = (change / int(year1)) * 100
    return round(change_in_percent, 2)


def get_country_change_for_years(country, year1, year2):
    """
    Gets the change in emission in percent for two years
    :param country:
    :param year1:
    :param year2:
    :return:
    """
    year1 = get_country_year_data_megaton(country, year1)
    year2 = get_country_year_data_megaton(country, year2)
    change = int(year2) - int(year1)
    change_in_percent = (change / int(year1)) * 100
    return round(change_in_percent, 2)


def get_country_population(country, year):
    """
    Converts the country name to the population of that country
    """
    year_index = 0
    if year == "2005":
        year_index = 1
    elif year == "2017":
        year_index = 2
    country_as_list = search_country(country)
    country_as_string = country_as_list.pop()
    data_of_country = emission_data.country_data[country_as_string]
    population_of_country = data_of_country["population"][year_index]
    return population_of_country


def get_country_data(country_name):
    """
    Collects data from a country
    :param country_name:
    :return:
    """
    emission_1990 = get_country_year_data_megaton(country_name, "1990")
    emission_2005 = get_country_year_data_megaton(country_name, "2005")
    emission_2017 = get_country_year_data_megaton(country_name, "2017")
    try:
        population_1990 = get_country_population(country_name, "1990")
        population_2005 = get_country_population(country_name, "2005")
        population_2017 = get_country_population(country_name, "2017")
    except IndexError:
        population_1990 = None
        population_2005 = None
        population_2017 = None
    try:
        to_print = {"name": country_name,
                    "1990": {"emission": emission_1990, "population": population_1990},
                    "2005": {"emission": emission_2005, "population": population_2005},
                    "2017": {"emission": emission_2017, "population": population_2017},
                    "emission_change": (get_country_change_for_megaton(get_country_year_data_megaton(country_name,
                                                                                                     "1990"),
                                                                       get_country_year_data_megaton(country_name,
                                                                                                     "2005")),
                                        get_country_change_for_megaton(get_country_year_data_megaton(country_name,
                                                                                                     "2005"),
                                                                       get_country_year_data_megaton(country_name,
                                                                                                     "2017")))
                    }
    except ValueError:
        return None
    else:
        return to_print


def print_country_data(data):
    """
    prints the data of a country
    :param data:
    :return:
    """
    if data is not None:
        country_name = data["name"]
        emission_1990 = data["1990"]["emission"]
        emission_2005 = data["2005"]["emission"]
        emission_2017 = data["2017"]["emission"]
        emission_change_90_05 = data["emission_change"][0]
        emission_change_05_17 = data["emission_change"][1]
        population_is_no_data = "Missing population data!"
        if data["1990"]["population"] is not None:
            population_1990 = data["1990"]["population"]
        else:
            population_1990 = population_is_no_data
        if data["2005"]["population"] is not None:
            population_2005 = data["2005"]["population"]
        else:
            population_2005 = population_is_no_data
        if data["2017"]["population"] is not None:
            population_2017 = data["2017"]["population"]
        else:
            population_2017 = population_is_no_data
        string_to_print = \
            f"{country_name}\n" \
            f"Emission        -1990: {emission_1990}    2005: {emission_2005}    2017: {emission_2017} \n" \
            f"Emission change -1990-2005: {emission_change_90_05}%    2005-2017: {emission_change_05_17}% " \
            f"\n" \
            f"Population      -1990: {population_1990}    2005: {population_2005}    2017: {population_2017} "
        print(string_to_print)
    else:
        pass
