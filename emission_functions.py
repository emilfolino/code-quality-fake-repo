"""
Module for marvin4
"""


import emission_data

def search_country(search_word):
    """Examines if input of part of country name/country name exists, prints out matching countries"""

    #jämför vårt input med dict country_data, case insensitive, lägger key-matchningar i en lista
    matching_countries = [key for key in emission_data.country_data \
        if search_word.lower() in key.lower()]             

    #Blev det matchning så borde listan ha en elements som utgör en längd
    if len(matching_countries):             
        print("Following countries were found:" + str(matching_countries))      
    else:
        raise ValueError("Country does not exist!")

    return matching_countries

def get_country_year_data_megaton(country, year1):
    """returnera hur mycket utsläpp ett land gjorde ett specifikt år, \
        i måttet ton (du behöver multiplicera datan med 1000000.)"""

    #Jämför vårt input, om det finns i dict country_data läggs key till i listan)
    matching_country_name_list = [key for key in emission_data.country_data \
        if country.lower() == key.lower()]         
    
    if len(matching_country_name_list) == 0:
        raise ValueError("Wrong country!")

    country_name = matching_country_name_list[0]                            #Plocka ut landets namn, key, från listan
    country_id = int(emission_data.country_data[country_name]["id"])        #Hämta landets id och gör till integer 

    if year1 == "1990":
        emission = emission_data.emission_1990[country_id] * 1000000
    elif year1 == "2005":
        emission = emission_data.emission_2005[country_id] * 1000000
    elif year1 == "2017":
        emission = emission_data.emission_2017[country_id] * 1000000
    
    
    else:
        #Om årtalet som skickas in inte finns ska funktionen lyfta ett ValueError.
        raise ValueError("Wrong year!")      

    return emission

def get_country_change_for_years(country, year1, year2):
    """Räkna ut med hur många procent utsläppen har ändrats mellan year1 \
        och year2, avrunda till två decimaler."""

    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)

    emission_difference_procent = round(((emission_year2 / emission_year1 * 100) - 100), 2)
    return emission_difference_procent
    
def get_country_pop(country_name):
    """funktion för att hämta ett lands population."""
    country_pop = [country_tuple[1]["population"] \
        for country_tuple in emission_data.country_data.items() if country_name.lower() == country_tuple[0].lower()][0]
    return country_pop

def get_country_data(country_name):
    """samla all data för ett land och skriv ut den."""

    country_pop = get_country_pop(country_name)
    
    if len(country_pop) == 0:
        country_pop = (None, None, None)

    dict_country = {}
    dict_country["name"] = country_name
    dict_country["1990"] = {"emission":get_country_year_data_megaton(country_name, "1990"), "population":country_pop[0]}
    dict_country["2005"] = {"emission":get_country_year_data_megaton(country_name, "2005"), "population":country_pop[1]}
    dict_country["2017"] = {"emission":get_country_year_data_megaton(country_name, "2017"), "population":country_pop[2]}
    dict_country["emission_change"] = (get_country_change_for_years(country_name, "1990", "2005")),\
        (get_country_change_for_years(country_name, "2005", "2017"))

    return dict_country

def print_country_data(country_data):
    """Använd print_country_data för att skriva ut datan du får från get_country_data."""

    print(country_data["name"])
    print("1990:", country_data["1990"]["emission"], "\t 2005:", country_data["2005"]["emission"], \
        "\t 2017:", country_data["2017"]["emission"])
    print("1990-2005: " + str(country_data["emission_change"][0]) + "%" + \
        "\t 2005-2017: " + str(country_data["emission_change"][1]) + "%")
    
    country_pop = get_country_pop(country_data["name"])
    if len(country_pop) == 0:
        print("Missing population data!")

    else:
        print("1990:", country_data["1990"]["population"], \
            "\t\t 2005:", country_data["2005"]["population"], \
                "\t 2017:", country_data["2017"]["population"])
