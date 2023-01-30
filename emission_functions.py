"""
Emission functions
"""

import emission_data
def search_country(searchWord):
    """
    Look up a country.
    """
    countries = []
    for key in emission_data.country_data:
        if searchWord.lower() in key.lower():
            countries.append(key)
    if countries == []:
        raise ValueError("Country does not exist!")
    return countries

def get_country_change_for_years(country, year1, year2):
    """
    See the changes of emission between two years for a country.
    """
    return (round(((get_country_year_data_megaton(country, year2)/
    get_country_year_data_megaton(country, year1))*100)-100, 2))


def get_country_year_data_megaton(country, year):
    """
    Get the emissions data for a country.
    """
    for key, value in emission_data.country_data.items():
        if country.lower() == key.lower():
            countryId = value["id"]
    if year == "1990":
        emission = emission_data.emission_1990[countryId]*1000000
    elif year == "2005":
        emission = emission_data.emission_2005[countryId]*1000000
    elif year == "2017":
        emission = emission_data.emission_2017[countryId]*1000000
    else:
        raise ValueError("Wrong year!")
    return emission

def print_country_data(country_info):
    """
    Print out info about a country.
    """
    if country_info["1990"]["population"] is None:
        del country_info["1990"]["population"]
        del country_info["2005"]["population"]
        del country_info["2017"]["population"]
    print(country_info["name"])
    print(("Emission: 1990: " + str(country_info["1990"]["emission"]) + " 2005: " + 
    str(country_info["2005"]["emission"]) + " 2017: " + str(country_info["2017"]["emission"])))
    print(("Population: 1990: " + str(country_info["1990"].get("population", "Missing population data!")) + 
    " 2005: " + str(country_info["2005"].get("population", "Missing population data!")) + 
    " 2017: " + str(country_info["2017"].get("population", "Missing population data!"))))
    print("1990-2005: " + str(country_info["emission_change"][0]) + "%")
    print("2005-2017: " + str(country_info["emission_change"][1]) + "%")

def get_country_data(country_name):
    """
    Get info about a country.
    """
    info = {"name" : "",
    "1990" : {},
    "2005" : {},
    "2017" : {},
    "emission_change" : ""}
    info["name"] = country_name
    info["1990"]["emission"] = get_country_year_data_megaton(country_name, "1990")
    info["2005"]["emission"] = get_country_year_data_megaton(country_name, "2005")
    info["2017"]["emission"] = get_country_year_data_megaton(country_name, "2017")
    for key, value in emission_data.country_data.items():
        if country_name.lower() == key.lower():
            if value["population"] != []:
                info["1990"]["population"] = value["population"][0]
                info["2005"]["population"] = value["population"][1]
                info["2017"]["population"] = value["population"][2]
            else:
                info["1990"]["population"] = None
                info["2005"]["population"] = None
                info["2017"]["population"] = None
    info["emission_change"] = (get_country_change_for_years(country_name, "1990", "2005"), 
    get_country_change_for_years(country_name, "2005", "2017"))
    return info
