"""
Functions for Marvin4 regarding emissions.
"""

import emission_data


def search_country(search_word):
    """
    Function to search for a country in a dictionary
    """
    list_exist = [] # list for all countries which has been found with the search string
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            list_exist.append(country)
            #print("Yes!")

    if not list_exist: # check to see if list is empty, empty = False
        raise ValueError("Country does not exist!")
    #else:
    list_str = ", ".join(list_exist)
    # print(list_exist)
    print(f"Following countries were found: {list_str}")
    return list_exist


def get_country_year_data_megaton(country, year):
    """
    Function to return a country's emission
    """
    # get country ID
    country_id = emission_data.country_data[country]["id"]
    #print(emission_data_small.country_data[country]["id"])
    #print(country_id)

    if year == "1990":
        country_emission = emission_data.emission_1990.get(country_id) * 1000000
        #print(country_emission)
    elif year == "2005":
        country_emission = emission_data.emission_2005.get(country_id) * 1000000
        #print(country_emission)
    elif year == "2017":
        country_emission = emission_data.emission_2017.get(country_id) * 1000000
        #print(country_emission)
    else:
        raise ValueError("Wrong year!")
    return country_emission





def get_country_change_for_years(country, year1, year2):
    """
    Calculates difference in years for a country's emission
    """
    first_year = get_country_year_data_megaton(country, year1)
    second_year = get_country_year_data_megaton(country, year2)
    result = round((second_year / first_year) * 100 - 100, 2)
    #print(first_year)
    #print(second_year)
    #print(f"{country}:{result}%")
    return result



def get_country_data(country_name):
    """
    Function to print a country's data
    """
    emis_dict = {}
    # search for country in emission
    for country in emission_data.country_data:
        # get country's value from population , if no = None
        if country_name in country:
            try:
                country_pop_90 = emission_data.country_data[country_name].get("population")[0]
                country_pop_05 = emission_data.country_data[country_name].get("population")[1]
                country_pop_17 = emission_data.country_data[country_name].get("population")[2]
            except IndexError: #OBS! Fungerar endast om hela population är tom!
                country_pop_90 = None
                country_pop_05 = None
                country_pop_17 = None

            #get emission in ton from above functions
            country_emis_90 = get_country_year_data_megaton(country_name,"1990")
            country_emis_05 = get_country_year_data_megaton(country_name,"2005")
            country_emis_17 = get_country_year_data_megaton(country_name,"2017")

            # get emission change 1990-2005, 2005-2017
            emis_change_90 = get_country_change_for_years(country_name, "1990", "2005")
            emis_change_17 = get_country_change_for_years(country_name, "2005", "2017")

            emis_dict = {
                "name" : country_name,
                "1990" : {"emission" : country_emis_90, "population" : country_pop_90},
                "2005" : {"emission" : country_emis_05, "population" : country_pop_05},
                "2017" : {"emission" : country_emis_17, "population" : country_pop_17},
                "emission_change" : (emis_change_90, emis_change_17)
            }
    return emis_dict

def print_country_data(data):
    """
    Function to format the data
    """
    # dict who shall be printed
    print_dict = data

    # OBS! Utifrån hur dictionarien är uppbyggd "fungerar" det här sättet...
    if print_dict.get('1990')['population'] is not None: 
        print_emis = f"{print_dict.get('name')} \nEmission - \t1990: {print_dict.get('1990')['emission']} " \
        f"\t2005: {print_dict.get('2005')['emission']} \t2017: {print_dict.get('2017')['emission']} "
        print_chg = f"\nEmission change - \t1990-2005: {print_dict.get('emission_change')[0]}%" \
        f"\t2005-2017: {print_dict.get('emission_change')[1]}%"
        print_pop = f"\nPopulation - \t1990: {print_dict.get('1990')['population']}" \
        f"\t2005: {print_dict.get('2005')['population']} \t2017: {print_dict.get('2017')['population']}"
        print(print_emis, print_chg, print_pop)
    else:
        print_emis = f"{print_dict.get('name')} \nEmission - \t1990: {print_dict.get('1990')['emission']} " \
        f"\t2005: {print_dict.get('2005')['emission']} \t2017: {print_dict.get('2017')['emission']} "
        print_chg = f"\nEmission change - \t1990-2005: {print_dict.get('emission_change')[0]}%" \
        f"\t2005-2017: {print_dict.get('emission_change')[1]}%"
        print_pop = "\nPopulation - \tMissing population data!"
        print(print_emis, print_chg, print_pop)


if __name__ == "__main__":
    print_country_data("United States of America")
