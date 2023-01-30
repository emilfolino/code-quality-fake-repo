"""Funktioner som används för att kunna ta fram uppgifter kopplat till ett lands utsläpp"""

import emission_data


def search_country(search_word):
    """Funktion om används för att kunna söka efter vilka länder som finns i country_data"""
    
    list_1 = []
    data = emission_data.country_data
    for country in data:
        if search_word in country:
            list_1.append(country)
        else:
            if str(search_word).lower() in country.lower():
                list_1.append(country)
    if list_1 == []:
        raise ValueError("Wrong year!")
        
    return list_1



def get_id(country):
    """Hittar "id" för angivet land, som används för att kunna söka ut andra uppgifter"""
    id_1 = 0
    try:
        for country_list, possible_id in emission_data.country_data.items():
            if country_list == country:
                
                id_1 = possible_id
                id_1 = id_1["id"] 

    except Exception as error:
        raise ValueError from error
    if id_1 == 0:
        raise ValueError

    return id_1



def get_country_year_data_megaton(country, year):
    
    """Funktionen ger hur mycket utsläpp ett angivet land haft angivet år"""
        
    
    gas_megaton = 0
    try:

        if year == "2017":
            id_1 = 0
            id_1 = get_id(country)
            for id_list, gas in emission_data.emission_2017.items():
                if id_1 == id_list:
                    gas_megaton = gas*1000000


        elif year == "2005":
            id_1 = 0
            id_1 = get_id(country)
            for id_list, gas in emission_data.emission_2005.items():
                if id_1 == id_list:
                    gas_megaton = gas*1000000
                        
        elif year == "1990":
            id_1 = 0
            id_1 = get_id(country)
            for id_list, gas in emission_data.emission_1990.items():
                if id_1 == id_list:
                    gas_megaton = gas*1000000
                    
        else:
            raise ValueError
                    
    except Exception as error:
        raise ValueError from error

    if gas_megaton == 0:
        raise ValueError
        
        
    return gas_megaton     
        



        
        

def get_country_change_for_years(country, year1, year2):
    """Funktionen som räknar ut och returnera skillnaden för ett lands utsläpp mellan två år."""
    
    
    try:
        gas_year1 = get_country_year_data_megaton(country, year1) 
        gas_year2 = get_country_year_data_megaton(country, year2) 
        change_in_gas = (float(gas_year2) - float(gas_year1))
        percent_gas = (float(change_in_gas)/gas_year1)*100 
        gas_megaton = round(float(percent_gas), 2) 
        
    except Exception as error:
        raise ValueError("Wrong year!") from error        
        
    return gas_megaton         
        

        
    

    


def get_country_data(country):
    """Hämtar information som finns om ett land"""

    try:
        emission_1990 = 0
        emission_2005 = 0
        emission_2017 = 0
        emission_change1990_2005 = 0
        emission_change2005_2017 = 0
        

        emission_1990 = get_country_year_data_megaton(country, "1990")
        emission_2005 = get_country_year_data_megaton(country, "2005")
        emission_2017 = get_country_year_data_megaton(country, "2017")
        emission_change1990_2005 = get_country_change_for_years(country, "1990", "2005")
        emission_change2005_2017 = get_country_change_for_years(country, "2005", "2017")
    except ValueError:
        print("Wring")

    list_dict = dict
    
    for country_name in emission_data.country_data.items():
        if country in country_name:
            dict1 = country_name
            dict_out_of_tuple = dict1[1]
            population = dict_out_of_tuple["population"]
            
            if population == []:
                population = (None, None, None)
            population_1990 = 0
            population_2005 = 0
            population_2017 = 0
            population_1990 = population[0]
            population_2005 = population[1]
            population_2017 = population[2]


            list_dict = {"name" : country,
            '1990': {'emission': emission_1990, "population": population_1990},
            '2005': {'emission': emission_2005, "population": population_2005},
            '2017': {'emission': emission_2017, "population": population_2017},
            'emission_change': (emission_change1990_2005, emission_change2005_2017)}
    return list_dict

def print_country_data(listing_from_dict):
    """Skriver ut data om ett land"""
    
    list_from_dict = [(k, v) for k, v in listing_from_dict.items()]
    list_1990 = list_from_dict[1][1]
    list_2005 = list_from_dict[2][1]
    list_2017 = list_from_dict[3][1]
    list_change = list_from_dict[4][1]
    list_change_1 = list_change[0]
    list_change_2 = list_change[1]
    population_1990 = list_1990.get("population")
    if population_1990 is None:
        population_1990 = "Missing population data!"
    population_2005 = list_2005.get("population")
    if population_2005 is None:
        population_2005 = "Missing population data!"
    population_2017 = list_2017.get("population")
    if population_2017 is None:
        population_2017 = "Missing population data!"
    emission_1990 = list_1990.get("emission")
    emission_2005 = list_2005.get("emission")
    emission_2017 = list_2017.get("emission")
    country = list_from_dict[0][1]

    list_ready_for_print = (
    f"{country} \
    Emission 1990: {emission_1990} 2005: {emission_2005} 2017: {emission_2017}, \
    Emission change 1990-2005: {list_change_1}% 2005-2017: {list_change_2}%, \
    Population 1990: {population_1990} 2005: {population_2005} 2017: {population_2017}")



    print(list_ready_for_print)
