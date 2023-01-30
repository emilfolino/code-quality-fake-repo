"""
Functions for Phoenix's emission part.
"""


import emission_data

def search_country(search_word):
    """
    Function to search after countries in our list if there are any countries with that input string
    """

    country_list = []

    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            country_list.append(key)
    if not country_list:
        raise ValueError
    return country_list

def get_country_change_for_years(country,year_1,year_2):
    """
    Counts percentage change in CO2 emission for a country in two different years
    """
    year_1_emission = get_country_year_data_megaton(country, year_1)
    year_2_emission = get_country_year_data_megaton(country, year_2)

    change = year_2_emission - year_1_emission

    change_percentage = (change / year_1_emission)
    change_percentage_2 = change_percentage * 100
    change_rounded = round(change_percentage_2, 2)
    return change_rounded

def get_country_year_data_megaton(country, year):
    """
    Retrieves data about CO2 emission of a country in a specific year
    """
    years = ['1990', '2005', '2017']
    if year not in years:
        raise ValueError
    id_ = emission_data.country_data[country]["id"]
    return getattr(emission_data, f'emission_{year}')[id_] * 1000000



def get_country_data(country):
    """
    Gets and prints all data for a chosen country
    """

    try:

        pop_1990 = emission_data.country_data[country]["population"][0]
        pop_2005 = emission_data.country_data[country]["population"][1]
        pop_2017 = emission_data.country_data[country]["population"][2]

    except IndexError:
        pop_1990 = None
        pop_2005 = None
        pop_2017 = None


    emission_1990 = get_country_year_data_megaton(country, "1990")
    emission_2005 = get_country_year_data_megaton(country, "2005")
    emission_2017 = get_country_year_data_megaton(country, "2017")

    emission_data_1 = get_country_change_for_years(country, "1990", "2005")
    emission_data_2 = get_country_change_for_years(country, "2005", "2017")


    full_data = {
        'name' : country,
        '1990' : {'emission': emission_1990, 'population' : pop_1990},
        '2005' : {'emission': emission_2005, 'population' : pop_2005},
        '2017' : {'emission': emission_2017, 'population' : pop_2017},
        'emission_change' : (emission_data_1, emission_data_2)
    }

    return full_data


def print_country_data(data):
    """
    Beautifully prints all data we got from the function get_country_data
    """
    st = f"""
{data.get('name')}
Emission    - 1990: {data['1990']['emission']}    2005: {data['2005']['emission']}    2017: {data['2017']['emission']} 
Emission change   -   1990-2005: {data['emission_change'][0]}%    2005-2017: {data['emission_change'][1]}%
Population    - 1990: {data['1990']['population'] or "Missing population data!"}\t\
2005: {data['2005']['population'] or "Missing population data!"}    2017: {data['2017']['population'] or "Missing population data!"} 
"""
    print(st)
