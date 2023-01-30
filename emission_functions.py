"""
A module for emission functions in Marvin step 4, kmom05
"""

from operator import itemgetter
import emission_data

# Menu choice == "12"
def search_country(search_word):
    """
    Allows user to search for a country
    """
    matching = []
    matched = 0
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            matched += 1
            matching.append(key)
    if not matched:
        raise ValueError("Country does not exist!")
    return matching

# Used with menu choice == "13" and many other menu choices
def get_country_year_data_megaton(country, year):
    """
    Returns a country's emission data of a specific year in tons.
    """
    if year == "1990":
        year_emission = emission_data.emission_1990
    elif year == "2005":
        year_emission = emission_data.emission_2005
    elif year == "2017":
        year_emission = emission_data.emission_2017
    else:
        raise ValueError("Wrong year!")
    country_id = emission_data.country_data[country]["id"]
    data_in_ton = year_emission[country_id] * 1000000
    return data_in_ton

# Menu choice == "13"
def get_country_change_for_years(country, year1, year2):
    """
    Calculates and returns a country's difference in emission 
    between two years.
    """
    # year2 / year1 round to 2 decimals
    data_year1 = get_country_year_data_megaton(country, year1)
    data_year2 = get_country_year_data_megaton(country, year2)
    percentage_difference = round(
        ((data_year2 - data_year1) / data_year1 * 100), 2
    )
    return percentage_difference

# Used with menu choice == "14"
def get_country_data(country_name):
    """
    Returns a dictionary of obtained country data and returns it.

    'name': '<name>',
    '1990': {'emission': <utsläppp i ton>, 'population': <antal eller None>},
    '2005': {'emission': <utsläppp i ton>, 'population': <antal eller None>},
    '2017': {'emission': <utsläppp i ton>, 'population': <antal eller None>},
    'emission_change': (<skillnad mellan 1990-2005>, <skillnad mellan 2005-2017>)
    """
    if emission_data.country_data[country_name]["population"] == []:
        population = (None, None, None)
    else:
        population = emission_data.country_data[country_name]["population"]
    data_country = {}
    data_country["name"] = country_name
    data_country["1990"] = {
        "emission" : get_country_year_data_megaton(country_name, "1990"),
        "population" : population[0]
    }
    data_country["2005"] = {
        "emission" : get_country_year_data_megaton(country_name, "2005"),
        "population" : population[1]
    }
    data_country["2017"] = {
        "emission" : get_country_year_data_megaton(country_name, "2017"),
        "population" : population[2]
    }
    data_country["emission_change"] = (
        (get_country_change_for_years(country_name, "1990", "2005")), 
        (get_country_change_for_years(country_name, "2005", "2017"))
    )
    return data_country

# Menu choice == "14"
def print_country_data(data):# Can not print "Missing population data!" for output !!!!
    """
    Prints out a country's data as follows:

    "<name of country>"
    "<year>: <emission of year in ton>"
    "<year>: <population in year>"
    "<year>-<year>: <emission change in percent>"
    """
    if data["1990"]["population"] is None:
        population_info = (
        "Missing population data!", "Missing population data!", "Missing population data!"
    )
    else:
        population_info = (
        (data["1990"]["population"]), (data["2005"]["population"]), (data["2017"]["population"])
    )
    print(data["name"])
    print(
f"""
    Emission - 1990: {data['1990']['emission']}, 2005: {data['2005']['emission']}, 2017: {data['2017']['emission']}
    Population - 1990: {population_info[0]}, 2005: {population_info[1]}, 2017: {population_info[2]} 
    Emission change - 1990-2005: {data['emission_change'][0]}%, 2005-2017: {data['emission_change'][1]}%
"""
)

# Menu choice == "e1"
def print_country_emmission_in_year(year, number=0):
    """
    Prints out the CO2 emission of every country during a given year 
    from highest emission. 
    """

    def every_country_emission_to_list(dictionary):
        """
        Creates a list co2_emission where each element is a tuple consisting of
        (country_name, emission_of year)
        """
        co2_emission = []
        for country_id, emission in dictionary.items():
            for key, value in emission_data.country_data.items():
                if value['id'] == country_id:
                    emission = get_country_year_data_megaton(key, year)
                    co2_emission.append((key, emission))
        return co2_emission

    if number == 0:
        number = len(emission_data.country_data)
    if year == "1990":
        co2_emission = every_country_emission_to_list(emission_data.emission_1990)
    elif year == "2005":
        co2_emission = every_country_emission_to_list(emission_data.emission_2005)
    elif year == "2017":
        co2_emission = every_country_emission_to_list(emission_data.emission_2017)
    else:
        raise ValueError("Wrong year!")
    sorted_co2_emission = sorted(co2_emission, key=itemgetter(1), reverse=True)
    for country_name, co2 in sorted_co2_emission[:number]:
        print(f"{country_name}: {co2}")

