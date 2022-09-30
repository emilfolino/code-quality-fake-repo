"""
Module that takes values from dictionarys
"""
import emission_data

def search_country(search_word):
    """
    Function that looks for a country and prints out that value
    """
    l =[]
    for key in emission_data.country_data:
        search_word = search_word.lower()
        keys = key.lower()
        if search_word in keys:
            l.append(key)
    if not l:
        raise ValueError("Country doesnt exist!")
    return l

def get_country_year_data_megaton(country, year):
    """
    Function that returns emissions in megaton for a country a specific year
    """
    id_country = emission_data.country_data[country]['id']

    year = int(year)
    if year == 1990:
        return emission_data.emission_1990[id_country] * 1000000
    if year == 2005:
        return emission_data.emission_2005[id_country] * 1000000
    if year == 2017:
        return emission_data.emission_2017[id_country] * 1000000
    raise ValueError

def get_country_change_for_years(country, year1, year2):
    """
    Function that takes values from another function and returns difference
    """
    data_year1 = get_country_year_data_megaton(country, year1)
    data_year2 = get_country_year_data_megaton(country, year2)
    return round(((data_year2 - data_year1) / (data_year1) * 100), 2)

def get_country_data(country_name):
    """
    Gets pollution data from a country
    """
    pop_data = emission_data.country_data[country_name]["population"]
    if pop_data == []:
        pop_data = [None, None, None]
    change_19902005 = get_country_change_for_years(country_name, 1990, 2005)
    change_20052017 = get_country_change_for_years(country_name, 2005, 2017)

    data={
        'name': country_name,
        '1990': {'emission': get_country_year_data_megaton(country_name, 1990), 'population': pop_data[0]},
        '2005': {'emission': get_country_year_data_megaton(country_name, 2005), 'population': pop_data[1]},
        '2017': {'emission': get_country_year_data_megaton(country_name, 2017), 'population': pop_data[2]},
        'emission_change': (change_19902005, change_20052017)
}
    return data

def print_country_data(data):
    """
    Prints out the data from another function
    """
    country_name = str(data["name"])
    emission1990 = str(data["1990"]["emission"])
    emission2005 = str(data["2005"]["emission"])
    emission2017 = str(data["2017"]["emission"])
    emissionchange19902005 = str(data["emission_change"][0])
    emissionchange20052017 = str(data["emission_change"][1])
    population1990 = data["1990"]["population"]
    population2005 = data["2005"]["population"]
    population2017 = data["2017"]["population"]
    print("Name: "+ country_name)
    print("Emissions:"+" 1990: "+emission1990+" 2005: "+emission2005+ " 2017: "+emission2017)
    print("Emission change:", "1990-2005: " + emissionchange19902005 +"%" " 2005-2017: " + emissionchange20052017 + "%")
    if population1990 is None:
        print("Missing population data!")
    else:
        print("Population:", "1990:", population1990, " 2005:" , population2005, " 2017:" , population2017)
