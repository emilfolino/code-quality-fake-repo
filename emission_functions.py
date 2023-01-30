#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Emission"""

#from operator import itemgetter
#import operator

import emission_data


def search_country(ser_count):
    
    """Docstring"""

    every_count_last = []
    i = 0

    for every_count in emission_data.country_data:
        i += 1
        if ser_count.lower() in every_count.lower():
            every_count_last.append(every_count)
        elif len(every_count_last) < 1 and  i == len(emission_data.country_data):
            raise ValueError(ser_count) 
    return(every_count_last)
       
def get_country_year_data_megaton(country, year):

    """Docstring"""
    all_years = ["1990", "2005", "2017"]

    for count_list in search_country(country):
       
        if year in all_years and country.lower() == count_list.lower():
            if country[0].isupper():
                uppered_country = country
                if "1990" in year:
                    get_count_dict = emission_data.country_data.get(uppered_country)
                    get_id = get_count_dict.get("id")
                    get_megaton_data = emission_data.emission_1990.get(get_id)
                elif "2005" in year:
                    get_count_dict = emission_data.country_data.get(uppered_country)
                    get_id = get_count_dict.get("id")
                    get_megaton_data = emission_data.emission_2005.get(get_id)
                else:
                    get_count_dict = emission_data.country_data.get(uppered_country)
                    get_id = get_count_dict.get("id")
                    get_megaton_data = emission_data.emission_2017.get(get_id)
            else:
                lowered_country = country.lower()
                uppered_country = lowered_country.replace(lowered_country[0], lowered_country[0].upper())
                if "1990" in year:
                    get_count_dict = emission_data.country_data.get(uppered_country)
                    get_id = get_count_dict.get("id")
                    get_megaton_data = emission_data.emission_1990.get(get_id)
                elif "2005" in year:
                    get_count_dict = emission_data.country_data.get(uppered_country)
                    get_id = get_count_dict.get("id")
                    get_megaton_data = emission_data.emission_2005.get(get_id)
                else:
                    get_count_dict = emission_data.country_data.get(uppered_country)
                    get_id = get_count_dict.get("id")
                    get_megaton_data = emission_data.emission_2017.get(get_id)
        else:
            raise ValueError
        return(get_megaton_data * 1000000)

    

def get_country_change_for_years(country, year1, year2):

    """Docstring"""
         
    if year1 != year2:
        change_data1 = get_country_year_data_megaton(country, year1)
        change_data2 = get_country_year_data_megaton(country, year2)
        increase_change_data = change_data2 - change_data1
        last_change_data = (increase_change_data / change_data1) * 100
    else:
        raise ValueError
    return(round(last_change_data, 2))

