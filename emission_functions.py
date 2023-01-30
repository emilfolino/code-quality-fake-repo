"""
Emission functions
"""

import emission_data

def search_country(search_word):
    """ Searching if argument word matches country """
    final_list = []
    final_string = ""
    for row in emission_data.country_data:
        if search_word.lower() in row.lower():
            final_list.append(row)
            final_string += row + ", "
    if final_list:
        print("Following countries were found: " + final_string[:-2])
        return final_list
    raise ValueError("Country does not exist!")

def get_country_year_data_megaton(country, year):
    """ Getting data from country/year"""
    for key, value in emission_data.country_data.items():
        if key.lower() == country.lower():
            country_info = value

    country_id = list(country_info.values())[1]

    if int(year) == 1990:
        return emission_data.emission_1990.get(country_id) * 1000000
    if int(year) == 2005:
        return emission_data.emission_2005.get(country_id) * 1000000
    if int(year) == 2017:
        return emission_data.emission_2017.get(country_id) * 1000000
    raise ValueError("Wrong year!")

def get_country_change_for_years(country, year1, year2):
    """ Comparing data from 2 country/year"""
    first_country_info = get_country_year_data_megaton(country.lower(), year1)
    second_country_info = get_country_year_data_megaton(country.lower(), year2)
    if first_country_info and second_country_info:
        country_change = (second_country_info) / float(first_country_info)

        change_math = (country_change - 1) * 100
        return(round(change_math, 2))
    raise ValueError("Wrong year!")

def get_country_data(country):
    """ Fetching country data """
    asigned_country = ""
    for row in emission_data.country_data:
        if row.lower() == country.lower():
            asigned_country = str(row)

    country_info = emission_data.country_data[asigned_country]

    if country_info:

        if list(country_info.values())[2]:
            population_1990 = list(country_info.values())[2][0]
            population_2005 = list(country_info.values())[2][1]
            population_2017 = list(country_info.values())[2][2]
        else:
            population_1990 = None
            population_2005 = None
            population_2017 = None

        emission_1990 = get_country_year_data_megaton(country, 1990)
        emission_2005 = get_country_year_data_megaton(country, 2005)
        emission_2017 = get_country_year_data_megaton(country, 2017)

        differ_first = get_country_change_for_years(country, 1990, 2005)
        differ_second = get_country_change_for_years(country, 2005, 2017)

        country_dict = {
            'name': asigned_country,
            '1990': {'emission': emission_1990, 'population': population_1990},
            '2005': {'emission': emission_2005, 'population': population_2005},
            '2017': {'emission': emission_2017, 'population': population_2017},
            'emission_change': (differ_first, differ_second)
        }

    return country_dict

def print_country_data(data):
    """ Printing country data """
    fstring = ""

    #Adding country:
    fstring += str(data.get("name")) + " \n"

    #Define populationdata - Only needs to check if one year of population is missing
    #because then, all years of population is missing.
    if data.get("1990")["population"] is None:
        population_1990 = "Missing population data!"
        population_2005 = "Missing population data!"
        population_2017 = "Missing population data!"
    else:
        population_1990 = data.get("1990")["population"]
        population_2005 = data.get("2005")["population"]
        population_2017 = data.get("2017")["population"]
        

    #Adding emission for each year
    fstring += f'Emission         - 1990: {str(data.get("1990")["emission"])}' \
    f'2005: {str(data.get("2005")["emission"])}   2017: {str(data.get("2017")["emission"])} \n'

    fstring += f'Emission change  - 1990-2005: {str(data.get("emission_change")[0])}%   ' \
    f'2005-2017: {str(data.get("emission_change")[1])}% \n'

    fstring += f'Population       - 1990: {str(population_1990)}    ' \
    f'2005: {str(population_2005)}    2017: {str(population_2017)} \n'

    print(fstring)