# Menu choice == "e2"
def emission_per_capita(year, number=0):
    """
    Prints the emission per capita for every country, or the given amount of countries.
    """
    countries_with_population_data = []
    for key, value in emission_data.country_data.items():
        if value['population'] != []:
            countries_with_population_data.append(key)

    def every_country_emission_per_capita_to_list(dictionary, index, countries):
        """
        Creates a list co2_emission where each element is a tuple consisting of
        (country_name, emission_per_capita of year)
        """
        co2_emission_per_capita = []
        for country_id, emission in dictionary.items():
            for key, value in emission_data.country_data.items():
                if key in countries:
                    if value['id'] == country_id:
                        emission = get_country_year_data_megaton(key, year) # get in ton
                        capita = value['population'][index]
                        co2_per_capita = round((emission / capita), 2)
                        co2_emission_per_capita.append((key, co2_per_capita))
        return co2_emission_per_capita

    if number == 0:
        number = len(countries_with_population_data)
    co2_emission_per_capita = []
    if year == "1990":
        index = 0
        co2_emission_per_capita = every_country_emission_per_capita_to_list(
        emission_data.emission_1990, index, countries_with_population_data
)
         # in tuple: emission_data.country_data[country_name]['population'][index]
    elif year == "2005":
        index = 1
        co2_emission_per_capita = every_country_emission_per_capita_to_list(
            emission_data.emission_2005, index, countries_with_population_data
)
    elif year == "2017":
        index = 2
        co2_emission_per_capita = every_country_emission_per_capita_to_list(
            emission_data.emission_2017, index, countries_with_population_data
)
    else:
        raise ValueError("Wrong year!")
    sorted_co2_emission_per_capita = sorted(
        co2_emission_per_capita, key=itemgetter(1), reverse=True
        )
    for country_name, co2_per_capita in sorted_co2_emission_per_capita[:number]:
        print(f"{country_name}: {co2_per_capita}")

# Menu choice == "e3"
def emission_per_area(year, number=0):
    """
    Prints the emission per area for every country, or the given amount of countries.
    """
    countries_with_area_data = []
    for key, value in emission_data.country_data.items():
        if value['area'] != 0:
            countries_with_area_data.append(key)

    def every_country_emission_per_area_to_list(dictionary, countries):
        """
        Creates a list co2_emission where each element is a tuple consisting of
        (country_name, emission_per_are of year)
        """
        co2_emission_per_area = []
        for country_id, emission in dictionary.items():
            for key, value in emission_data.country_data.items():
                if value['id'] == country_id:
                    if key in countries:
                        emission = get_country_year_data_megaton(key, year) # get in ton
                        area = value['area']
                        co2_per_area = round((emission / area), 2)
                        co2_emission_per_area.append((key, co2_per_area))
        return co2_emission_per_area

    if number == 0:
        number = len(countries_with_area_data)
    co2_emission_per_area = []
    if year == "1990":
        co2_emission_per_area = every_country_emission_per_area_to_list(
        emission_data.emission_1990, countries_with_area_data
        )
    elif year == "2005":
        co2_emission_per_area = every_country_emission_per_area_to_list(
            emission_data.emission_2005, countries_with_area_data
        )
    elif year == "2017":
        co2_emission_per_area = every_country_emission_per_area_to_list(
        emission_data.emission_2017, countries_with_area_data
        )
    else:
        raise ValueError("Wrong year!")
    sorted_co2_emission_per_area = sorted(co2_emission_per_area, key=itemgetter(1), reverse=True)
    for country_name, co2_per_area in sorted_co2_emission_per_area[:number]:
        print(f"{country_name}: {co2_per_area}")


if __name__ == "__main__":
    # inp = input("Enter 'year number': ")
    # year, number = inp.split(" ")
    # try:
    #     number = int(number)
    # except ValueError:
    #     print("Number is not a valid number.")
    # emission_per_area(year, number)

    # inp = input("Enter a country: ")
    # data = get_country_data(inp)
    # print_country_data(data)
    pass
