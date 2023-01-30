"""
Functions for emission data
"""

import emission_data

def search_country(sw):
    """
    Gives countries that includes the substring
    """
    results = []
    for key in emission_data.country_data:
        if sw.lower() in key.lower():
            results.append(key)
    if results:
        return results
    raise ValueError

def get_country_year_data_megaton(c, y):
    """
    Gives the amount emissions from a country by the given year
    """
    country_id = emission_data.country_data[c]["id"]
    if y == "1990":
        return emission_data.emission_1990[country_id] * 1000000
    if y == "2005":
        return emission_data.emission_2005[country_id] * 1000000
    if y == "2017":
        return emission_data.emission_2017[country_id] * 1000000
    raise ValueError

def get_country_change_for_years(c, y1, y2):
    """
    Gives the change of emission
    """
    y1_emission = get_country_year_data_megaton(c, y1)
    y2_emission = get_country_year_data_megaton(c, y2)
    diffrance = y2_emission / y1_emission
    return round((diffrance-1) * 100, 2)

def get_country_data(c):
    """
    gets data for a country
    """
    try:
        populations = [
            emission_data.country_data[c]["population"][0],
            emission_data.country_data[c]["population"][1],
            emission_data.country_data[c]["population"][2]
        ]
    except IndexError:
        populations = [None, None, None]
    country_data = {
        "name" : c,
        "1990" : {"emission" : get_country_year_data_megaton(c, "1990"), "population" : populations[0]},
        "2005" : {"emission" : get_country_year_data_megaton(c, "2005"), "population" : populations[1]},
        "2017" : {"emission" : get_country_year_data_megaton(c, "2017"), "population" : populations[2]},
        "emission_change" : (get_country_change_for_years
                             (c, "1990", "2005"), get_country_change_for_years(c, "2005", "2017"))
    }
    return country_data

def print_country_data(d):
    """
    Print out the data
    """
    print(
        "{name}\n".format
        (
            name = d["name"]
        )+
        "Emission\t\t - 1990: {emission_1990}\t 2005: {emission_2005}\t 2017: {emission_2017}\n".format
        (
            emission_1990 = str(d["1990"]["emission"]),
            emission_2005 = str(d["2005"]["emission"]),
            emission_2017 = str(d["2017"]["emission"])
        )+
        "Emission change\t\t - 1990-2005: {emission_1990_2005}%\t 2005-2017: {emission_2005_2017}%".format
        (
            emission_1990_2005 = str(d["emission_change"][0]),
            emission_2005_2017 = str(d["emission_change"][1])
        )
    )
    if d["1990"]["population"] is None:
        print("population\t\t - Missing population data!")
    else:
        print("Population\t\t - 1990: {population_1990}\t 2005: {population_2005}\t 2017: {population_2017}".format
            (
                population_1990 = str(d["1990"]["population"]),
                population_2005 = str(d["2005"]["population"]),
                population_2017 = str(d["2017"]["population"])
            )
        )
