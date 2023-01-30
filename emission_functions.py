#!/usr/nin/env python3

"""
Emission functions for the marvin program
"""
from operator import itemgetter
import emission_data


def search_country(search_word):
    """
    Takes a search_word (string) and searches for countries matching
    that string in the emissions data. Throws a ValueError if
    country is not found
    """
    #Make sure search_word is a str
    search_word = str(search_word)

    #Get all countries in country_data (the keys) i a list
    countries = emission_data.country_data.keys()

    #List to store the search results
    results = []

    #Loop through the countries if search_word matches (part of)
    #the country append that country to results
    for country in countries:
        if search_word.lower() in country.lower():
            results.append(country)

    #Raise a ValueError if there is no matching country (results is empty)
    if not results:
        raise ValueError("Country does not exist!")

    #Return the list with the results
    return results

def get_country_year_data_megaton(country, year):
    """
    Gets the emissions in megatons for a certain country and a certain year
    from the emissions data
    """
    #Get the country id
    country_id = get_country_id(country)

    #If the id is None we didn't find a country, raise a ValueError
    if country_id is None:
        raise ValueError("Country does not exist!")

    #Get right "year variable"
    emissions = get_emission_data_for_year(year)

    #If emissions is None we didn't find a variable for that year
    #and we raise a ValueError
    if emissions is None:
        raise ValueError("Wrong year!")

    country_year_data_megaton = emissions[country_id] * 1000000

    return country_year_data_megaton

def get_country_change_for_years(country, year1, year2):
    """
    Takes a country and two years, finds the emissions for
    this country these years (using get_country_year_data_megaton)
    and returns the change in emissions in percantage between the
    years.
    """
    #Use get_country_year_data_megaton() to get the output for each year
    first_year_output = get_country_year_data_megaton(country, year1)

    second_year_output = get_country_year_data_megaton(country, year2)

    #Calculate the change in percent
    change = round(((second_year_output - first_year_output) / first_year_output) * 100, 2)

    #Return change
    return change

def get_country_id(country):
    """
    Returns the country id from the emissions data. Raises an error
    if the country does not exist
    """

    #Initialize country_id to None
    country_id = None

    #Check if the country is in country_data, if so
    #get the id and assign it to country_id
    if country in emission_data.country_data:
        country_id = emission_data.country_data[country]['id']

    #Return country_id
    return country_id


def get_country_data(country_name):
    """
    Takes a string (country_name) and builds a dictionary
    with emissions data about that country
    """
    #The name variable = the argument country_name
    name = country_name

    #Use get_country_year_data_megaton() to get emissions for the different years
    emissions_1990 = get_country_year_data_megaton(country_name, "1990")

    emissions_2005 = get_country_year_data_megaton(country_name, "2005")

    emissions_2017 = get_country_year_data_megaton(country_name, "2017")

    #Use get_population_year() to get population for the different years
    population_1990 = get_population_year(country_name, "1990")
    
    population_2005 = get_population_year(country_name, "2005")

    population_2017 = get_population_year(country_name, "2017")

    #Use get_country_change_for_years() to get the change in emissions between years
    emission_change_1990_2005 = get_country_change_for_years(country_name, "1990", "2005")

    emission_change_2005_2017 = get_country_change_for_years(country_name, "2005", "2017")

    #Build the dict with the above variables
    country_data = {
        'name': name,
        '1990':{'emission':emissions_1990, 'population': population_1990},
        '2005':{'emission':emissions_2005, 'population': population_2005},
        '2017':{'emission':emissions_2017, 'population': population_2017},
        'emission_change': (emission_change_1990_2005, emission_change_2005_2017)
        }
    #Return country_data
    return country_data

