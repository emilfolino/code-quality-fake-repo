"""
emission_functions
"""

import emission_data

def search_country(search_word):
    """
    search_country
    """
    #while True:
    countryList = []
    for key in emission_data.country_data:
        if str(search_word).lower() in key.lower():
            countryList.append(key)

    print(countryList)
    if bool(countryList) is False:
        raise ValueError("Country does not exist!")
    
    print(f"Following countries were found: {countryList}")
    return countryList
    

def get_country_year_data_megaton(country, year):
    """
    get_country_year_data_megaton
    """
    theId = emission_data.country_data[country]["id"] 
    counter = 0

    theYear = ("emission_" + str(year))

    if theYear == "emission_1990":
        counter = 1
        emmisions = emission_data.emission_1990.get(theId)

    elif theYear == "emission_2005":
        counter = 1
        emmisions = emission_data.emission_2005.get(theId)

    elif theYear == "emission_2017":
        counter = 1
        emmisions = emission_data.emission_2017.get(theId)

    print(str(counter) + " im counter")
    if counter == 0:
        raise ValueError()
    return emmisions * 1000000
   

def get_country_change_for_years(country, year1, year2):
    """
    get_country_change_for_years
    """
    try:
        megaton1 = get_country_year_data_megaton(country, year1)
        print(megaton1)
        megaton2 = get_country_year_data_megaton(country, year2)
        print(megaton2)
    except ValueError as something:
        #vill ha en raise from
        raise ValueError from something

    result = round((int(megaton2) / int(megaton1)) - 1,4) *100
    print(f"{country}:{result}%")
    return result
        

def get_country_data(country_name):
    """
    get_country_data
    """
    search_country(country_name)
    year1 = get_country_year_data_megaton(country_name, "1990")
    year2 = get_country_year_data_megaton(country_name, "2005")
    year3 = get_country_year_data_megaton(country_name, "2017")
    pop = emission_data.country_data[country_name]["population"]

    megChange1 = get_country_change_for_years(country_name, "1990", "2005")
    megChange2 = get_country_change_for_years(country_name, "2005", "2017")

    try:
        data = {"name": country_name, 
        "1990": {"emission": year1, "population": pop[0]},
        "2005": {"emission": year2, "population": pop[1]},
        "2017": {"emission": year3, "population": pop[2]},
        "emission_change": (megChange1, round(megChange2,2))}
        print_country_data(data)
    except IndexError:
        data = {"name": country_name, 
        "1990": {"emission": year1, "population": None},
        "2005": {"emission": year2, "population": None},
        "2017": {"emission": year3, "population": None},
        "emission_change": (megChange1, round(megChange2,2))}
        print_country_data(data)

    return data

    

    #print(str(year1) +" "+ str(year2) + " " +str(year3))
    

def print_country_data(data):
    """
    print_country_data
    """
    name = data.get("name",{})
    megton1 = data.get("1990", {}).get("emission")
    megton2 = data.get("2005", {}).get("emission")
    megton3 = data.get("2017", {}).get("emission")
    pop1 = data.get("1990", {}).get("population")
    pop2 = data.get("2005", {}).get("population")
    pop3 = data.get("2017", {}).get("population")
    change = data.get("emission_change", {})#.get(megChange1)
    #change2 = data.get("emission_change", {})#.get(megChange2)

    #print(f"POTATIS1990-2005: {change[0]}%")

    print(name)
    print(f"1990: {megton1}")
    print(f"2005: {megton2}")
    print(f"2017: {megton3}")

    if pop1 is None:
        print("1990: Missing population data!")
        print("2005: Missing population data!")
        print("2017: Missing population data!")
        print(f"1990-2005: {change[0]}%")
        print(f"2005-2017: {change[1]}%")
    else:
        print(f"1990: {pop1}")
        print(f"2005: {pop2}")
        print(f"2017: {pop3}")
        print(f"1990-2005: {change[0]}%")
        print(f"2005-2017: {change[1]}%")
  