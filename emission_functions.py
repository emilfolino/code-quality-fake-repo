#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Methods for emission calculations """
import emission_data as emDat

countryData = emDat.country_data

def search_country(search_word):
    """Search available keys in data"""

    searchResult = []
    for key in countryData:
        if search_word.lower() in key.lower():
            searchResult.append(key)

    if len(searchResult) == 0:
        raise ValueError

    return searchResult

def get_country_year_data_megaton(country, year):
    """Return emission data for year"""

    countryDataLower = dict((k.lower(), v) for k, v in countryData.items())
    countryLower = country.lower()

    if countryLower not in countryDataLower.keys():
        raise KeyError

    countryIndex = countryDataLower[countryLower]['id']
    if year == "1990":
        emissionData = emDat.emission_1990[countryIndex]
    elif year == "2005":
        emissionData = emDat.emission_2005[countryIndex]
    elif year == "2017":
        emissionData = emDat.emission_2017[countryIndex]
    else:
        raise ValueError("Wrong Year!")

    return emissionData * 1000000

def get_country_change_for_years(country, year1, year2):
    """Get emmission level change in percentage between years"""

    for year in [year1, year2]:
        if year not in ["1990","2005","2017"]:
            raise ValueError("Wrong Year!")

    emission = []
    for year in [year1, year2]:
        try:
            em = get_country_year_data_megaton(country, year)
        except ValueError:
            break
        else:
            emission.append(em)

    percentageChange = round((emission[1]-emission[0]) / emission[0] * 100, 2)

    return percentageChange

def get_country_data(country_name):
    """Get country data"""
    countryDataLower = dict((k.lower(), v) for k, v in countryData.items())
    countryLower = country_name.lower()

    if countryLower not in countryDataLower.keys():
        raise KeyError

    specificCountryData = countryDataLower[countryLower]

    if len(specificCountryData["population"]) == 3:
        [pop1990, pop2005, pop2017] = specificCountryData["population"][0:3]
    else:
        [pop1990, pop2005, pop2017] = (None, None, None)

    emission = []
    change = []
    years = ["1990", "2005", "2017"]
    for i, j in enumerate(years):
        emission.append(get_country_year_data_megaton(country_name, j))

        if i < 2:
            change.append(get_country_change_for_years(country_name, years[i], years[i+1]))

    iniDict = {
            "name": country_name,
            "1990": {"emission": emission[0], "population": pop1990},
            "2005": {"emission": emission[1], "population": pop2005},
            "2017": {"emission": emission[2], "population": pop2017},
            "emission_change": (change[0], change[1])
            }

    return iniDict

def print_country_data(data):
    """Print country data"""
    emis1990 = str(data["1990"]["emission"])
    emis2005 = str(data["2005"]["emission"])
    emis2017 = str(data["2017"]["emission"])
    emisChange90_05 = str(data["emission_change"][0])
    emisChange05_17 = str(data["emission_change"][1])
    pop1990 = str(data["1990"]["population"])
    pop2005 = str(data["2005"]["population"])
    pop2017 = str(data["2017"]["population"])



    textString1 = data["name"] + "\n"
    textString2 = ("Emission" + "\t\t-" + " 1990: " + emis1990 +\
                "\t" + "2005: " + emis2005 + "\t" + "2017: " +  emis2017 + "\n")
    textString3 = ("Emission change" + "\t\t-" + " 1990-2005: " + emisChange90_05 + "%" +\
                   "\t" + "2005-2017: " + emisChange05_17 + "%" + "\n")
    textString4 = ("Population" + "\t\t-" + " 1990: " + pop1990 + "\t" +\
                "\t" + "2005: " + pop2005 + "\t\t" + "2017: " + pop2017 + "\n")


    textString5 = ""
    if data["1990"]["population"] is None:
        textString5 = "\nMissing population data!\n"

    print(textString1 + textString2 + textString3 + textString4 + textString5)
