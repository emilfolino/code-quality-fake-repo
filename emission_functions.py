"""
Emission Functions page
"""
import emission_data

def search_country(search_word):
    """
    Search country
    """
    list_country = emission_data.country_data.keys()
    out = []

    for country in list_country:
        temp = country 
        if str(search_word).lower() in temp.lower():
            out.append(country)
    if out == []:
        raise ValueError
    return out

def get_country_year_data_megaton(country, year):
    """
    Get megaton data
    """
    country_id = emission_data.country_data.get(country).get("id")
    data = 0
    if year == "1990":
        data = emission_data.emission_1990.get(country_id) * 1000000
    elif year == "2005":
        data = emission_data.emission_2005.get(country_id) * 1000000
    elif year == "2017":
        data = emission_data.emission_2017.get(country_id) * 1000000
    else:
        raise ValueError

    return data

def get_country_change_for_years(country, year1, year2):
    """
    Converts the data form get_country_year_data_megaton in to procent
    """
    emission_data1 =  get_country_year_data_megaton(country, year1)
    emission_data2 = get_country_year_data_megaton(country, year2)
    
    procent = round((((emission_data2 / emission_data1) - 1) * 100), 2)

    return procent

def get_country_data(country_name):
    """
    Data of country
    """
    country_pop = emission_data.country_data.get(country_name).get("population")
    if country_pop == []:
        country_pop = (None, None, None)
    Change1 = get_country_change_for_years(country_name, "1990", "2005")
    Change2 = get_country_change_for_years(country_name, "2005", "2017")
    dict_info = {
        "name": country_name,
        "1990": {"emission": get_country_year_data_megaton(country_name, "1990"), "population": country_pop[0]},
        "2005": {"emission": get_country_year_data_megaton(country_name, "2005"), "population": country_pop[1]},
        "2017": {"emission": get_country_year_data_megaton(country_name, "2017"), "population": country_pop[2]},
        "emission_change": (Change1, Change2)
    }
    return(dict_info)

def print_country_data(data):
    """
    Prints out the data from get_country_data
    """
    E_1990 = data.get("1990").get("emission")
    E_2005 = data.get("2005").get("emission")
    E_2017 = data.get("2017").get("emission")
    Change1, Change2 = data.get("emission_change")
    P_1990 = data.get("1990").get("population")
    P_2005 = data.get("2005").get("population")
    P_2017 = data.get("2017").get("population")

    if P_2017 is None:
        P_1990 = "Missing population data!"
        P_2005 = "Missing population data!"
        P_2017 = "Missing population data!"

    print(data.get("name"))
    print(f"Emission durring the year of -  1990: {E_1990}   2005: {E_2005}    2017: {E_2017}")
    print(f"Population                   -  1990: {P_1990}   2005: {P_2005}   2017: {P_2017}")
    print(f"Emission change              -  1990-2005: {Change1}%    2005-2017: {Change2}%")
    

def list_to_string(in_data):
    """
    Converst list to string
    """
    text = ""
    for n in in_data:
        text += " "+ n + ","
    text = text[0 : len(text)-1]
    return text

if __name__ == "__main__":
    info = get_country_data("Sweden")
    print_country_data(info)
