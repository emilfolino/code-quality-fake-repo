"""
Functions for Emission_Data
"""
import emission_data as EDS

def search_country(search_word):
    """
    Takes string, search for country
    """
    search_list = [key for key in EDS.country_data if search_word.lower() in key.lower()]
    if search_list:
        no_return_error = search_list
    else:
        raise ValueError("Country does not exist!")
    return(no_return_error)
def get_country_year_data_megaton(country, year):
    """
    Get year data_megaton
    """
    list_country = search_country(country)
    new_country = list_country[0]
    emission_data = None
    if year == "2017":
        emission_data = EDS.emission_2017
    
    elif year == "2005":
        emission_data = EDS.emission_2005
         
    elif year == "1990":
        emission_data = EDS.emission_1990
    
    else:
        raise ValueError("Wrong year!")

    country_id = EDS.country_data[new_country]['id']
    emission = emission_data[country_id]                
    mega_ton = emission * 1000000
    return mega_ton

def get_country_change_for_years(country, year1, year2 : None):
    """
    Calc diff for country between two years
    """
    year_1 = get_country_year_data_megaton(country, year1)
    year_2 = get_country_year_data_megaton(country, year2)
    if year_2 is None:
        raise IndexError("Need two countries to compare")
    diff = year_2 - year_1
    result_var = round(diff / year_1 * 100, 2)
    round(result_var, 2)
    return(result_var)
    
def get_country_data(country_name):
    """
    Get country data
    """
    final_dict = {"1990":{}, "2005":{}, "2017":{}, "emission_change": ()}
    list_country = search_country(country_name)
    new_country = list_country[0]
    final_dict["name"] = new_country
    data_list = [value["population"] for key, value in EDS.country_data.items()if new_country in key]
    
    if data_list[0]:
        pop_1990 = [x[0] for x in data_list]
        pop_2005 = [x[1] for x in data_list]
        pop_2017 = [x[2] for x in data_list]
        final_dict["1990"]["population"] = pop_1990[0]
        final_dict["2005"]["population"] = pop_2005[0]
        final_dict["2017"]["population"] = pop_2017[0]
    else:
        final_dict["1990"].setdefault("population", None)
        final_dict["2005"].setdefault("population", None)
        final_dict["2017"].setdefault("population", None)
    
    final_dict["1990"]["emission"] = get_country_year_data_megaton(new_country, "1990")
    final_dict["2005"]["emission"] = get_country_year_data_megaton(new_country, "2005")
    final_dict["2017"]["emission"] = get_country_year_data_megaton(new_country, "2017")
    final_dict["emission_change"] = (get_country_change_for_years(new_country, "1990", "2005") \
    , get_country_change_for_years(new_country, "2005", "2017"))
    return final_dict

def print_country_data(data):
    """
    Prints the data
    """
    temp_country = data.pop("name")
    temp = data.pop("emission_change")
    print(temp_country)
    for k, v in data.items():
        population_v = v['population']
        print(f"{k}: {v['emission']}")
        if population_v is None:
            print("Missing population data!")
        else:
            print(f"{k}: {population_v}")

    print(f"1990-2005: {temp[0]}%")
    print(f"2005-2017: {temp[1]}%")
