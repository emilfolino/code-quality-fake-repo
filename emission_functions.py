"""
emission functions
"""

from operator import itemgetter
import emission_data
#import emission_data_small

def search_country(search_word):
    """
    search word
    """
    country_list = []
    for country in emission_data.country_data:
        if search_word.lower() in country.lower():
            country_list.append(country)
    if len(country_list) < 1:
        raise ValueError("Country does not exist!")
    return country_list

def get_country_year_data_megaton(country, year):
    """
    megaton convert
    """
    country_id = emission_data.country_data[country]["id"]
    emission_value = 0.0
    if year == "1990":
        emission_value = float(emission_data.emission_1990[country_id]) * 1000000
    elif year == "2005":
        emission_value = float(emission_data.emission_2005[country_id]) * 1000000
    elif year == "2017":
        emission_value = float(emission_data.emission_2017[country_id]) * 1000000
    else:
        raise ValueError("Wrong year!")
    return emission_value

def get_country_change_for_years(country, year1, year2):
    """
    change year to year
    """
    if year1 and year2 in ("1990","2005","2017"):
        first_year = get_country_year_data_megaton(country,year1)
        second_year = get_country_year_data_megaton(country,year2)
        change_year = round(((second_year / first_year) * 100) - 100,2)
        return change_year
    raise ValueError("Wrong year!")


def get_country_data(country_name):
    """
    country data
    """
    c_data = {}
    c_data["name"] = country_name
    if len(emission_data.country_data[country_name]["population"]) > 0:
        c_data["1990"] = {"emission" : get_country_year_data_megaton(country_name,"1990"), 
        "population" : emission_data.country_data[country_name]["population"][0]}
        c_data["2005"] = {"emission" : get_country_year_data_megaton(country_name,"2005"), 
        "population" : emission_data.country_data[country_name]["population"][1]}
        c_data["2017"] = {"emission" : get_country_year_data_megaton(country_name,"2017"), 
        "population" : emission_data.country_data[country_name]["population"][2]}
    else:
        c_data["1990"] = {"emission" : get_country_year_data_megaton(country_name,"1990"), "population" : None}
        c_data["2005"] = {"emission" : get_country_year_data_megaton(country_name,"2005"), "population" : None}
        c_data["2017"] = {"emission" : get_country_year_data_megaton(country_name,"2017"), "population" : None}
    c_data["emission_change"] = (get_country_change_for_years(country_name,"1990","2005"), 
    get_country_change_for_years(country_name,"2005","2017"))
    return c_data

def print_country_data(data):
    """
    print country data
    """
    print(data["name"])
    print("1990: " + str(data["1990"]["emission"]))
    print("2005: " + str(data["2005"]["emission"]))
    print("2017: " + str(data["2017"]["emission"]))
    if data["1990"]["population"] is None:
        print("Missing population data!")
    else:
        print("1990: " + str(data["1990"]["population"]))
        print("2005: " + str(data["2005"]["population"]))
        print("2017: " + str(data["2017"]["population"]))
    print("1990-2005: " + str(data["emission_change"][0]) + "%")
    print("2005-2017: " + str(data["emission_change"][1]) + "%")

def co2_order(year,amount=None):
    """
    co2 per country
    """
    string_return = ""
    if year == "1990":
        sorted_data = sorted(emission_data.emission_1990.items(), key=itemgetter(1), reverse=True)
    elif year == "2005":
        sorted_data = sorted(emission_data.emission_2005.items(), key=itemgetter(1), reverse=True)
    elif year == "2017":
        sorted_data = sorted(emission_data.emission_2017.items(), key=itemgetter(1), reverse=True)
    else:
        raise ValueError("Not a valid year!")
    if amount is None:
        for value in sorted_data:
            name = get_country_from_id(value[0])
            string_return += (name + ": " + str(get_country_year_data_megaton(name,year)) + "\n")
    else:
        for value in sorted_data[:int(amount)]:
            name = get_country_from_id(value[0])
            string_return += (name + ": " + str(get_country_year_data_megaton(name,year)) + "\n")
    return string_return


def get_country_from_id(id_value):
    """
    get country from id
    """
    country = ""
    for i in emission_data.country_data.items():
        if int(id_value) == i[1]["id"]:
            country = i[0]
    return country

def get_emission_from_id(year,id_):
    """
    get emission from country
    """
    emission = 0.0
    if year == "1990":
        for value in emission_data.emission_1990.items():
            if int(id_) == value[0]:
                emission = value[1]
    elif year == "2005":
        for value in emission_data.emission_2005.items():
            if int(id_) == value[0]:
                emission = value[1]
    elif year == "2017":
        for value in emission_data.emission_2017.items():
            if int(id_) == value[0]:
                emission = value[1]
    return emission

def get_emission_capita(year,amount=None):
    """
    Emission per capita
    """
    ec = ""
    ec_tup = {}

    if amount is None:
        if year == "1990":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec += str(round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["population"][0],2)) + "\n"
        elif year == "2005":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec += str(round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["population"][1],2)) + "\n"
        elif year == "2017":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec += str(round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["population"][2],2)) + "\n"
        else:
            raise ValueError("Not a valid year!")
        #return ec
    else:
        if year == "1990":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec_tup[value[0]] = round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["population"][0],2)
                #ec = value[1]["population"][0] / get_emission_from_id(year,value[1]["id"]) + "\n"
        elif year == "2005":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec_tup[value[0]] = round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["population"][1],2)
                #ec = value[1]["population"][1] / get_emission_from_id(year,value[1]["id"]) + "\n"
        elif year == "2017":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec_tup[value[0]] = round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["population"][2],2)
                #ec += value[1]["population"][2] / get_emission_from_id(year,value[1]["id"]) + "\n"
        else:
            raise ValueError("Not a valid year!")
        ec_tup = sorted(ec_tup.items(), key=itemgetter(1), reverse=True)[:int(amount)]
        for value in ec_tup:
            ec += value[0] + ": " + str(value[1]) + "\n"
    return ec
            #ec += values[0] + ": " + str(round(values[1], 2)) + "\n"

def get_emission_area(year,amount=None):
    """
    Emission area
    """
    ec = ""
    ec_tup = {}

    if amount is None:
        if year == "1990":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec += str(round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["area"],2)) + "\n"
        elif year == "2005":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec += str(round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["area"],2)) + "\n"
        elif year == "2017":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec += str(round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["area"],2)) + "\n"
        else:
            raise ValueError("Not a valid year!")
        #return ec
    else:
        if year == "1990":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec_tup[value[0]] = round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["area"],2)
                #ec = value[1]["population"][0] / get_emission_from_id(year,value[1]["id"]) + "\n"
        elif year == "2005":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec_tup[value[0]] = round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["area"],2)
                #ec = value[1]["population"][1] / get_emission_from_id(year,value[1]["id"]) + "\n"
        elif year == "2017":
            for value in emission_data.country_data.items():
                if len(value[1]["population"]) > 0:
                    ec_tup[value[0]] = round((get_emission_from_id(year,value[1]["id"]) * 1000000) 
                    / value[1]["area"],2)
                #ec += value[1]["population"][2] / get_emission_from_id(year,value[1]["id"]) + "\n"
        else:
            raise ValueError("Not a valid year!")
        ec_tup = sorted(ec_tup.items(), key=itemgetter(1), reverse=True)[:int(amount)]
        for value in ec_tup:
            ec += value[0] + ": " + str(value[1]) + "\n"
    return ec
