"Module for fetching emission data"
import emission_data

valid_years = {"1990", "2005", "2017"}


def search_country(search_word):
    """
    Search for a country, partial strings are OK. Case in-sensitive.
    """
    countries = emission_data.country_data.keys()
    countries = [c for c in countries if search_word.lower() in c.lower()]
    if len(countries) == 0:
        raise ValueError("No countries found")
    return countries


def get_country_year_data_megaton(country, year):
    """
    Get the emissions for a specified country and year.
    """
    if year not in valid_years:
        raise ValueError
    country_id = emission_data.country_data.get(country).get("id")
    if year == "1990":
        emissions = emission_data.emission_1990.get(country_id)
    elif year == "2005":
        emissions = emission_data.emission_2005.get(country_id)
    else:
        emissions = emission_data.emission_2017.get(country_id)
    return emissions * 1000000


def get_country_change_for_years(country, year1, year2):
    """
    Get the difference in emissions between two years for a country.
    """
    try:
        emission1 = get_country_year_data_megaton(country, year1)
        emission2 = get_country_year_data_megaton(country, year2)
        delta = emission2 - emission1
        change_percentage = (delta / emission1) * 100
        return round(change_percentage, 2)
    except ValueError as value_error:
        raise value_error


def get_country_data(country_name):
    """
    Get aggregated emission data for a specified country.
    """
    emissions_1990 = get_country_year_data_megaton(country_name, "1990")
    emissions_2005 = get_country_year_data_megaton(country_name, "2005")
    emissions_2017 = get_country_year_data_megaton(country_name, "2017")
    emissions_change_1990_2005 = get_country_change_for_years(country_name, "1990", "2005")
    emissions_change_2005_2017 = get_country_change_for_years(country_name, "2005", "2017")
    population = emission_data.country_data.get(country_name).get("population")
    country_dict = {
        "name": country_name,
        "1990": {
            "emission": emissions_1990,
            "population": population[0]
            if len(population) > 0 and population[0] is not None
            else None,
        },
        "2005": {
            "emission": emissions_2005,
            "population": population[1]
            if len(population) > 1 and population[1] is not None
            else None,
        },
        "2017": {
            "emission": emissions_2017,
            "population": population[2]
            if len(population) > 2 and population[2] is not None
            else None,
        },
        "emission_change": (emissions_change_1990_2005, emissions_change_2005_2017),
    }
    return country_dict


def print_country_data(data):
    """
    Print country information given an info dictionary fetched from get_country_data.
    """
    print(data["name"])
    print(
        f"Emission           - 1990: {data['1990']['emission']}  2005: {data['2005']['emission']}  "
        f"  2017: {data['2017']['emission']}"
    )
    print(
        f"Emission change    - 1990-2005: {data['emission_change'][0]}%  2005-2017:"
        f" {data['emission_change'][1]}%"
    )
    print(
        "Population         - 1990:"
        f" {data.get('1990').get('population') if data.get('1990').get('population') is not None else 'Missing population data!'}"  # pylint: disable=line-too-long
        "   2005:"  # pylint: disable=line-too-long
        f" {data.get('2005').get('population') if data.get('1990').get('population') is not None else 'Missing population data!'}"
        "   2017:"  # pylint: disable=line-too-long
        f" {data.get('2017').get('population') if data.get('1990').get('population') is not None else 'Missing population data!'}"  # pylint: disable=line-too-long
    )


def format_list(l):
    """
    Utility function to print a list prettily.
    """
    s = ""
    for i in l:
        s += i + ", "
    return s[:-2]
