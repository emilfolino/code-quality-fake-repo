"""
Module for emission functions. Imports data from emission_data and compiles it
in different ways for the user
"""
from emission_data import emission_1990, emission_2005, emission_2017, country_data

def function_calls(user_choice):
    """Logic for calling functions"""
    if user_choice == 12:
        country_pattern = input('Enter a country pattern: ')
        result = search_country(country_pattern)
    elif user_choice == 13:
        my_string = input('Enter a country and two years: ')
        choice_list = my_string.split(',')
        if len(choice_list) == 3:
            change = get_country_change_for_years(choice_list[0], choice_list[1], choice_list[2])
            result = str(choice_list[0]) + ':' + str(change) + '%'
        else:
            raise ValueError('Illegal input, try again!')
    else:
        country = input('Enter a country name: ')
        result = get_country_data(country)
        print_country_data(result)
        result =  'No more data'
    return result

def get_country_data(country_name):
    """Compiles the information for a given country in emission_data"""
    if len(country_data[country_name]['population']) < 3:
        population = (None, None, None)
    else:
        population = country_data[country_name]['population']

    my_data = {
    'name' : country_name,
    '1990' : {'emission': 0, 'population': population[0]},
    '2005' : {'emission': 0, 'population': population[1]},
    '2017' : {'emission': 0, 'population': population[2]},
    'emission_change' : ()
    }
    change = []

    for year in ('1990', '2005', '2017'):
        my_data[year]['emission'] = get_country_year_data_megaton(country_name, year)
    change.append(get_country_change_for_years(country_name, '1990', '2005'))
    change.append(get_country_change_for_years(country_name, '2005', '2017'))
    my_data['emission_change'] = tuple(change)
    return my_data

def print_country_data(data):
    """Prints the information compiled in get_country_data"""

    print(data['name'])
    my_string = 'Emissions - \t'
    for year in ('1990', '2005', '2017'):
        my_string += year + ': ' + str(data[year]['emission']) + '\t'
    print(my_string)
    my_string = 'Population - \t'
    if data[year]['population'] is None:
        my_string += "Missing population data!"
    else:
        for year in ('1990', '2005', '2017'):
            my_string += year + ': ' + str(data[year]['population']) + '\t'
    print(my_string)
    print('Emission change - \t 1990-2005:', str(data['emission_change'][0]) + '%',
    '\t', '2005-2017:', str(data['emission_change'][1]) + '%')

def get_country_year_data_megaton(country, year):
    """Picks out emission informmation for a country in a given year and returns the value in tons"""
    country_id = country_data[country]['id']
    if year == '1990':
        megaton = emission_1990[country_id]
    elif year == '2005':
        megaton = emission_2005[country_id]
    elif year == '2017':
        megaton = emission_2017[country_id]
    else:
        raise ValueError('Wrong year!')
    return megaton * 1000000

def get_country_change_for_years(country, year1, year2):
    """Calculates the change of emissions and returns a procentage"""
    #maybe you should check the order of the years, maybe not...
    value1 = get_country_year_data_megaton(country, year1)
    value2 = get_country_year_data_megaton(country, year2)
    if value1 > 0:
        num = value2/value1
        result = round((num - 1) * 100, 2)
    else:
        raise ValueError('Missing country data!')
    return result

def search_country(search_word):
    """Searches for a given string in the country_data keys and returns all matches"""
    result = []
    for key in country_data:
        if search_word.lower() in str(key).lower():
            result.append(key)
    if len(result) < 1:
        raise ValueError('Country does not exist!')
    return result
