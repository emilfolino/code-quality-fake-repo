"""
Functions for emission-calls
"""
from emission_data import country_data, emission_1990, emission_2005, emission_2017



def search_country(search_word):
    """
    Function for searching
    """
    result = []
    for key in country_data:
        if search_word.lower() in key.lower():
            result.append(key)
    if not result:
        raise ValueError
    
    return result

def get_country_year_data_megaton(country, year):
    """
    Function for collecting numbers of emission
    """
    result = ""

    country_id = country_data[country]["id"]
    
    if year == "1990":
        result = float(emission_1990[country_id]) * 1000000
    
    elif year == "2005":
        result = float(emission_2005[country_id]) * 1000000
    
    elif year == "2017":
        result = float(emission_2017[country_id]) * 1000000

    if not result:
        raise ValueError

    return result


def get_country_change_for_years(country, year1, year2):
    """
    Function for calculating emission change between years
    """
    year1_megaton = get_country_year_data_megaton(country, year1)
    year2_megaton = get_country_year_data_megaton(country, year2)

    calculate_change = round(((year2_megaton - year1_megaton) / year1_megaton) * 100, 2)

    return calculate_change

def get_country_data(country_name):
    """
    Function for retrieving country data
    """
    if not country_data[country_name]["population"]:
        country_info = {
        "name" : country_name,
        
        "1990" : {"emission" : get_country_year_data_megaton(country_name,
            "1990"), "population" : None},
        
        "2005" : {"emission" : get_country_year_data_megaton(country_name,
            "2005"), "population" : None},
        
        "2017" : {"emission" : get_country_year_data_megaton(country_name,
            "2017"), "population" : None},
        
        "emission_change" : (get_country_change_for_years(country_name, "1990", "2005"),
            get_country_change_for_years(country_name, "2005", "2017"))
    }

    else:
    
        country_info = {
            "name" : country_name,
            
            "1990" : {"emission" : get_country_year_data_megaton(country_name,
                "1990"), "population" : country_data[country_name]["population"][0]},
            
            "2005" : {"emission" : get_country_year_data_megaton(country_name, "2005"),
                "population" : country_data[country_name]["population"][1]},
            
            "2017" : {"emission" : get_country_year_data_megaton(country_name, "2017"),
                "population" : country_data[country_name]["population"][2]},
            
            "emission_change" : (get_country_change_for_years(country_name, "1990", "2005"),
                get_country_change_for_years(country_name, "2005", "2017"))
        }
    
    return country_info


def print_country_data(data):
    """
    Function for printing country data
    """
    print(data["name"])
    
    print("Emission     - 1990: " + str(data["1990"]["emission"]) + "   2005: " +
        str(data["2005"]["emission"]) + "  2017: " + str(data["2017"]["emission"]))
    
    print("Emission change     - 1990-2005: " + str(data["emission_change"][0]) +
        "%   " + "2005-2017: " + str(data["emission_change"][1]) + "%")
    
    if data["1990"]["population"] is None:
        print("Missing population data!")
    
    else:
        print("Population      - 1990: " + str(data["1990"]["population"]) + "  2005: " +
            str(data["2005"]["population"]) + "   2017: " + str(data["2017"]["population"]))








"""
Function for change of emission between years
"""