def get_country_data(country_name):

    """Docstring"""
    country_name = str(country_name)
    c_n = country_name[0]
    if c_n.isupper():
        year_1990_mega = get_country_year_data_megaton(country_name, "1990")
        year_2005_mega = get_country_year_data_megaton(country_name, "2005")
        year_2017_mega = get_country_year_data_megaton(country_name, "2017")
        year_1990_2005 = get_country_change_for_years(country_name, "1990", "2005")
        year_2005_2017 = get_country_change_for_years(country_name, "2005", "2017")
        get_count_dict = emission_data.country_data.get(country_name)
        get_pop = get_count_dict.get("population")
        if len(get_pop) < 1:
            get_pop_1990 = None
            get_pop_2005 = None
            get_pop_2017 = None
            count_data_dict = {"name" : country_name,
            "1990": {"emission" : year_1990_mega,"population" : get_pop_1990},
            "2005": {"emission" : year_2005_mega, "population" : get_pop_2005},
            "2017": {"emission" : year_2017_mega, "population" : get_pop_2017},
            "emission_change" : (year_1990_2005, year_2005_2017)}
        else:
            get_pop_1990 = get_pop[0]
            get_pop_2005 = get_pop[1]
            get_pop_2017 = get_pop[2]
            count_data_dict = {"name" : country_name,
            "1990": {"emission" : year_1990_mega,"population" : get_pop_1990},
            "2005": {"emission" : year_2005_mega, "population" : get_pop_2005},
            "2017": {"emission" : year_2017_mega, "population" : get_pop_2017},
            "emission_change" : (year_1990_2005, year_2005_2017)}
    else:
        lowered_country = country_name.lower()
        uppered_country = lowered_country.replace(lowered_country[0], lowered_country[0].upper())
        year_1990_mega = get_country_year_data_megaton(uppered_country, "1990")
        year_2005_mega = get_country_year_data_megaton(uppered_country, "2005")
        year_2017_mega = get_country_year_data_megaton(uppered_country, "2017")
        year_1990_2005 = get_country_change_for_years(uppered_country, "1990", "2005")
        year_2005_2017 = get_country_change_for_years(uppered_country, "2005", "2017")
        get_count_dict = emission_data.country_data.get(uppered_country)
        get_pop = get_count_dict.get("population")
        if len(get_pop) < 1:
            get_pop_1990 = None
            get_pop_2005 = None
            get_pop_2017 = None
            count_data_dict = {"name" : country_name,
            "1990": {"emission" : year_1990_mega,"population" : get_pop_1990},
            "2005": {"emission" : year_2005_mega, "population" : get_pop_2005},
            "2017": {"emission" : year_2017_mega, "population" : get_pop_2017},
            "emission_change" : (year_1990_2005, year_2005_2017)}
        else:
            get_pop_1990 = get_pop[0]
            get_pop_2005 = get_pop[1]
            get_pop_2017 = get_pop[2]
            count_data_dict = {"name" : country_name,
            "1990": {"emission" : year_1990_mega,"population" : get_pop_1990},
            "2005": {"emission" : year_2005_mega, "population" : get_pop_2005},
            "2017": {"emission" : year_2017_mega, "population" : get_pop_2017},
            "emission_change" : (year_1990_2005, year_2005_2017)}
    return(count_data_dict)

def print_country_data(full_count_data):

    """Docstring"""
    e = "emission"
    p = "population"
    #full_count_data = get_country_data(data)
    fcpc = full_count_data.get("emission_change")
    fcp1 = full_count_data.get("1990")
    fcp2 = full_count_data.get("2005")
    fcp3 = full_count_data.get("2017")
    if fcp1.get("population") is None:
        f_c_p_n = full_count_data.get("name") + "\n"
        f_c_p_e1 = "Emission 1990: " + str(fcp1.get(e)) + " "
        f_c_p_e2 = "2005: " + str(fcp2.get(e)) + " " + "2017: " + str(fcp3.get(e)) + "\n"
        fcpc =  "Emission change " + "1990-2005: " +  str(fcpc[0]) + "% " + "2005-2017: " +  str(fcpc[1]) + "%\n"
        f_c_p_p = "Missing population data!"
        comp_count_print = f_c_p_n + f_c_p_e1 + f_c_p_e2 + fcpc + f_c_p_p
        
    else:
        f_c_p_n = full_count_data.get("name") + "\n"
        f_c_p_e1 = "Emission 1990: " + str(fcp1.get(e)) + " "
        f_c_p_e2 = "2005: " + str(fcp2.get(e)) + " " + "2017: " + str(fcp3.get(e)) + "\n"
        fcpc =  "Emission change " + "1990-2005: " +  str(fcpc[0]) + "% " + "2005-2017: " +  str(fcpc[1]) + "%\n"
        f_c_p_p1 = "Population " + "1990: " + str(fcp1.get(p)) + " " 
        f_c_p_p2 = "2005: " + str(fcp2.get(p)) + " " + "2017: " + str(fcp3.get(p))
        comp_count_print = f_c_p_n + f_c_p_e1 + f_c_p_e2 + fcpc + f_c_p_p1 + f_c_p_p2
    print(comp_count_print)
