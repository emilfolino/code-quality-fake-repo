"""EMISSION FUNCTIONS FOR TORKEL"""

import emission_data

def search_country(search_word):
    """SEARCHES FOR AN COUNTRY IN EMISSION DATA"""
    country_list = []
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            country_list.append(key)
    if len(country_list) > 0:
        return country_list
    raise ValueError

def get_country_change_for_years(country, year1, year2):
    """CALCULATES THE DIFFERENCE IN PERCENTAGE BEETWEEN TWO YEARS OF EMISSION"""
    result_percentages = "Wrong year!"
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    if emission_year1 and emission_year2 != "Wrong year!":
        result_percentages = round(((float(emission_year2) - float(emission_year1)) / float(emission_year1))*100, 2)
    return result_percentages

def get_country_year_data_megaton(country, year):
    """FINDS AN SPECIFIC EMISSION DATA OF A COUNTRY"""
    country_id = emission_data.country_data[country]["id"]
    emission = ""
    if year == "1990":
        emission = emission_data.emission_1990[country_id]*1000000
    elif year == "2005":
        emission = emission_data.emission_2005[country_id]*1000000
    elif year == "2017":
        emission = emission_data.emission_2017[country_id]*1000000
    else:
        raise ValueError
    return emission

def get_country_data(country):
    """GETS ALL THE DATA FROM A SPECIFIC COUNTRY"""

    country_dict = {}
    population = emission_data.country_data[country]["population"]

    country_dict = {
        'name': country,
        '1990': {
            'emission': get_country_year_data_megaton(country, "1990"), 
            'population': population[0] if len(population) > 0 else None
        },
        '2005': {
            'emission': get_country_year_data_megaton(country, "2005"),
            'population': population[1] if len(population) > 0 else None
        },
        '2017': {
            'emission': get_country_year_data_megaton(country, "2017"),
            'population': population[2] if len(population) > 0 else None
        },
        'emission_change': (
            get_country_change_for_years(country, "1990", "2005"),
            get_country_change_for_years(country, "2005", "2017")
        )
    }

    print_country_data(country_dict)
    return country_dict

def print_country_data(data):
    """PRINTS OUT ALL THE DATA FROM A SPECIFIC COUNTRY"""
    _1990 = data["1990"]
    _2005 = data["2005"]
    _2017 = data["2017"]
    
    population_1990 = _1990["population"] if _1990["population"] is not None else "Missing population data!"
    population_2005 = _2005["population"] if _2005["population"] is not None else "Missing population data!"
    population_2017 = _2017["population"] if _2017["population"] is not None else "Missing population data!"

    print(
        data["name"] + "\n" +

        "Emission: 1990: " + str(_1990["emission"]) +
        ", 2005: " + str(_2005["emission"]) +
        ", 2017: " + str(_2017["emission"]) + "\n" + 

        "Emission change: 1990-2005: " + str(data["emission_change"][0]) + 
        "%, 2005-2017: " + str(data["emission_change"][1]) + "%\n" + 

        "Population: 1990: " + str(population_1990) +
        ", 2005: " + str(population_2005) +
        ", 2017: " + str(population_2017) 
    )
