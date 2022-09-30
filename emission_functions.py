"""
functions for Marvin4
"""
import emission_data

def search_country(search_word):
    """
    Search country function
    """
    search_word = search_word.lower()
    lst = []

    for key in emission_data.country_data:
        key = key.lower()
        if search_word in key:
            key = key.title()
            lst.append(key)

    if lst == []:
        raise ValueError
    return(lst)

def get_country_year_data_megaton(country, year):
    """
    Function to calculate emission data by year
    """
    country_id = emission_data.country_data[country]["id"]

    if year == "1990":
        return(emission_data.emission_1990[country_id] * 1000000)
    if year == "2005":
        return(emission_data.emission_2005[country_id] * 1000000)
    if year == "2017":
        return(emission_data.emission_2017[country_id] * 1000000)
    raise ValueError



def get_country_change_for_years(country, year1, year2):
    """
    Function to calculate the emission change between two years
    """
    factor1 = get_country_year_data_megaton(country, year1)
    factor2 = get_country_year_data_megaton(country, year2)

    if year1 > year2:
        diff = float(factor2 - factor1)
        change = round((diff / factor1) * 100, 2)
        return(change)
    if factor1 < factor2:
        diff = float(factor2 - factor1)
        change = round((diff / factor1) * 100, 2)
        return(change)
    if factor1 > factor2:
        diff = float(factor2 - factor1)
        change = round((diff / factor1) * 100, 2)
        return(change)
    return(0)

def get_country_data(country_name):
    """
    Get all data from a country
    """
    population = emission_data.country_data[country_name]["population"]
    if population == []:
        year_1990_population = None
        year_2005_population = None
        year_2017_population = None
        year_1990_emission =  get_country_year_data_megaton(country_name, "1990")
        year_2005_emission = get_country_year_data_megaton(country_name, "2005")
        year_2017_emission = get_country_year_data_megaton(country_name, "2017")
        year_1990_2005_change = get_country_change_for_years(country_name, "1990", "2005")
        year_2005_2017_change = get_country_change_for_years(country_name, "2005", "2017")
    else:
        year_1990_population = emission_data.country_data[country_name]["population"][0]
        year_2005_population = emission_data.country_data[country_name]["population"][1]
        year_2017_population = emission_data.country_data[country_name]["population"][2]
        year_1990_emission =  get_country_year_data_megaton(country_name, "1990")
        year_2005_emission = get_country_year_data_megaton(country_name, "2005")
        year_2017_emission = get_country_year_data_megaton(country_name, "2017")
        year_1990_2005_change = get_country_change_for_years(country_name, "1990", "2005")
        year_2005_2017_change = get_country_change_for_years(country_name, "2005", "2017")



    d = {
    "name":country_name,
    '1990': {'emission': year_1990_emission, 'population': year_1990_population},
    '2005': {'emission': year_2005_emission, 'population': year_2005_population},
    '2017': {'emission': year_2017_emission, 'population': year_2017_population},
    'emission_change': (year_1990_2005_change, year_2005_2017_change)
    }


    return(d)

def print_country_data(data):
    """
    Print all data from a country
    """
    population = data['1990']['population']
    if population is None:

        print(f"{data['name']} \nEmission\t\t- 1990: {data['1990']['emission']}\
         \t2005: {data['2005']['emission']} \t\t2017: {data['2017']['emission']}\
          \nEmission change\t\t- 1990-2005: {data['emission_change'][0]}%\
           \t2005-2017: {data['emission_change'][1]}% \nPopulation\t\t- 1990:\
            Missing population data! \t2005: Missing population data!\
             \t\t2017: Missing population data!")
    else:
        print(f"{data['name']} \nEmission\t\t- 1990: {data['1990']['emission']}\
         \t2005: {data['2005']['emission']} \t\t2017: {data['2017']['emission']}\
          \nEmission change\t\t- 1990-2005: {data['emission_change'][0]}%\
           \t2005-2017: {data['emission_change'][1]}%\
            \nPopulation\t\t- 1990: {data['1990']['population']}\
             \t2005: {data['2005']['population']} \t\t2017: {data['2017']['population']}")
