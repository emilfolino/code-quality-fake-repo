"""
All functions used to show emissionsdata on different countries
"""

import emission_data

def search_country(search_word):
    """
    Search for all nations containing the searchword in a dictionary 
    dict is (country_data in the file emission_data.py)
    """
    answer_list = []    
    for country in emission_data.country_data:
        if (search_word.casefold() in country.casefold()) or (search_word.casefold == country.casefold()):
            answer_list.append(country)
    if len(answer_list) == 0:
        raise ValueError
    return answer_list

def get_country_year_data_megaton(country, year):
    """
    gets a countries emission in megatons in specific year (1990, 2005 or 2017)
    Raises ValueError if the chosen year is not 1990, 2005 or 2017
    """
    for country_loop, data in emission_data.country_data.items():
        if country.casefold() == country_loop.casefold():
            country_id = data["id"]
            if int(year) == 1990:
                output = emission_data.emission_1990[country_id] * 1000000
            elif int(year) == 2005:
                output = emission_data.emission_2005[country_id] * 1000000
            elif int(year) == 2017:
                output =emission_data.emission_2017[country_id] * 1000000
            else:
                raise ValueError("Wrong year!")
            return output    
    raise ValueError("That's not a country/english!")

def get_country_change_for_years(country, year1, year2):
    """
    gets a countries emissiondifference between two years
    """
    year_1 = get_country_year_data_megaton(country, year1)
    year_2 = get_country_year_data_megaton(country, year2)
    difference = ((year_2 / year_1) - 1) * 100 
    return round(difference, 2)

def get_country_data(country_name):
    """
    Gets a countries emission in 1990, 2005 and 2017, difference between emission in 1990-2005 and 2005-2017
    Then puts this in its own directory (country_dict)
    """
    country_dict = emission_data.country_data
    population = []
    for country, key in country_dict.items():
        if (country == country_name) or country == country_name.casefold():
            population += key["population"]
    if len(population) != 3:
        i = 0
        while i < 4:
            population.append(None)
            i+= 1

    country_dict = {
        "name" : country_name,
        "1990" : {"emission" : get_country_year_data_megaton(country_name, 1990), "population" : population[0]},
        "2005" : {"emission" : get_country_year_data_megaton(country_name, 2005), "population" : population[1]},
        "2017" : {"emission" : get_country_year_data_megaton(country_name, 2017), "population" : population[2]},
        "emission_change" : (get_country_change_for_years(country_name, 1990, 2005), 
            get_country_change_for_years(country_name, 2005, 2017))
    }

    return country_dict

def print_country_data(data):
    """
    print dictionary from the function get_country_data and prints it out in a specific format
    """
    country = data["name"]
    emission = f"Emission \t- 1990: {data['1990']['emission']}\
    2005: {data['2005']['emission']}\t2017: {data['2017']['emission']}"
    emission_change = f"Emission change - 1990-2005: {data['emission_change'][0]}%\
     2005-2017: {data['emission_change'][1]}%"
    population = f"Population\t- 1990: {data['1990']['population']}\
    2005: {data['2005']['population']}\t2017: {data['2017']['population']}"
    if data["1990"]["population"] is not None:
        if data["2005"]["population"] is not None:
            if data["2017"]["population"] is not None:
                print(f"{country} \n{emission} \n{emission_change} \n{population}")
    else:
        print(f"{country} \n{emission} \n{emission_change} \nMissing population data!")

def get_emission_sorted_list(year):
    """
    gets the name of all countries and their emission in a specific year
    returns in dict
    """
    if year == 1990:
        country_dict = emission_data.emission_1990
    elif year == 2005:
        country_dict = emission_data.emission_2005
    elif year == 2017:
        country_dict = emission_data.emission_2017
    else:
        raise ValueError("That's not a valid year!")

    country_data = emission_data.country_data.items()
    tmp_dict = {}

    for country_id , emission in country_dict.items():
        for country, data in country_data:
            if data["id"] == country_id:
                tmp_dict[country] = emission 
    tmp_list = sorted(tmp_dict.items(), key = lambda x: x[1], reverse = True)
    return tmp_list

def get_multiple_countries(year, countries_nmbr = 0):
    """
    Prints all/a number of countries emissions sorted from largest to smallest amount
    """
    tmp_list = get_emission_sorted_list(year)

    if countries_nmbr:
        index = 0
        while index < (countries_nmbr):
            print(f"{tmp_list[index][0]}: {tmp_list[index][1] * 1000000}")
            index += 1
    else:
        for country, emission in tmp_list:
            print(f"{country}: {emission * 1000000}")
    
def get_emission_per_capita(year, countries_nmbr =0):
    """
    Prints all/a number of countries emissions sorted from largest to smallest amount
    per capita
    """
    tmp_list = get_emission_sorted_list(year)
    tmp_dict = {}

    for country, emission in tmp_list:
        data = get_country_data(country)
        try:
            capita = round((emission * 1000000 / data[str(year)]["population"]), 2)
            tmp_dict[country] = capita
        except TypeError:
            tmp_dict[country] = -1
    tmp_list = sorted(tmp_dict.items(), key = lambda x: x[1], reverse = True)
    
    if countries_nmbr:
        index = 0
        while index < (countries_nmbr):
            if tmp_list[index][1] == -1:
                print(f"{tmp_list[index][0]}: Missing population data!")
            else:
                print(f"{tmp_list[index][0]}: {tmp_list[index][1]}")
            index += 1
    else:
        for country, emission in tmp_list:
            if emission == -1:
                print(f"{country}: Missing population data!")
            else:
                print(f"{country}: {emission}")

def get_emission_per_area(year, countries_nmbr = 0):
    """
    Prints all/a number of countries emissions sorted from largest to smallest amount
    per area
    """
    tmp_list = get_emission_sorted_list(year)
    pop_list = emission_data.country_data
    tmp_dict = {}

    for country, emission in tmp_list:
        try:
            capita = round((emission * 1000000 / pop_list[country]["area"]), 2)
            tmp_dict[country] = capita
        except ZeroDivisionError:
            tmp_dict[country] = -1
        
    tmp_list = sorted(tmp_dict.items(), key = lambda x: x[1], reverse = True)

    if countries_nmbr:
        index = 0
        while index < (countries_nmbr):
            if tmp_list[index][1] == -1:
                print(f"{tmp_list[index][0]}: Missing area data!")
            else:
                print(f"{tmp_list[index][0]}: {tmp_list[index][1]}")
            index += 1
    else:
        for country, emission in tmp_list:
            if emission == -1:
                print(f"{tmp_list[index][0]}: Missing area data!")
            else:
                print(f"{country}: {emission}")
