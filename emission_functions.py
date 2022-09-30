"""
All functions that handle every tasks about emission
"""

import emission_data as emiDATA

def search_country(search_word):
    """
    Search for search_word in countries name from country_data
    """
    search_word = search_word.lower()
    findedNames = []
    for country in emiDATA.country_data:
        nameLowerCase = country.lower()
        if nameLowerCase == search_word:
            findedNames.append(country)
        else:
            if search_word in nameLowerCase:
                findedNames.append(country)
    
    if len(findedNames) == 0:
        raise ValueError
    
    return findedNames

def getEmissionByCountrysID(id_, year):
    """
    find the countrys emission in a specific year by id
    """
    result = None
    if year == '1990':
        result = emiDATA.emission_1990[id_]
    elif year == '2005':
        result = emiDATA.emission_2005[id_]
    elif year == '2017':
        result = emiDATA.emission_2017[id_]
    return result


def get_country_year_data_megaton(inputedCountry, year):
    """
    get how much emissions a country made in a specific year.
    """ 
    validYears = ['1990','2005','2017']
    if year in validYears:
        id_ = getCountrysID(inputedCountry)
        result = getEmissionByCountrysID(id_, year)
        return result * 1000000
    raise ValueError

def get_country_change_for_years(country, year1, year2):
    """
    calculate and return the difference for a country's emissions between two years
    """
    emissionAtYear1 = get_country_year_data_megaton(country, year1) 
    emissionAtYear2 = get_country_year_data_megaton(country, year2) 
    percentageEmissionDifference = (1 - ( emissionAtYear2 / emissionAtYear1 ) ) * 100
    percentageEmissionDifference = round(percentageEmissionDifference,2)
    if percentageEmissionDifference < 0:
        return -percentageEmissionDifference
    return -percentageEmissionDifference        


def print_country_data(data):
    """
    print given data i en nicer format
    """
    years = ['1990','2005','2017']
    for year in years:
        if not data[year]['population']:
            data[year]['population'] = 'Missing population data!'

    stringToBePrint = f"""
        {data['name']}
        Emissions         - 1990: {data['1990']['emission']}\t 2005: {data['2005']['emission']}\t 2017: {data['2017']['emission']}
        Emission change   - 1990-2005: {data['emission_change'][0]}%\t 2005-2017: {data['emission_change'][1]}%
        Population        - 1990: {data['1990']['population']}\t 2005: {data['2005']['population']}\t 2017: {data['2017']['population']}
    """
    print(stringToBePrint)


def get_country_data(country_name):
    """
    Get and print data for a country
    """
    for country in emiDATA.country_data:
        if country.lower() == country_name.lower():
            country_name = country
            
    years = ['1990','2005','2017']
    result = {
        'name':country_name,
        '1990':{'emission': 0, 'population': None},
        '2005':{'emission': 0, 'population': None},
        '2017':{'emission': 0, 'population': None},
        'emission_change':(),
    }
    population = emiDATA.country_data[country_name]['population']
    try:
        for index,year in enumerate(years):
            result[year]['emission'] = get_country_year_data_megaton(country_name, year)
            if population:
                result[year]['population'] = population[index]  
            else:
                result[year]['population'] = None
        difference_1990_2005 = get_country_change_for_years(country_name, '1990', '2005')
        difference_2005_2017 = get_country_change_for_years(country_name, '2005', '2017')
        result['emission_change'] = (difference_1990_2005,difference_2005_2017)
    except ValueError:
        print("Couldn't find the country!")
    
    return result


def getCountrysID(countryName):
    """
    Get and return the countrys ID
    """
    id_= -1
    countries = emiDATA.country_data.keys()
    for country in countries:
        if country.lower() == countryName.lower():
            id_ = emiDATA.country_data[country]['id']
    return id_
