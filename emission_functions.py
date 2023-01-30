"""Module with functions for emissions"""

import emission_data

def search_country(search_word):
    """Returns a list of countries matching the search word"""
    country_list = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            country_list.append(country)
    if country_list:
        return country_list
    raise ValueError
    
def get_country_year_data_megaton(country, year):
    """Returns the emission of a country in a specific year"""
    year = str(year)
    country_id = emission_data.country_data.get(country).get("id")
    if year == "1990": 
        country_emission = emission_data.emission_1990.get(country_id)
    elif year == "2005":
        country_emission = emission_data.emission_2005.get(country_id)
    elif year == "2017":
        country_emission = emission_data.emission_2017.get(country_id)
    else:
        raise ValueError
    country_emission = country_emission * 1000000
    return country_emission

def get_country_change_for_years(country, year1, year2):
    """Returns the differance in emission between two years"""
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)

    increase = emission_year2 - emission_year1
    percentage = round((increase / emission_year1) * 100, 2)
    
    return percentage

def get_country_data(country_name):
    """Builds a dictionary containing data for a country"""
    try:
        dict_country_data = {
            "name" : country_name,

            "1990" : {"emission" : get_country_year_data_megaton(country_name, 1990), 
                    "population" : emission_data.country_data.get(country_name).get("population")[0]},

            "2005" : {"emission" : get_country_year_data_megaton(country_name, 2005), 
                    "population" : emission_data.country_data.get(country_name).get("population")[1]},

            "2017" : {"emission" : get_country_year_data_megaton(country_name, 2017), 
                    "population" : emission_data.country_data.get(country_name).get("population")[2]},

            "emission_change" : (get_country_change_for_years(country_name, 1990, 2005),
                                get_country_change_for_years(country_name, 2005, 2017))
        }
    except IndexError:
        dict_country_data = {
            "name" : country_name,

            "1990" : {"emission" : get_country_year_data_megaton(country_name, 1990), 
                    "population" : None},

            "2005" : {"emission" : get_country_year_data_megaton(country_name, 2005), 
                    "population" : None},

            "2017" : {"emission" : get_country_year_data_megaton(country_name, 2017), 
                    "population" : None},

            "emission_change" : (get_country_change_for_years(country_name, 1990, 2005),
                                get_country_change_for_years(country_name, 2005, 2017))
        }

    return dict_country_data

def print_country_data(data):
    """Prints country data"""
    name = data.get("name")
    population = emission_data.country_data.get(name).get("population")
    
    if population != []:
        print( f"{name}\n Emission - 1990: {data.get('1990').get('emission')}\
                2005: {data.get('2005').get('emission')}\
                2017: {data.get('2017').get('emission')}\n\
                Emission change - 1990-2005: {data.get('emission_change')[0]}%\
                2005-2017: {data.get('emission_change')[1]}%\n\
                Population - 1990: {data.get('1990').get('population')}\
                2005: {data.get('2005').get('population')}   2017: {data.get('2017').get('population')}")
    else:
        print( f"{name}\n Emission - 1990: {data.get('1990').get('emission')}\
            2005: {data.get('2005').get('emission')}   2017: {data.get('2017').get('emission')}\n\
            Emission change - 1990-2005: {data.get('emission_change')[0]}%  2005-2017: {data.get('emission_change')[1]}%\n\
            Population - Missing population data!")
