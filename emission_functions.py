"""
A module with functions for marvin options kmom05
"""
from operator import itemgetter
import emission_data

# def test(country):
#     get_population = emission_data.country_data[country]["population"]
#     if get_population == []:
#         get_population = [None, None, None]
#     print(get_population)
#     print(get_population[1])

# test("Sweden")
# test("Bermuda")

def search_country(search_word):
    """
    Menu option 12, search for countries
    """
    list_names_found = []

    for key, _ in emission_data.country_data.items():
        if search_word.lower() in key.lower():
            list_names_found.append(key)
    if list_names_found == []:
        raise ValueError("Country does not exist!")
    return list_names_found



def get_country_year_data_megaton(country, year):
    """
    Called from get_country_change_for_years()
    """
    year = int(year)

    country_id = emission_data.country_data[country]["id"]
    if year == 1990:
        return emission_data.emission_1990[country_id] * 1000000
    if year == 2005:
        return emission_data.emission_2005[country_id] * 1000000
    if year == 2017:
        return emission_data.emission_2017[country_id] * 1000000
    raise ValueError("Wrong year!")

def get_country_change_for_years(country, year1, year2):
    """
    Menu option 13, check pollution change in country
    """
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    change_in_percent = round((emission_year2/ emission_year1 - 1) * 100, 2)
    return change_in_percent

# print(get_country_change_for_years("China", 1990, 2017))
# print(get_country_change_for_years("China", 1000, 2017))

def get_country_data(country_name):
    """
    Menu option 14, makes dictionary of facts of a country and calls print_country_data
    """
    if len(emission_data.country_data[country_name]["population"]) < 3:
        dict_countries = {
            "name" : country_name,
            "1990" : {
                "emission": get_country_year_data_megaton(country_name, "1990"),
                "population": None
            },
            "2005": {
                "emission": get_country_year_data_megaton(country_name, "2005"),
                "population": None
            },
            "2017": {
                "emission": get_country_year_data_megaton(country_name, "2017"),
                "population": None
            },
            "emission_change" : (
                get_country_change_for_years(country_name, "1990", "2005"),
                get_country_change_for_years(country_name, "2005", "2017")
                )
        }
    else:
        dict_countries = {
            "name": country_name,
            "1990": {
                "emission": get_country_year_data_megaton(country_name, 1990),
                "population": emission_data.country_data[country_name]["population"][0]
            },
            "2005": {
                "emission": get_country_year_data_megaton(country_name, 2005),
                "population": emission_data.country_data[country_name]["population"][1]
            },
            "2017": {
                "emission": get_country_year_data_megaton(country_name, 2017),
                "population": emission_data.country_data[country_name]["population"][2]
            },
            "emission_change": (
                get_country_change_for_years(country_name, 1990, 2005),
                get_country_change_for_years(country_name, 2005, 2017)
            )
        }
    return dict_countries

def print_country_data(data):
    """
    Prints out facts about a country
    """

    str_print = ""
    if data["1990"]["population"] is None:
        str_print = (
            f"\n{data['name']}"
            f"\nEmission:"
            f"    1990: {data['1990']['emission']} megaton"
            f"    2005: {data['2005']['emission']} megaton"
            f"    2017: {data['2017']['emission']} megaton"
            f"\nEmission Change:"
            f"    1990-2005: {data['emission_change'][0]}%"
            f"    2005-2017: {data['emission_change'][1]}%"
            f"\nPopulation:"
            f"    Missing population data!"
        )
    else:
        str_print = (
            f"\n{data['name']}"
            f"\nEmission:"
            f"    1990: {data['1990']['emission']} megaton"
            f"    2005: {data['2005']['emission']} megaton"
            f"    2017: {data['2017']['emission']} megaton"
            f"\nEmission Change:"
            f"    1990-2005: {data['emission_change'][0]}%"
            f"    2005-2017: {data['emission_change'][1]}%"
            f"\nPopulation:"
            f"    1990: {data['1990']['population']}"
            f"    2005: {data['2005']['population']}    2017: {data['2017']['population']}"
        )
    print(str_print)

def worst_countries(year, list_length):
    """
    Returns a list of worst CO2 pollution countries in the world
    """
    year = int(year)
    list_length = int(list_length)

    list_all_countries = []

    # Får dictionarien i speciell dict.item.lista i form av tupelpar och lägger in dem i en "vanlig" lista
    if year == 1990:
        for tup in emission_data.emission_1990.items():
            list_all_countries.append(tup)
    elif year == 2005:
        for tup in emission_data.emission_2005.items():
            list_all_countries.append(tup)
    elif year == 2017:
        for tup in emission_data.emission_2017.items():
            list_all_countries.append(tup)
    else:
        raise ValueError("Wrong year!")

    # Sorterar alla på value med itemgetter (import operator) från störst till minst
    sorted_list_all_countries = sorted(list_all_countries, key=itemgetter(1),reverse = True)
    list_shortend = sorted_list_all_countries[:list_length]

    # Kollar av id-match och om det matchar skriv ut <land>:< utsläpp>
    # I dict.item.listan är key landets namn och value all fakta
    for tup in list_shortend:
        for key, value in emission_data.country_data.items():
            if tup[0] == value["id"]:
                print(f"{key}: {tup[1] * 1000000}")
