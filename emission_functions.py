"""
Functions 
"""
import emission_data

the_data  = emission_data.country_data
the_y1990 = emission_data.emission_1990
the_y2005 = emission_data.emission_2005
the_y2017 = emission_data.emission_2017
years = [1990, 2005, 2017]

def search_country(search_word):
    """
    Something
    """
    country_list = []
    for index_1 in the_data:
        if search_word.lower() in index_1.lower():
            country_list.append(index_1)
    if len(country_list) == 0 :
        print("Country does not exist!")
        raise ValueError
    return country_list

def get_country_year_data_megaton(input_country, the_year_input):
    """
    info om utsläpp för ett land
    """
    the_info = the_data[input_country]["id"]

    if int(the_year_input) == 1:
        print("this year dose not year")
        raise ValueError
    if int(the_year_input) not in years:
        print("this year dose not year")
        raise ValueError

    if int(the_year_input) == 1990:
        return the_y1990[the_info] * 1000000
    if int(the_year_input) == 2005:
        return the_y2005[the_info] * 1000000
    if int(the_year_input) == 2017:
        return the_y2017[the_info] * 1000000
    return None

def get_country_change_for_years(input_country,input_y1=1,input_y2=1):
    """
    how much is the difference between years
    """
    if int(input_y1) == 1:
        raise ValueError
    if int(input_y2) == 1:
        raise ValueError

    year_one = get_country_year_data_megaton(input_country, input_y1)
    year_two = get_country_year_data_megaton(input_country, input_y2)
    differnt_1 = int(year_two) - int(year_one)
    diffenrnt_2 = differnt_1 / year_one * 100

    return round(diffenrnt_2, 2)


def get_country_data(country):
    """
    find the population 
    """
    info_about_country = the_data[country]["population"]
    first_one = get_country_change_for_years(country,years[0],years[1])
    second_one = get_country_change_for_years(country,years[1],years[2])
    if info_about_country == [] :
        the_answer = {'name': country,
        '1990': {'emission': get_country_year_data_megaton(country,years[0]), 'population': None},
        '2005': {'emission': get_country_year_data_megaton(country,years[1]), 'population': None},
        '2017': {'emission': get_country_year_data_megaton(country,years[2]), 'population': None},
        'emission_change': (first_one, second_one)}
    else :
        the_answer = {'name': country,
'1990': {'emission': get_country_year_data_megaton(country,years[0]), 'population': int(info_about_country[0])},
'2005': {'emission': get_country_year_data_megaton(country,years[1]), 'population': int(info_about_country[1])},
'2017': {'emission': get_country_year_data_megaton(country,years[2]), 'population': int(info_about_country[2])},
'emission_change': (first_one, second_one)}
    return the_answer
    

def print_country_data(data):
    """
    print all country data
    """
    new_list = []
    for index in years:
        info_about_country= data[str(index)]['emission']
        info_about_country_pop = data[str(index)]['population']

        if info_about_country_pop is None :
            info_about_country_pop = "Missing population data!"
        new_list.append((f"{info_about_country}, population-{index}: {info_about_country_pop}"))
           

    info_about_country_change = data['emission_change']
    info_about_country_name = data['name']

    the_result = f"""{info_about_country_name},
    1990: {new_list[0]},
    2005: {new_list[1]},
    2017: {new_list[2]},
    1990-2005: {info_about_country_change[0]}%,2005-2017: {info_about_country_change[1]}%"""

    return print(the_result)
