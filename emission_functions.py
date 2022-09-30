'''
Funktioner för utsläpp
'''

import emission_data

def search_country(search_word):
    '''
    Söker efter ett land och om det finns i listan
    '''
    the_list = []

    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            the_list.append(key)

    if the_list == []:
        raise ValueError

    return the_list

def get_country_year_data_megaton(country, year):
    '''
    Visar utsläppen för ett land under ett visst år
    '''
    year = int(year)
    country_identification = emission_data.country_data[country]["id"]

    if year == 1990:
        string = emission_data.emission_1990[country_identification] * 1000000
    elif year == 2005:
        string = emission_data.emission_2005[country_identification] * 1000000
    elif year == 2017:
        string = emission_data.emission_2017[country_identification] * 1000000
    else:
        raise ValueError

    return string

def get_country_change_for_years(country, year1, year2):
    '''
    Räknar ut skillnaden för ett lands utsläpp mellan två år
    '''
    country_year1 = get_country_year_data_megaton(country, year1)
    country_year2 = get_country_year_data_megaton(country, year2)
    
    emission_percentage = (country_year2 - country_year1) / country_year1 * 100 
    emission_percentage_results = round(emission_percentage, 2)
   

    return emission_percentage_results

def get_country_data(country_name): 
    '''
    Kollar om landet finns, samt datan
    '''
    try:
        population1990 = emission_data.country_data[country_name]["population"][0]
    except IndexError:
        population1990 = None        
    
    try:
        population2005 = emission_data.country_data[country_name]["population"][1]
    except IndexError:
        population2005 = None
        
    try:
        population2017 = emission_data.country_data[country_name]["population"][2]
    except IndexError:
        population2017 = None

    data = {
        "name" : country_name,
        "1990" : {"emission" : + get_country_year_data_megaton(country_name, "1990"), "population" : population1990},
        "2005" : {"emission" : + get_country_year_data_megaton(country_name, "2005"), "population" : population2005},
        "2017" : {"emission" : + get_country_year_data_megaton(country_name, "2017"), "population" : population2017},
        "emission_change" : (get_country_change_for_years(country_name, "1990", "2005") 
        , get_country_change_for_years(country_name, "2005", "2017"))
        }

    return data

def print_country_data(data):
    '''
    Printar ut all data
    '''
    if  (data["1990"]["population"] is None):
        data["1990"]["population"] = "Missing population data!"
    
    if  (data["2005"]["population"] is None):
        data["2005"]["population"] = "Missing population data!"
    
    if  (data["2017"]["population"] is None):
        data["2017"]["population"] = "Missing population data!"
           
    print(data["name"])
    print("1990: " + str(data["1990"]["emission"]) + "2005: " + 
    str(data["2005"]["emission"]) + "2017: " + str(data["2017"]["emission"]))
    print("1990: " + str(data["1990"]["population"]) + "2005: " + 
    str(data["2005"]["population"]) + "2017: " + str(data["2017"]["population"]))
    print("1990-2005: " + str(data["emission_change"][0]) + "% " + 
    "2005-2017: " + str(data["emission_change"][1]) + "%")
