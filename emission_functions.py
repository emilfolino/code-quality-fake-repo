"""
Module that contains all the funtions tha manages data.
"""
import emission_data


def search_country(search_word):
    """
    Funtoins to check whether a country is 
    in data or not.
    """
    list_counties = []
    
    for key in emission_data.country_data:
        if str(search_word).lower() in key.lower():
            list_counties.append(key)


    if len(list_counties) == 0:
        raise ValueError
    
        
    return list_counties



def get_country_year_data_megaton(country,year1):
    """
    Finction that return the emission in ton 
    for a given year.
    """
    for key in emission_data.country_data:

        if str(country).lower() == key.lower():
            id_country = emission_data.country_data.get(key)
            id_emission = id_country.get("id")

            if year1 == "1990":
                emission = emission_data.emission_1990.get(id_emission)*1000000
            elif year1 == "2005":
                emission = emission_data.emission_2005.get(id_emission)*1000000
            elif year1 == "2017":
                emission = emission_data.emission_2017.get(id_emission)*1000000
            else:
                raise ValueError
        

    return emission



def get_country_change_for_years(country, year1, year2):
    """
    Funtion that returns change in emession for sepecific 
    period of time.
    """
    for key in emission_data.country_data:

        if str(country).lower() == key.lower():
            id_country = emission_data.country_data.get(key)
            id_emission = id_country.get("id")

            if year2 == "1990":
                emission = emission_data.emission_1990.get(id_emission)
            elif year2 == "2005":
                emission = emission_data.emission_2005.get(id_emission)
            elif year2 == "2017":
                emission = emission_data.emission_2017.get(id_emission)
            else:
                raise ValueError

    change = emission * 100000000/ float(get_country_year_data_megaton(country,year1)) - 100
    change = (round(change,2))
    return change



def get_country_data(country_name):
    """
    Funtion that gets country data by asking for country name.
    """

    for key in emission_data.country_data:
        check_list = []
        if str(country_name).lower() in key.lower():
            check_list.append(key)
            if len(check_list) == 0:
                raise ValueError
        

               
            if str(country_name).lower() == str(key).lower():
                country_name = key
                country_info = emission_data.country_data.get(key)
                population = country_info.get("population")
                emission_1990 = get_country_year_data_megaton(country_name,year1="1990")
                emission_2005 = get_country_year_data_megaton(country_name,year1="2005")
                emission_2017 = get_country_year_data_megaton(country_name,year1="2017")
                emission_change_1990_2005 = (get_country_change_for_years(country_name,year1="1990",year2="2005"))
                emission_change_2005_2017 = (get_country_change_for_years(country_name,year1="2005",year2="2017"))

                if len(population)==3:
                
                    population_1990 = (population[0])
                    population_2005 = (population[1])
                    population_2017 = (population[2])

                    data = {

                        "name" : country_name,
                    "1990" : {"emission": emission_1990,"population": population_1990},
                    "2005" : {"emission": emission_2005,"population": population_2005},
                    "2017" : {"emission": emission_2017,"population": population_2017},
                        "emission_change": (emission_change_1990_2005,emission_change_2005_2017)
                            }
                else: 
                    data = {
                        "name" : country_name,
                    "1990" : {"emission": emission_1990, "population": None},
                    "2005" : {"emission": emission_2005, "population": None},
                    "2017" : {"emission": emission_2017, "population": None},
                        "emission_change": ((emission_change_1990_2005,emission_change_2005_2017))

                        }
                
    return data


def print_country_data(data):
    """
    Function that organize data and prints it by
    reading data from user.
    """
    countryName = data.get("name") 
    info_1990 = data.get("1990")
    info_2005 = data.get("2005")
    info_2017 = data.get("2017")
    emission_change = data.get("emission_change")

    change_1 = emission_change[0]
    change_2 = emission_change[1]
    if info_1990["population"] is None:
        info_1990["population"] = "Missing population data!"
    
    if info_2005["population"] is None:
        info_2005["population"] = "Missing population data!"
    
    if info_2017["population"] is None:
        info_2017["population"] = "Missing population data!"

    reformated_data =    countryName + "\n" + str(["1990: " + str(data.get("1990").get("emission")),
    
                                    "2005: " + str(data.get("2005").get("emission")),
                                    "2017: " + str(data.get("2017").get("emission")),
                                    "1990-2005: " + str(change_1)+"%",
                                    "2005-2017: " + str(change_2)+"%",
                                    "1990: " +str(info_1990["population"]) ,
                                    "2005: " +str(info_2005["population"]) ,
                                    "2017: " + str(info_2017["population"])
                                 ])
                        
                    
    print(reformated_data)  
    return reformated_data
    