def print_country_data(data):
    """
    Prints data about a country
    """
    #The string representing the countries name is at data['name']
    name_string = data['name'] + "\n"

    #Construct a string with emissions data for different years
    #the data for each year is at data[year][emission]
    emission_string = (
        "Emission\t\t\t - "
        "1990: " + str(data['1990']['emission']) + "\t"
        "2005: " + str(data['2005']['emission']) + "\t"
        "2017: " + str(data['2017']['emission']) + "\n"
    )

    #Construct a string with emission changes data for different year-intervalls
    #the data for each interval is at data[emission_change][0] resp. data[emission_change][1]
    emmission_change_string = (
        "Emission change\t\t\t - "
        "1990-2005: " + str(data['emission_change'][0]) + "%" + "\t"
        "2005-2017: " + str(data['emission_change'][1]) + "%" + "\n"
    )

    #The start of the population string
    population_start_string = (
        "Population\t\t\t - "
    )

    #Coonstruct the population string for each year, the data is at data[year][population]
    population_1990_string = "1990: " + str(data['1990']['population']) + "\t"

    population_2005_string = "2005: " + str(data['2005']['population']) + "\t"

    population_2017_string = "2017: " + str(data['2017']['population']) + "\n"

    #If the population data at a certain year is None, replace that with
    #the string 'year: Missing population data!'
    if data['1990']['population'] is None:
        population_1990_string = "1990: Missing population data!\t"
    
    if data['2005']['population'] is None:
        population_2005_string = "2005: Missing population data!\t"

    if data['2017']['population'] is None:
        population_2017_string = "2017: Missing population data!\n"

    #Concatenate and print the strings
    print(
        name_string +
        emission_string +
        emmission_change_string +
        population_start_string +
        population_1990_string +
        population_2005_string +
        population_2017_string
        )

def get_emission_data_for_countries(operation, year, nr_of_countries=None):
    """
    Gets and prints data about countries emissions for a certain year. The parameter
    operation decides which calculation should be made (by output, output/capita or output/area)
    optionally a nr of countries can be be given as argument, then only that number of
    countries will be in the returned list. The countries are sorted on amount of output, largest first
    """

    #Get countries in countries_data (the keys) as a list
    countries = list(emission_data.country_data.keys())

    #Calculate the data by calling the "operation-function" asked for,
    #functions return a list of tuples with data
    if operation == "country":
        data= calculate_emission_per_country(countries, year)
    elif operation == "capita":
        data = caclculate_emission_per_capita(countries, year)
    elif operation == "area":
        data = calculate_emission_divided_by_area(countries, year)
    else:
        raise ValueError(f"Unrecognized operation: {operation} for get_emission_data")

    #Initialize countries_to_get the  to len of the list
    countries_to_get = len(countries)

    #If a nr_of_countries is supplied set countries_to_get
    #to nr_of_countries (if it is an int, otherwise catch ValueError and return None)
    if nr_of_countries is not None:
        try:
            nr_of_countries = int(nr_of_countries)
            countries_to_get = nr_of_countries
        except ValueError:
            print("Nr of countries to display must be an int")
            return None

    #Sort the data using, sorted and itemgetter to sort on the
    #second value in the tuples (the emissions) set reverse to
    #True to get largest output first
    data_sorted = sorted(data, key=itemgetter(1), reverse=True)

    #Slice the data-list to get the number of values(tuples) equal to nr_or_countries
    data_sorted= data_sorted[0:countries_to_get]

    return data_sorted

def print_emission_data(data):
    """"
    Takes a list of tupples with country and emissions data
    and prints it.
    """
    #Print the info in the data list. Country should be at
    #index 0 of each tupple and emissions value at index 1
    for value in data:
        print(value[0] + ": " + str(value[1]) + "\n")

def calculate_emission_per_country(countries, year):
    """
    Takes a list of countries and a year and builds a list with country
    names and outputs in tuples. Returns the list
    """

    countries_by_emissions = []

    #Loop through the countries, call get_country_year_data_megaton
    #with the country and year as argument to get the output in
    #million tons append the country and the emissions
    #as a tupple in the list countries_by_emissons
    for country in countries:
        emission = get_country_year_data_megaton(country, year)
        countries_by_emissions.append((country, emission))

    return countries_by_emissions

def caclculate_emission_per_capita(countries, year):
    """
    Takes a list of countries and a year and builds a list
    with country names and outputs/capita in tuples.
    Returns the list
    """
    emission_per_capita = []

    ##Loop through the countries, call get_population_year
    #with the country and year as arguments to get the population
    #for that year. Call get_country_year_data_megaton with country
    #and year as arguments to get the output in million tons.
    #Then calculate emissions per capita.
    #Population could be None in that case catch TypeError
    #and continue(country will be ignored). Append country and
    #emission to emission_per_capita
    for country in countries:
        population = get_population_year(country, year)
        try:
            emission = round(get_country_year_data_megaton(country, year) / population, 2)
            emission_per_capita.append((country, emission))
        except TypeError:
            continue

    return emission_per_capita

