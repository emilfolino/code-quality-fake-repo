"""
Emission functions
"""

import emission_data



def search_country(search_word):
    """
    Searches up country
    """
    
    list_of_countries = list(emission_data.country_data.keys())
    country_str = ""
    searched_country:list = []
    
    for country in list_of_countries:
        country_str = country
        if search_word.lower() in country_str.lower():
            searched_country.append(country_str)
           
    if searched_country == []:
        raise ValueError("Country does not exist!")
    
    return searched_country

def get_country_year_data_megaton(country, year):
    """
    Shows the emission of a country a specific year
    """
    tuple_of_countries = tuple(emission_data.country_data)
    
    if country in tuple_of_countries:
        country_id = emission_data.country_data[country]["id"]
        
        if year in ("1990", "2005", "2017"):
            if year == "1990":
                country_emission_1990 = emission_data.emission_1990[country_id]  
                emission_megaton = float(country_emission_1990) * 1000000
            
            elif year == "2005":
                country_emission_2005 = emission_data.emission_2005[country_id]  
                emission_megaton = float(country_emission_2005) * 1000000
            elif year == "2017":
                country_emission_2017 = emission_data.emission_2017[country_id]  
                emission_megaton = float(country_emission_2017) * 1000000
        
        else:
            raise ValueError("Wrong year!")
    else:
        emission_megaton = None
    return emission_megaton
    

    
def get_country_change_for_years(country, year1, year2):
    """
    Calculates the difference of emission between years 
    """
    
    emission_year1 = get_country_year_data_megaton(country,year1)
    emission_year2 = get_country_year_data_megaton(country,year2)
    if emission_year1 is not None:
        increase = emission_year2 - emission_year1
        emission_difference = round(increase/emission_year1 * 100,2)
    else:
        raise TypeError("That country does not exist in the list!")
    return emission_difference
    

def get_country_data(country_name):
    """
    Gets info about a country
    """
    country_tuple = tuple(emission_data.country_data)
    country_data = None

    if country_name in country_tuple:
        country_data = {"name":"",
                        "1990":{"emission":"","population":""},
                        "2005":{"emission":"","population":""},
                        "2017":{"emission":"","population":""},
                        "emission_change":()
                        }
        country_data["name"] = country_name

        country_population = tuple(emission_data.country_data[country_name]["population"])

        if country_population == ():
            country_data["1990"]["population"] = None
            country_data["2005"]["population"] = None
            country_data["2017"]["population"] = None
        else:
            country_data["1990"]["population"] = country_population[0]
            country_data["2005"]["population"] = country_population[1]
            country_data["2017"]["population"] = country_population[2]
    
        
        country_data["1990"]["emission"] = get_country_year_data_megaton(country_name,"1990")
        country_data["2005"]["emission"] = get_country_year_data_megaton(country_name,"2005")
        country_data["2017"]["emission"] = get_country_year_data_megaton(country_name,"2017")
        
        country_data["emission_change"] = (get_country_change_for_years(country_name, "1990","2005"),
        get_country_change_for_years(country_name, "2005","2017"))
    if country_data is None:
        raise TypeError("That Country does not exist or is not in the list")
    return country_data

def print_country_data(data):
    """
    Prints the info about the country
    """
    if data["1990"]["population"] is not None:
        print(str(data["name"]) + "\n"
              + "Emission: " + "- 1990: " + str(data["1990"]["emission"])
              + "    " + "2005: " + str(data["2005"]["emission"])
              + "    " + "2017: " + str(data["2017"]["emission"]) +"\n"
              + "Emission change: " + "- 1990-2005: " + str(data["emission_change"][0]) + "%"
              + "    " + "2005-2017: " + str(data["emission_change"][1]) + "%" + "\n"
              + "Population: " + "- 1990: " + str(data["1990"]["population"])
              + "    " + "2005: " + str(data["2005"]["population"])
              + "    " + "2017: " + str(data["2017"]["population"]))
    
    else:
        data["1990"]["population"] = "Missing population data!"
        data["2005"]["population"] = "Missing population data!"
        data["2017"]["population"] = "Missing population data!"
        print(str(data["name"]) + "\n"
              + "Emission: " + "- 1990: " + str(data["1990"]["emission"])
              + "    " + "2005: " + str(data["2005"]["emission"])
              + "    " + "2017: " + str(data["2017"]["emission"]) +"\n"
              + "Emission change: " + "- 1990-2005: " + str(data["emission_change"][0]) + "%"
              + "    " + "2005-2017: " + str(data["emission_change"][1]) + "%" + "\n"
              + "Population: " + "- 1990: " + str(data["1990"]["population"])
              + "    " + "2005: " + str(data["2005"]["population"])
              + "    " + "2017: " + str(data["2017"]["population"]))
        