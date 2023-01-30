#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Funktioner för beräkning av utsläpp
"""
#import emission_data_small as em_data
import emission_data as em_data


def search_country(search_word):
    """
    sök efter länder enl inkommande sökord
    """
    country_dict = em_data.country_data.keys()
    result_list = []
    for country in country_dict:
        if search_word.lower() in country.lower():
            result_list.append(country)
    
    # en tom lista returnerar falskt, landet saknas
    if not result_list:
        raise ValueError("Country does not exist!")

    return result_list


def get_country_data(country):
    """
    hämtar data om angivet land
    """
    country_data = em_data.country_data.get(country)
    country_dict = {}

    # namn på landet
    country_dict["name"] = country

    # om antal invånare saknas, används None
    # 'population'-värdet är en tuple
    # om den är tom returnerar if-frågan False
    if country_data["population"]:
        pop_list = country_data["population"]
    else:
        pop_list = (None, None, None)

    # tre årtal, innehåller info om utsläpp och antal invånare
    year_list = ("1990", "2005", "2017")
    for i, year in enumerate(year_list):
        year_dict = {}
        year_dict["emission"] = get_country_year_data_megaton(country, year)
        year_dict["population"] = pop_list[i]
        country_dict[year] = year_dict

    # beräkning av skillnaden i utsläpp mellan åren
    country_dict["emission_change"] = (
        get_country_change_for_years(country, year_list[0], year_list[1]),
        get_country_change_for_years(country, year_list[1], year_list[2])
    )
    return country_dict


def get_country_change_for_years(country, year1, year2):
    """
    beräknar förändring i utsläpp mellan angivna år
    """
    em_year1 = get_country_year_data_megaton(country, year1)
    em_year2 = get_country_year_data_megaton(country, year2)
    em_changes = round((em_year2 - em_year1) / em_year1 * 100, 2)
    return em_changes


def get_country_year_data_megaton(country, year):
    """
    hämtar ett lands utsläpp för angivet år
    """
    country_data = em_data.country_data.get(country)
    country_id = country_data["id"]

    if year == "1990":
        emission = em_data.emission_1990.get(country_id)
    elif year == "2005":
        emission = em_data.emission_2005.get(country_id)
    elif year == "2017":
        emission = em_data.emission_2017.get(country_id)
    else:
        raise ValueError("Wrong year!")
    
    em_megaton = emission * 1000000
    return em_megaton


def print_country_data(country):
    """
    skriver ut all tillgänglig data för angivet land
    """    
    y1, e1, p1, y2, e2, p2, y3, e3, p3, c1, c2 = short_init(country)

    print(country["name"])
    print(f"Emission        - {y1}: {e1}   {y2}: {e2}   {y3}: {e3}")
    print(f"Emission change - {y1}-{y2}: {c1}%   {y2}-{y3}: {c2}%")
    print(f"Population      - {y1}: {p1}   {y2}: {p2}   {y3}: {p3}")


def short_init(country):
    """
    all data från country-dictionary läggs i variabler med
    kortare namn, för att underlätta formatering vid utskrift
    """
    key = tuple(country.keys())

    for i in range(1,4):
        if country[key[i]]["population"] is None: 
            country[key[i]]["population"] = "Missing population data!"

    short_tuple = (
        key[1],
        country[key[1]]["emission"],
        country[key[1]]["population"],
        key[2],
        country[key[2]]["emission"],
        country[key[2]]["population"],
        key[3],
        country[key[3]]["emission"],
        country[key[3]]["population"],
        country[key[4]][0],
        country[key[4]][1]
    )
    return short_tuple


# används vid test av enbart denna modul
# exekveras inte när modulen importeras till annan fil
if __name__ == "__main__":
    try:
        country_dict1 = get_country_data("Turks and Caicos Islands")
        # print(country_dict1)
        # print()
        print_country_data(country_dict1)
        print()
        a = get_country_data("Kyrgyzstan")
        print_country_data(a)
        print()
        country_dict1 = get_country_data("Norway")
        # print()
        print_country_data(country_dict1)

    except ValueError as error_message:
        print(str(error_message))
