"""
This module contains functions for co2 analysis.
"""

import emission_data

def search_country(search_word):
    """Searches for matching countries based on a search word."""
    matchingList = []
    countryList = list(emission_data.country_data.keys())
    for country in countryList:
        if search_word.lower() in country.lower():
            matchingList.append(country)
    if len(matchingList) == 0:
        raise ValueError
    print("The following countries were found: " + ", ".join(matchingList))
    return matchingList

def get_country_year_data_megaton(country, year):
    """Gets the emissions for a country and year"""
    countryID = emission_data.country_data[country]['id']
    if year == '1990':
        return emission_data.emission_1990[countryID] * 1000000
    if year == '2005':
        return emission_data.emission_2005[countryID] * 1000000
    if year == '2017':
        return emission_data.emission_2017[countryID] * 1000000
    raise ValueError

def get_country_change_for_years(country, year1, year2):
    """Calculates the change for a country between two years"""
    startEmissions = get_country_year_data_megaton(country,year1)
    endEmissions = get_country_year_data_megaton(country,year2)

    difference = endEmissions - startEmissions
    changeInDecimals = difference / startEmissions
    changeInPercentage = changeInDecimals * 100
    return round(changeInPercentage,2)

def get_country_data(country_name):
    """Gets a dictinary with all the data for a country."""
    data = {}
    yearList = ['1990','2005','2017']
    data['name'] = country_name
    i = 0
    for year in yearList:
        emission = get_country_year_data_megaton(country_name, year)
        if emission_data.country_data[country_name]['population'] == []:
            population = None
        else:
            population = emission_data.country_data[country_name]['population'][i] 
        data[year] = {'emission':emission, 'population':population}
        i += 1
    firstSpan = get_country_change_for_years(country_name,'1990','2005')
    secondSpan = get_country_change_for_years(country_name,'2005','2017')
    changeTuple = (firstSpan,secondSpan)
    data['emission_change'] = changeTuple
    return data

def get_and_print_country_data(country_name):
    """Gets and prints data for a country."""
    data = get_country_data(country_name)
    print_country_data(data)
    
def print_country_data(data):
    """Prints a dictinary with all the data for a country."""
    print("Country: " + data["name"])
    years = ['1990','2005','2017']
    print("Emissions:")
    for year in years:
        print(year + ": " + str(data[year]['emission']))
    print("Population:")
    for year in years:
        if data[year]['population'] is None:
            print("Missing population data!")
        else:
            print(year + ": " + str(data[year]['population']))
    print("Emission change:")
    for i in [0,1]:
        print(years[i] + "-" + years[i+1] + ": " + str(data['emission_change'][i]) + "%")

def print_emissions_for_year(year,numberOfCountries = len(emission_data.country_data)):
    """Prints a sorted list of countries' emissions for year."""
    numberOfCountries = int(numberOfCountries)
    emissionDict = {}
    for key, _ in emission_data.country_data.items():
        emissionDict[key] = get_country_year_data_megaton(key,year)
    itemList = list(emissionDict.items())
    sortedList = sorted(itemList, reverse = True, key=lambda x: x[1])
    for i in range(numberOfCountries):
        print(sortedList[i][0] + ": " + str(sortedList[i][1]))

def get_per_capita_for_year(country,year):
    """Gets the per capita emissions for a year and country."""
    emissions = get_country_year_data_megaton(country,year)
    population = get_country_data(country)[year]['population']
    if population is None:
        return 0
    perCapita = emissions/population
    return perCapita

def print_emissions_for_year_per_capita(year,numberOfCountries = len(emission_data.country_data)):
    """Prints the per capita for every country a certain year."""
    numberOfCountries = int(numberOfCountries)
    capitaDict = {}
    for country, _ in emission_data.country_data.items():
        capitaDict[country] = get_per_capita_for_year(country,year)
    itemList = list(capitaDict.items())
    sortedList = sorted(itemList, reverse = True, key=lambda x: x[1])
    for i in range(numberOfCountries):
        print(sortedList[i][0] + ": " + str(round(sortedList[i][1],2)))

def get_per_area_for_year(country,year):
    """Gets the per area emissions for a year and country."""
    emissions = get_country_year_data_megaton(country,year)
    area = emission_data.country_data[country]['area']
    if area == 0:
        return 0
    perArea = emissions/area
    return perArea

def print_emissions_for_year_per_area(year,numberOfCountries = len(emission_data.country_data)):
    """Prints emissions per area for a country a certain year."""
    numberOfCountries = int(numberOfCountries)
    areaDict = {}
    for country, _ in emission_data.country_data.items():
        areaDict[country] = get_per_area_for_year(country,year)
    itemList = list(areaDict.items())
    sortedList = sorted(itemList, reverse = True, key=lambda x: x[1])
    for i in range(numberOfCountries):
        print(sortedList[i][0] + ": " + str(round(sortedList[i][1],2)))
