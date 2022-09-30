"""Dotline"""

import emission_data

#12
def search_country(search_word):
    """Dotline"""
    search_result = []
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            search_result.append(key)

    if (len(search_result) != 0):
        return search_result
    
    raise ValueError()
#13

def get_country_year_data_megaton(country, year):
    """Docstring"""
    year = int(year)

    country_id = emission_data.country_data[country]["id"]
    if year == 1990:
        if (emission_data.emission_1990[country_id] is not None):
            return  emission_data.emission_1990[country_id] * (10**6)
        return None
    if year == 2005:
        if (emission_data.emission_2005[country_id] is not None):
            return  emission_data.emission_2005[country_id] * (10**6)
        return None
    if year == 2017:
        if (emission_data.emission_2017[country_id] is not None):
            return  emission_data.emission_2017[country_id] * (10**6)
        return None

    raise ValueError()
    


def get_country_change_for_years(country, year1, year2):
    """  Docstring"""""
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    result = (round((emission_year2 / emission_year1 - 1) * 100, 2))
    return result
    

#14

def get_country_data(country_name):
    """Dotstring"""
    try:
        population1990 = emission_data.country_data[country_name]['population'][0]
    except IndexError:
        population1990 = None
    
    try:
        population2005 = emission_data.country_data[country_name]['population'][1]
    except IndexError:
        population2005 = None

    try:
        population2017 = emission_data.country_data[country_name]['population'][2]
    except IndexError:
        population2017 = None



    data_summary = {
        
        "name" : country_name,    
        '1990' : {
            'emission'  : get_country_year_data_megaton(country_name, "1990"),
            'population': population1990},

        '2005' : {
            'emission'  : get_country_year_data_megaton(country_name, "2005"),
            'population': population2005},
        '2017' : {
            'emission'  : get_country_year_data_megaton(country_name, "2017"),
            'population': population2017},

        'emission_change' : (get_country_change_for_years(country_name, '1990', '2005'), 
                             get_country_change_for_years(country_name, '2005', '2017'))
    }

    return data_summary



def print_country_data(data):
    """Docstring"""
    if (data['1990']['population'] is None):
        data['1990']['population'] = "Missing population data!"

    if (data['2005']['population'] is None):
        data['2005']['population'] = "Missing population data!"

    if (data['2017']['population'] is None):
        data['2017']['population'] = "Missing population data!"


    print (data['name'])
    print ('1990: ' + str(data['1990']['emission']) + ' 2005: '   + 
        str(data['2005']['emission']) + ' 2017: ' + str(data['2017']['emission']))
    print ('1990: ' + str(data['1990']['population']) + ' 2005: ' + 
        str(data['2005']['population']) + ' 2017: ' + str(data['2017']['population']))
    print ('1990-2005: ' + str(data['emission_change'][0]) + '% ' 
        + '2005-2017: ' + str(data['emission_change'][1]) + '%')
        