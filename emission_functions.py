"""
functions for handeling data from emissions
"""

import emission_data
CountryDataSet = {}
emissions90 = {}
emissions05 = {}
emissions17 = {}
def search_country(search_word):
    """
    Searches the dataset for a country
    """
    Matches = []
    for key in CountryDataSet:
        if search_word.lower() in key.lower():
            Matches.append(key)
    if(len(Matches) == 0):
        raise ValueError
    print(Matches)
    return Matches

def get_country_change_for_years(country, year1, year2):
    """
    Gets change in emissions over time for a country
    """
    try:
        y1data = get_country_year_data_megaton(country, year1)
        y2data = get_country_year_data_megaton(country, year2)
        diff = round(y2data/y1data*100 - 100, 2)
        return diff
    except ValueError as e:
        print("Wrong year!")
        raise ValueError from e

def get_country_year_data_megaton(country, year):
    """
    Gets emissions data for a country and year in the dataset
    """
    CountryDetails = CountryDataSet.get(country)
    idnum = CountryDetails.get("id")
    if(year == "1990"):
        return emissions90.get(idnum)*1000000
    if(year == "2005"):
        return emissions05.get(idnum)*1000000
    if(year == "2017"):
        return emissions17.get(idnum)*1000000
    raise ValueError

def get_country_data(country_name):
    """
    Prints out all known data about a country from the datasets
    """
    data = {}
    data["name"] = country_name
    CountryDetails = CountryDataSet.get(country_name)
    if(len(CountryDetails.get("population")) != 0):
        data["1990"] = {"emission": get_country_year_data_megaton(country_name, "1990"),
         "population": CountryDetails.get("population")[0]}
        data["2005"] = {"emission": get_country_year_data_megaton(country_name, "2005"),
         "population": CountryDetails.get("population")[1]}
        data["2017"] = {"emission": get_country_year_data_megaton(country_name, "2017"),
         "population": CountryDetails.get("population")[2]}
    else:
        data["1990"] = {"emission": get_country_year_data_megaton(country_name, "1990"),
         "population": None}
        data["2005"] = {"emission": get_country_year_data_megaton(country_name, "2005"),
         "population": None}
        data["2017"] = {"emission": get_country_year_data_megaton(country_name, "2017"),
         "population": None}

    data["emission_change"] = (get_country_change_for_years(country_name, "1990", "2005"),
     get_country_change_for_years(country_name, "2005", "2017"))
    return data

def print_country_data(data):
    """
    Prints the datastructure from get_country_data
    """
    print(data["name"])
    print(f"Emission 1990: {data['1990']['emission']} 2005: "
    f"{data['2005']['emission']} 2017: {data['2017']['emission']}")
    print(f"Emission change 1990-2005: {data['emission_change'][0]}%"
    f" 2005-2017: {data['emission_change'][1]}%")
    if(data['1990']['population'] is not None):
        print(f"Population 1990: {data['1990']['population']}"
        f" 2005: {data['2005']['population']} 2017: {data['2017']['population']}")
    else:
        print("Missing population data!")

def sorted_emissions(Year, Max = -1):
    """
    Prints a sorted list of emissions
    """
    Data = {}
    for Country in CountryDataSet:
        Data[Country] = get_country_year_data_megaton(Country, Year)
    SortedData = sorted(Data.items(), key= lambda x: x[1], reverse=True)
    if(int(Max) > 0):
        for i in range(0,int(Max)):
            print(f"{SortedData[i][0]}: {SortedData[i][1]}")
    else:
        for i in enumerate(len(SortedData)):
            print(f"{SortedData[i][0]}: {SortedData[i][1]}")
        
def sorted_emissions_per_capita(Year, Max = -1):
    """    
    Prints a sorted list of emissions per capita
    """
    Data = {}
    for Country in CountryDataSet:
        try:
            CountryData = CountryDataSet.get(Country)
            if(Year == "1990"):
                population = CountryData['population'][0]
            elif(Year == "2005"):
                population = CountryData['population'][1]
            elif(Year == "2017"):
                population = CountryData['population'][2]
            Data[Country] = round(int(get_country_year_data_megaton(Country, Year))/population,2)
        except IndexError:
            pass
    SortedData = sorted(Data.items(), key= lambda x: x[1], reverse=True)
    if(int(Max) > 0):
        for i in range(0,int(Max)):
            print(f"{SortedData[i][0]}: {SortedData[i][1]}")
    else:
        for i in enumerate(len(SortedData)):
            print(f"{SortedData[i][0]}: {SortedData[i][1]}")

def sorted_emissions_per_area(Year, Max = -1):
    """
    Prints a sorted list of emissions per area
    """
    Data = {}
    for Country in CountryDataSet:
        try:
            CountryData = CountryDataSet.get(Country)
            if(Year == "1990"):
                area = CountryData['area']
            elif(Year == "2005"):
                area = CountryData['area']
            elif(Year == "2017"):
                area = CountryData['area']
            Data[Country] = round(int(get_country_year_data_megaton(Country, Year))/area,2)
        except (IndexError, ZeroDivisionError):
            pass
    SortedData = sorted(Data.items(), key= lambda x: x[1], reverse=True)
    if(int(Max) > 0):
        for i in range(0,int(Max)):
            print(f"{SortedData[i][0]}: {SortedData[i][1]}")
    else:
        for i in enumerate(len(SortedData)):
            print(f"{SortedData[i][0]}: {SortedData[i][1]}")

CountryDataSet = emission_data.country_data
emissions90 = emission_data.emission_1990
emissions05 = emission_data.emission_2005
emissions17 = emission_data.emission_2017
