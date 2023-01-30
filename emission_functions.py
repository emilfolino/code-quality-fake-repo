"""
Emissions functions
"""

import emission_data
# pylint: disable=line-too-long

def search_country(search_word):
    """
    Search for a country.
    """
    countrynr = ""
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            countrynr += (str(country) + ", ")
        
    countrynr = countrynr[:-2]
    
    countrynr = list(countrynr.split(","))

    countrynr = [space.strip(' ') for space in countrynr]

    if '' in countrynr:
        raise ValueError
    
    return countrynr

def get_country_year_data_megaton(country, year):
    """
    Get a country's emission.
    """
    countryid = emission_data.country_data[country]["id"]
    if year == "1990":
        emission = emission_data.emission_1990[countryid]
        emission = emission * 1000000
    elif year == "2005":
        emission = emission_data.emission_2005[countryid]
        emission = emission *  1000000
    elif year == "2017":
        emission = emission_data.emission_2017[countryid]
        emission = emission *  1000000
    else:
        raise ValueError
    
    return emission


def get_country_change_for_years(country, year1, year2):
    """
    Get a country's emission difference
    in percentage between 1990, 2005 and 2017.
    """
    if country not in emission_data.country_data:
        raise ValueError
    
    emission1 = get_country_year_data_megaton(country, year1)
    emission2 = get_country_year_data_megaton(country, year2)

    percentagedif = (emission2 / emission1) * 100
    if percentagedif > 100:
        percentagedif = percentagedif - 100
        percentagedif = round(percentagedif, 2)
        #return f"An increase of {percentagedif}% between {year1} and {year2}"
    else:
        percentagedif = 1 - (percentagedif/100)
        percentagedif = percentagedif * 100
        percentagedif = round(percentagedif, 2)
        #return f"A decrease of -{percentagedif}% between {year1} and {year2}"
        percentagedif = -percentagedif
    
    return percentagedif

def get_country_data(country_name):
    """
    Get country data.
    """
    try:
        if len(emission_data.country_data[country_name].get("population")):
            countryinformation = {
                "name" : country_name,
                "1990": {"emission": get_country_year_data_megaton(country_name, "1990"), "population": emission_data.country_data[country_name]["population"][0]},
                "2005": {"emission": get_country_year_data_megaton(country_name, "2005"), "population": emission_data.country_data[country_name]["population"][1]},
                "2017": {"emission": get_country_year_data_megaton(country_name, "2017"), "population": emission_data.country_data[country_name]["population"][2]},
                "emission_change": (float(get_country_change_for_years(country_name, "1990", "2005")), float(get_country_change_for_years(country_name, "2005", "2017")))}
            
        else:
            countryinformation = {
                "name" : country_name,
                "1990": {"emission": get_country_year_data_megaton(country_name, "1990"), "population": None},
                "2005": {"emission": get_country_year_data_megaton(country_name, "2005"), "population": None},
                "2017": {"emission": get_country_year_data_megaton(country_name, "2017"), "population": None},
                "emission_change": (float(get_country_change_for_years(country_name, "1990", "2005")), float(get_country_change_for_years(country_name, "2005", "2017")))}
                
    except KeyError as keynotfound:
        raise ValueError from keynotfound
    return countryinformation

def print_country_data(data):
    """
    Print country data
    """
    if data["1990"]["population"] and data["2005"]["population"] and data["2017"]["population"] is not None:
        result = (f"{data['name']}\nEmission         - 1990: {data['1990']['emission']}    2005: {data['2005']['emission']}   2017: {data['2017']['emission']}")
        result += (f"\nPopulation       - 1990: {data['1990']['population']}    2005: {data['2005']['population']}   2017: {data['2017']['population']}")
        result += (f"\nEmission change  - 1990-2005: {data['emission_change'][0]}%    2005-2017: {data['emission_change'][1]}%")
    else:
        result = (f"{data['name']}\nEmission         - 1990: {data['1990']['emission']}    2005: {data['2005']['emission']}   2017: {data['2017']['emission']}")
        result += ("\nPopulation       - Missing population data!")
        result += (f"\nEmission change  - 1990-2005: {data['emission_change'][0]}%    2005-2017: {data['emission_change'][1]}%")
    return print(result) #Har försökt hur mycket som helst att få det att fungera när man inte returnerar print här men i main istället, är genuint osäker på varför det inte fungerar
