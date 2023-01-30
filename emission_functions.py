"""
This module will handle functions for emission
"""
from emission_data import country_data, emission_1990, emission_2005, emission_2017


def search_country(search_word: str) -> list:
    """
    Searches for countries which matches the search word
    """
    matching_countries = []
    for country in country_data:
        if str(search_word).lower() in country.lower():
            matching_countries.append(country)

    if not matching_countries:
        raise ValueError("Country does not exist!")

    return matching_countries


def get_country_year_data_megaton(country, year):
    """
    Returns the emission in megaton for a given country
    """
    if year == "1990":
        return get_emission_for_1990(country)

    if year == "2005":
        return get_emission_for_2005(country)

    if year == "2017":
        return get_emission_for_2017(country)

    raise ValueError("Wrong year!")


def get_emission_for_1990(country):
    """
    Get emission for 1990
    """
    constant = 1000000
    country_id = country_data[country]["id"]
    return emission_1990[country_id] * constant


def get_emission_for_2005(country):
    """
    Get emission for 2005
    """
    constant = 1000000
    country_id = country_data[country]["id"]
    return emission_2005[country_id] * constant


def get_emission_for_2017(country):
    """
    Get emission for 2017
    """
    constant = 1000000
    country_id = country_data[country]["id"]
    return emission_2017[country_id] * constant


def get_country_change_for_years(country, year1, year2):
    """
    Calculate the change in emission between 2 years
    """
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    change_in_percent = (emission_year2 - emission_year1) / emission_year1 * 100
    return round(change_in_percent, 2)


def get_country_data(country_name):
    """
    Retrieves data regarding a country
    """
    data = {"name": country_name}
    for year in ["1990", "2005", "2017"]:
        data[year] = {
            "emission": get_country_year_data_megaton(country_name, year),
            "population": get_population(country_name, year)
        }
    data["emission_change"] = (
        get_country_change_for_years(country_name, "1990", "2005"),
        get_country_change_for_years(country_name, "2005", "2017")
    )
    return data


def get_population(country_name, year) -> str:
    """
    Returns the population of a country
    """
    data = country_data[country_name]
    if year == "1990":
        if len(data["population"]) >= 1:
            return data["population"][0]

    if year == "2005":
        if len(data["population"]) >= 2:
            return data["population"][1]

    if year == "2017":
        if len(data["population"]) >= 3:
            return data["population"][2]

    return None


def print_country_data(data: dict):
    """
    Prints out data regarding a country
    """
    print(str(data["name"]))
    print("Emission \t\t\t - 1990: "
          + str(data["1990"]["emission"]) + "   2005: "
          + str(data["2005"]["emission"]) + "   2017: "
          + str(data["2017"]["emission"]))
    print("Emission change \t - 1990-2005: "
          + str(data["emission_change"][0]) + "%   2005-2017: "
          + str(data["emission_change"][1]) + "%")
    print("Population \t\t\t - 1990: "
          + print_population(data, "1990") + "   2005: "
          + print_population(data, "2005") + "   2017: "
          + print_population(data, "2017"))


def print_population(data, year) -> str:
    """
    This method will print out the ppulation if it exist
    """
    if data[year]["population"] is None:
        return "Missing population data!"
    return str(data[year]["population"])