def calculate_emission_divided_by_area(countries, year):
    """
    Takes a list of countries and a year and builds a list
    with country names and outputs/area in tuples.
    Returns the list
    """
    emission_divided_by_area = []

    #Loop through countries call get_country_area
    #with country as argument.Call get_country_year_data_megaton
    #with country and year as arguments to get the output
    #in million tons.
    #Calculate the emission/area, area could be 0 therefore
    #try for and catch ZeroDivisionError, in case of error,
    #continue (thus ignoring the country). Append country and
    #emission to emission_divided_by_area
    for country in countries:
        area = get_country_area(country)
        try:
            emission = round(get_country_year_data_megaton(country, year) / area, 2)
            emission_divided_by_area.append((country, emission))
        except ZeroDivisionError:
            continue

    return emission_divided_by_area

# Below are "helper-functions" used in the above functions
def get_country_info(country_name):
    """
    Returns the country info for a specific country
    from the country data as dictionary
    """
    return emission_data.country_data.get(country_name)

def get_population_year(country_name, year):
    """
    Returns the population of the country for a certain year
    from the country data
    """

    #Initialize year_index used to get population data for the correct
    #year
    year_index = None

    #Set year_index depending on year-parameter
    if year == "1990":
        year_index = 0
    elif year == "2005":
        year_index = 1
    elif year == "2017":
        year_index = 2

    #If year_index is (still) None raise ValueError
    if year_index is None:
        raise ValueError("Wrong year")

    #Get info for the country represented by the country_name_parameter
    #Using function get_country_info(). Country_info is a dict
    country_info = get_country_info(country_name)

    #Use the get-method to get the value at "population"
    #in the dict country_info, returns None if there is no value
    #population_data will be a tuple with values representing
    #the country's population for 1990, 2005 and 2017, or an
    #empty [] if there is no data in emission_data
    population_data = country_info.get("population")

    #If population_data is empty [] or population_data is None
    if not population_data or population_data is None:
        #Set population to None and return population
        population = None
        return population

    #Set population to the value at year_index
    #in the tuple population_data
    population = population_data[year_index]
    return population


def get_id_emissions_as_list(year):
    """
    Gets the emission and id data for a certain year from emission_data. Returns it as
    a list of tupples
    """

    #Fetch the emissions data (a dict) using get_emission_data_for_year(year)
    emissions = get_emission_data_for_year(year)

    #If get_emissions_data returns None there
    #was no data for that year, raise a ValueError
    if emissions is None:
        raise ValueError("Wrong year!")

    #Put the dict items (tupples with id, year) in a list
    emissions = list(emissions.items())

    return emissions

def get_country_by_id(country_id):
    """
    Takes a country id and returns the country associated with that id
    in emissions_data
    """
    #Make sure id is an int else raise ValueError
    if not isinstance(country_id, int):
        raise ValueError("The country id must be an int")

    #Get the country data (dict) from emission_data
    country_data = emission_data.country_data

    #Loop through the dict items in country_data
    #where country is the key and data is the value
    #(a dict) at that key in country_data. Using,
    #dict.get() method to get the value at the key
    # 'id' in the data-dict, if it matches country_id
    # return the country (the key in country_data)
    for country, data in country_data.items():
        if data.get('id') == country_id:
            return country

    #If the country/id wasn't found return None
    return None

def get_country_area(country_name):
    """
    Returns the country area from the emission_data
    """
    #Get the country data (dict) from emission_data
    country_data = emission_data.country_data

    for country, data in country_data.items():
        if country == country_name:
            return data.get('area')

    #If the country wasn't found return None
    return None

def get_emission_data_for_year(year):
    """
    Takes a string representing a year and returns
    the correct variable containing the data for that
    year.
    """
    #Initialize emissions to None
    emissions = None

    #Make sure year is a str
    year = str(year)

    #Check if year matches the year in one of the
    #emission_x variables if so set emissions
    #to that variable
    if year == "1990":
        emissions = emission_data.emission_1990
    elif year == "2005":
        emissions = emission_data.emission_2005
    elif year == "2017":
        emissions = emission_data.emission_2017

    #Return emissions
    return emissions
