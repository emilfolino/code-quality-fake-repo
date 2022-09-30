"""
Functions Docstring
"""
import emission_data

def search_country(search_word):
    """
    Choice #12 
    Searches for a country
    """
    countries_list = []
    for countries in emission_data.country_data:
        if search_word.lower() in countries.lower():
            countries_list.append(countries)
    if len(countries_list) == 0:
        raise ValueError("Country does not exist!")
    
    return countries_list



def get_country_year_data_megaton(country, year):
    """
    Function 13 part 1
    """
    key = emission_data.country_data[country]["id"]


    value = ""


    if year == "1990":
        value = emission_data.emission_1990[key] * 1000000
    elif year == "2005":
        value = emission_data.emission_2005[key] * 1000000
    elif year == "2017":
        value = emission_data.emission_2017[key] * 1000000
    else:
        raise ValueError("Wrong year!")
    return value

def get_country_change_for_years(country, year1, year2):
    """
    Function 13 part 2
    """

    first_year = get_country_year_data_megaton(country, year1)
    second_year = get_country_year_data_megaton(country, year2)

    calculated_value = (second_year - first_year) / first_year
    return round(calculated_value * 100, 2)


def get_country_data(country_name):
    """
    Function to get data from different countries
    """
    country_dict = {}

    for country in emission_data.country_data:
        if country_name.lower() in country.lower():
            #Country population value
            try:
                country_pop_90 = emission_data.country_data[country_name].get("population")[0]
                country_pop_05 = emission_data.country_data[country_name].get("population")[1]
                country_pop_17 = emission_data.country_data[country_name].get("population")[2]
            except IndexError:
                country_pop_90 = None
                country_pop_05 = None
                country_pop_17 = None
            #Get emission values
            country_emission_90 = get_country_year_data_megaton(country_name, "1990")
            country_emission_05 = get_country_year_data_megaton(country_name, "2005")
            country_emission_17 = get_country_year_data_megaton(country_name, "2017")

            #Emission change between the different years: 
            emission_change_9005 = get_country_change_for_years(country_name, "1990", "2005")
            emission_change_0517 = get_country_change_for_years(country_name, "2005", "2017")

            country_dict = {
                "name" : country_name,
                "1990" : {"emission" : country_emission_90, "population" : country_pop_90},
                "2005" : {"emission" : country_emission_05, "population" : country_pop_05},
                "2017" : {"emission" : country_emission_17, "population" : country_pop_17},
                "emission_change" : (emission_change_9005, emission_change_0517)
            }
    return country_dict




def print_country_data(data):
    """
    Print data from emission functions
    """
    name = data["name"]
    emiss_90 = data["1990"]["emission"]
    emiss_05 = data["2005"]["emission"]
    emiss_17 = data["2017"]["emission"]

    population_90 = data["1990"]["population"]
    population_05 = data["2005"]["population"]
    population_17 = data["2017"]["population"]

    if population_90 is None:
        print("Missing population data!")
    if population_05 is None:
        print("Missing population data!")
    if population_17 is None:
        print("Missing population data!")


    emission_change_1 = data["emission_change"][0]
    emission_change_2 = data["emission_change"][1]
    print(name)
    print("Emission", "1990:", emiss_90, "2005:", emiss_05, "2017:", emiss_17)
    print(f"Emission change 1990-2005: {emission_change_1}% 2005-2017: {emission_change_2}%")
    print("Population", "1990:", population_90, "2005:", population_05, "2017:", population_17)
