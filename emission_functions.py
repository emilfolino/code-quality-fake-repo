"""Emission Functions"""

import emission_data

def search_country(search_word):
    """Find country"""
    countries = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            countries.append(country)

    if len(countries) == 0:
        raise ValueError("ValueError")

    return countries

def get_country_year_data_megaton(country, year):
    """Get data from the year"""
    get_id = 0
    result = 0
    for data_country in emission_data.country_data:
        if country == data_country:
            get_id = emission_data.country_data[country]['id']
            if year == "1990":
                for ids in emission_data.emission_1990:
                    if ids == get_id:
                        result = emission_data.emission_1990[get_id] * 1000000
            elif year == "2005":
                for ids in emission_data.emission_2005:
                    if ids == get_id:
                        result = emission_data.emission_2005[get_id] * 1000000
            elif year == "2017":
                for ids in emission_data.emission_2017:
                    if ids == get_id:
                        result = emission_data.emission_2017[get_id] * 1000000
            else:
                raise ValueError("ValueError")

    return result

def get_country_change_for_years(country, year1, year2):
    """Country change for years"""
    data_year1 = get_country_year_data_megaton(country, year1)
    data_year2 = get_country_year_data_megaton(country, year2)

    data_minus = data_year1 - data_year2
    data_percent = round(data_minus / data_year1 * 100 * -1, 2)

    return data_percent


def get_country_data(country_name):
    """Get Data"""

    for data_country in emission_data.country_data:
        if country_name == data_country:
            get_population = emission_data.country_data[country_name]['population']
            if get_population == []:
                get_population = [None, None, None]

            country_change_first_decade = get_country_change_for_years(country_name,"1990","2005")
            country_change_second_decade = get_country_change_for_years(country_name,"2005","2017")

            dictionary = {'name': country_name,
            '1990':{'emission': get_country_year_data_megaton(country_name,"1990"), "population": get_population[0]},
            '2005':{'emission': get_country_year_data_megaton(country_name,"2005"), "population": get_population[1]},
            '2017':{'emission': get_country_year_data_megaton(country_name,"2017"), "population": get_population[2]},
            'emission_change':(country_change_first_decade, country_change_second_decade)
            }

    return dictionary

def print_country_data(data):
    """Print Data"""
    emission_1990 = "1990: " + str(data["1990"]["emission"]) + "\t"
    emission_2005 = "2005: " + str(data["2005"]["emission"]) + "\t"
    emission_2017 = "2017: " + str(data["2017"]["emission"])

    emission_change_1995_2005 = "1990-2005: " + str(data["emission_change"][0]) + "%\t"
    emission_change_2005_2017 = "2005-2017: " + str(data["emission_change"][1]) + "%"

    if data["1990"]["population"] is not None:
        population_1990 = "1990: " + str(data["1990"]["population"]) + "\t"
    else:
        population_1990 = "1990: Missing population data!" + "\t"

    if data["2005"]["population"] is not None:
        population_2005 = "2005: " + str(data["2005"]["population"]) + "\t"
    else:
        population_2005 = "2005: Missing population data!" + "\t"

    if data["2017"]["population"] is not None:
        population_2017 = "2017: " + str(data["2017"]["population"])
    else:
        population_2017 = "2017: Missing population data!" + "\t"


    print(data['name'])
    print("Emission\t- " + emission_1990 + emission_2005 + emission_2017)
    print("Emission change\t- " + emission_change_1995_2005 + emission_change_2005_2017)
    print("Population\t- " + population_1990 + population_2005 + population_2017)
