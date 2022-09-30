"""
Functions To Emissions
"""
import emission_data

def search_country(search_word):
    """
    Search Country By Word
    """
    Listan = []
    
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            Listan.append(key) 

    if not Listan:
        raise ValueError()
   
    return Listan


def get_country_year_data_megaton(country, year):
    """
    Get Data From Country
    """

    year = int(year)
    CountryID = emission_data.country_data[country]['id']
    OneMill = 1000000
    if year == 1990:
        return emission_data.emission_1990[CountryID] * OneMill
    if year == 2005:
        return emission_data.emission_2005[CountryID] * OneMill
    if year == 2017:
        return emission_data.emission_2017[CountryID] * OneMill

    raise ValueError()

def get_country_change_for_years(country, year1, year2):
    """
    Get Country Changes By Year
    """
    EMYear1 = get_country_year_data_megaton(country, year1)
    EMYear2 = get_country_year_data_megaton(country, year2)
    PercentChange = round((EMYear2 / EMYear1 - 1) * 100, 2)
    return (PercentChange)

def get_country_data(country_name):
    """
    Get Country Data Population
    From Each Year
    """

    #Fetch Information From EmissionData And Place In Veriales

    try:
        Population1990 = emission_data.country_data[country_name]["population"] [0]
    except IndexError:
        Population1990 = None

    try:
        Population2005 = emission_data.country_data[country_name]["population"] [1]
    except IndexError:
        Population2005 = None

    try:
        Population2017 = emission_data.country_data[country_name]["population"] [2]
    except IndexError:
        Population2017 = None


    #Create and add The Information Inside The Dictionary DataValue
    DataValue = {

        "name" : country_name,
        "1990" : {"emission" : + get_country_year_data_megaton(country_name, "1990"), "population" : Population1990},
        "2005" : {"emission" : + get_country_year_data_megaton(country_name, "2005"), "population" : Population2005},
        "2017" : {"emission" : + get_country_year_data_megaton(country_name, "2017"), "population" : Population2017},
        "emission_change" : (get_country_change_for_years(country_name, "1990", "2005") 
        , get_country_change_for_years(country_name, "2005", "2017"))
 }
    return DataValue



def print_country_data(data):
    """
    Print Out Data From Country
    """

    #Check If There Is No Data, If So Print Missing Population
    if  (data["1990"]["population"] is None):
        data["1990"]["population"] = "Missing population data!"
    
    if  (data["2005"]["population"] is None):
        data["2005"]["population"] = "Missing population data!"
    
    if  (data["2017"]["population"] is None):
        data["2017"]["population"] = "Missing population data!"

        
    #Print All Gathered Information.. Funkade inte med fstring här, vrf?
    print(data["name"])
    print("1990: " + str(data["1990"]["emission"]) + "2005: " + 
    str(data["2005"]["emission"]) + "2017: " + str(data["2017"]["emission"]))
    print("1990: " + str(data["1990"]["population"]) + "2005: " + 
    str(data["2005"]["population"]) + "2017: " + str(data["2017"]["population"]))
    print("1990-2005: " + str(data["emission_change"][0]) + "% " + 
    "2005-2017: " + str(data["emission_change"][1]) + "%")
    