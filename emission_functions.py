"""
Functions for emission_data
"""

from operator import itemgetter
import emission_data as em_data

def search_country(search_word:str):
    """Search for country"""

    results = []
    for name in em_data.country_data:
        if search_word.lower() in name.lower():
            results.append(name)
    if results == []:
        raise ValueError("Country does not exist!")

    return results

def get_country_year_data_megaton(country, year):
    """Get emissions in megaton for a country and year"""
    id_number = em_data.country_data[country]["id"]

    if year == "1990":
        emission = em_data.emission_1990[id_number]
    elif year == "2005":
        emission = em_data.emission_2005[id_number]
    elif year == "2017":
        emission = em_data.emission_2017[id_number]
    else:
        raise ValueError("Wrong year!")
    return emission * 1000000


def get_country_change_for_years(country, year1, year2):
    """Get emission change between two years"""

    emissions1 = get_country_year_data_megaton(country, year1)
    emissions2 = get_country_year_data_megaton(country, year2)

    # Difference second year to first year, as percentage of first year emissions
    difference = round((((emissions2 - emissions1) / emissions1) * 100), 2)

    return difference

def get_population(country_name, year):
    """Returns population for a country and year"""
    pop = em_data.country_data[country_name]["population"]
    if pop != []:
        # Translate year to first, second or third value
        if (year == "1990"):
            y = 0
        elif (year == "2005"):
            y = 1
        else: # 2017
            y = 2
        return pop[y]
    return None

def get_country_data(country_name):
    """Returns a dict with country data"""
    country_data = {
        "name" : country_name,
        "1990" : {
            "emission" : get_country_year_data_megaton(country_name, "1990"),
            "population" : get_population(country_name, "1990")
            },
        "2005" : {
            "emission" : get_country_year_data_megaton(country_name, "2005"),
            "population" : get_population(country_name, "2005")
            },
        "2017" : {
            "emission" : get_country_year_data_megaton(country_name, "2017"),
            "population" : get_population(country_name, "2017")
            },
        "emission_change" : (
            get_country_change_for_years(country_name, "1990", "2005"),
            get_country_change_for_years(country_name, "2005", "2017"),
            )
        }
    return country_data

def print_country_data(data):
    """Prints country data from a dict"""

    myString:str = (
        data["name"] + "\n"
        "Emission        - "
        "1990: " + str(data["1990"]["emission"]) + ", "
        "2005: " + str(data["2005"]["emission"]) + ", " 
        "2017: " + str(data["2017"]["emission"]) + "\n"
        "Emission change - "
        "1990-2005: " + str(data["emission_change"][0]) + "% "
        "2005-2017: " + str(data["emission_change"][1]) + "%\n"
        "Population      - "
        "1990: " + str(data["1990"]["population"]) + ", "
        "2005: " + str(data["2005"]["population"]) + ", "
        "2017: " + str(data["2017"]["population"])
     )

    myString = myString.replace("None", "Missing population data!")

    print(myString)

def emission_top(year, print_max=None):
    """Prints countries in order of most emissions"""

    # Put values from that year in a list of tuples (country, emissions)
    emission_list = []
    try:
        for country in em_data.country_data:
            # Append tuple (country, emissions)
            emission_list.append((country, get_country_year_data_megaton(country, year)))

        # Sort the list by emissions
        emission_list.sort(key=itemgetter(1), reverse=True)
        
        for em_tuple in emission_list[:print_max]: # Works for both max=None and max=int
            print(em_tuple[0] + ": " + str(em_tuple[1]))
    except ValueError as e:
        print(e)

def emission_top_capita(year, print_max=None):
    """Prints countries in order of most emissions per capita"""
    emission_list = []
    
    try:
        for country in em_data.country_data:
            emission = get_country_year_data_megaton(country, year)
            population = get_population(country, year)

            # Skip countries with no population data
            if population is not None:
                em_per_capita = round((emission / population), 2)
                emission_list.append((country, em_per_capita))

        # Sort the list by emission/capita
        emission_list.sort(key=itemgetter(1), reverse=True)
        
        for em_tuple in emission_list[:print_max]:
            print(em_tuple[0] + ": " + str(em_tuple[1]))
    except ValueError as e:
        print(e)

def emission_top_land(year, print_max=None):
    """Prints countries in order of most emissions per land size"""
    emission_list = []
    
    try:
        for country in em_data.country_data.items():
            emission = get_country_year_data_megaton(country[0], year)
            area = country[1]["area"]

            # In case area is 0, or not defined
            if (area > 0) and (area is not None):
                em_per_size = round((emission / area), 2)

            emission_list.append((country[0], em_per_size))

        # Sort the list by emission/size
        emission_list.sort(key=itemgetter(1), reverse=True)
        
        for em_tuple in emission_list[:print_max]:
            print(em_tuple[0] + ": " + str(em_tuple[1]))
    except ValueError as e:
        print(e)
