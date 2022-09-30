"""
module for main.py
"""
import emission_data

def search_country(search_word):
    """
    Return countries which contains search_word.
    """
    answers = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            answers.append(country)
    if answers == []:
        raise ValueError
    return answers

def get_country_year_data_megaton(country, year):
    """
    Calculate the emission of a country at a given year.
    """
    country_id = emission_data.country_data[country]["id"]
    try:
        country_emission = getattr(emission_data, f"emission_{year}")[country_id]
    except Exception as e:
        raise ValueError from e
        
    return country_emission * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Calculate the emission difference of a country between given years.
    """
    first_year_value = get_country_year_data_megaton(country, year1)
    second_year_value = get_country_year_data_megaton(country, year2)

    difference_in_emission = second_year_value / first_year_value
    difference_in_percent = round((difference_in_emission*100 - 100), 2)
    return difference_in_percent

def get_country_data(country_name):
    """
    Get country by country name.
    """
    emission_1990 = get_country_year_data_megaton(country_name, "1990")
    emission_2005 = get_country_year_data_megaton(country_name, "2005")
    emission_2017 = get_country_year_data_megaton(country_name, "2017")

    try:
        population_1990 = emission_data.country_data[country_name]["population"][0]
        population_2005 = emission_data.country_data[country_name]["population"][1]
        population_2017 = emission_data.country_data[country_name]["population"][2]
    except IndexError:
        population_1990, population_2005, population_2017 = (None, None, None)


    emission_change_1 = get_country_change_for_years(country_name, 1990, 2005)
    emission_change_2 = get_country_change_for_years(country_name, 2005, 2017)

    country_dict = {
        "name": country_name,
        "1990":{
            "emission": emission_1990,
            "population": population_1990,
        },
        "2005":{
            "emission": emission_2005,
            "population": population_2005,
        },
        "2017":{
            "emission": emission_2017,
            "population": population_2017,
        },
        "emission_change": (emission_change_1, emission_change_2)
    }

    return country_dict

def print_country_data(data):
    """
    Print country data.
    """
    print(data["name"])
    print("Emission - 1990:", data["1990"]["emission"],
        "2005:", data["2005"]["emission"],
        "2017:", data["2017"]["emission"])

    if data["1990"]["population"]:
        print("Population - 1990:", data["1990"]["population"],
            "2005:", data["2005"]["population"],
            "2017:", data["2017"]["population"])
    else:
        print("Missing population data!")

    print("Emission change - 1990-2005:", str(data["emission_change"][0])+"%",
        "2005-2017:", str(data["emission_change"][1])+"%")
#Om invånare data saknas (är None) skriv ut "Missing population data!" istället för <år>: <antal invånare>.
