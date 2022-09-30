""" Emissionfunctions"""

import emission_data

def GetDictByName(country):
    """Returning Dict of country"""
    for item in emission_data.country_data.items():
        key = item[0]
        if key.lower() in str(country).lower():
            return emission_data.country_data[key]
    return {}
        
def GetIdByName(country):
    """Returning ID of country"""
    for item in emission_data.country_data.items():
        current = item[1]
        if item[0].lower() in str(country).lower():
            return current["id"]
    return -1

def search_country(search_word):
    """ Search for country"""
    matchList = []
    for item in emission_data.country_data:
        if item.lower().__contains__(str(search_word).lower()):
            matchList.append(item)
    if len(matchList) == 0:
        raise ValueError
    return matchList


def get_country_data(countryName):
    """Create country dictionary"""
    newDict = GetDictByName(countryName)

    try:
        popYear1 = newDict['population'][0]
    except IndexError:
        popYear1 = None

    try:
        popYear2 = newDict['population'][1]
    except IndexError:
        popYear2 = None

    try:
        popYear3 = newDict['population'][2]
    except IndexError:
        popYear3 = None

    try:
        firstEmission = get_country_change_for_years(countryName, 1990, 2005)
        secondEmission = get_country_change_for_years(countryName, 2005, 2017)
        returnDict = dict(
            {
                'name': countryName,
                '1990': {'emission': get_country_year_data_megaton(countryName, 1990),
                         'population': popYear1},
                '2005': {'emission': get_country_year_data_megaton(countryName, 2005),
                         'population': popYear2},
                '2017': {'emission': get_country_year_data_megaton(countryName, 2017),
                         'population': popYear3},
                'emission_change': (firstEmission, secondEmission)
            })
    except ValueError:
        return ValueError
    return returnDict


def print_country_data(dataDict):
    """Prints out the data"""
    returnMsg = dataDict["name"] + '\n'
    returnMsg += "Emission\t" + "1990: " + \
        str(dataDict['1990']["emission"]) + '\t'
    returnMsg += "2005: " + str(dataDict['2005']["emission"])+'\t'
    returnMsg += "2017: " + str(dataDict['2017']["emission"]) + '\n'
    returnMsg += "Emission change\t " + "1990-2005: " + \
        str(dataDict['emission_change'][0]) + '%\t'
    returnMsg += "2005-2017: "+str(dataDict['emission_change'][1]) + '%\n'
    returnMsg += "Population\t " + "1990: " + \
        str(dataDict['1990']["population"]) + "\t\t"
    returnMsg += "2005: "+str(dataDict['2005']["population"]) + "\t\t"
    returnMsg += "2017: "+str(dataDict['2017']["population"]) + '\t\n'
    returnMsg += "Missing population data!"
    print(returnMsg)


def get_country_year_data_megaton(country, year):
    """ Get emissions by year"""
    idName = GetIdByName(country)
    if str(year) == "1990":
        return emission_data.emission_1990[idName]*1000000
    if str(year) == "2005":
        return emission_data.emission_2005[idName]*1000000
    if str(year) == "2017":
        return emission_data.emission_2017[idName]*1000000
    raise ValueError


def get_country_change_for_years(country, year1, year2):
    """Get the percentage difference only number"""
    try:
        countryYear1 = get_country_year_data_megaton(country, year1)
        countryYear2 = get_country_year_data_megaton(country, year2)
    except ValueError as arror:
        raise ValueError from arror
    returnValue = ""
    if (countryYear1 > countryYear2):
        returnValue = str("{:.2f}".format(
            (countryYear2-countryYear1)/countryYear1*100))
        if float(returnValue.rstrip('0')) < 0:
            return float(returnValue.rstrip('0'))
        return -float(returnValue.rstrip('0'))

    returnValue = str("{:.2f}".format(
        (countryYear2-countryYear1)/countryYear1*100))
    return float(returnValue.rstrip('0'))


def get_country_change_for_years_str(country, year1, year2):
    """Get country change plus text"""
    try:
        countryYear1 = get_country_year_data_megaton(country, year1)
        countryYear2 = get_country_year_data_megaton(country, year2)
    except ValueError as arror:
        raise ValueError from arror

    returnValue = ""
    if (countryYear1 > countryYear2):
        returnValue = str("{:.2f}".format(
            (countryYear2-countryYear1)/countryYear1*100)).rstrip('0')
        if float(returnValue) < 0:
            return country + ':' + returnValue+ '%'
        return country + ':' + str(-float(returnValue)) + '%'
    returnValue = str("{:.2f}".format(
        (countryYear2-countryYear1)/countryYear1*100)).rstrip('0')
    return country + ':' + returnValue + '%'
