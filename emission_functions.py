"""
Functions about emissions for main program
"""
import emission_data

def search_country(search_word):
    """
    A search engine which take input from user and then
     searches the module "emission_data" for countries matching
      input and then returns a list with matching countries
    """
    result_list = []
    for key in emission_data.country_data:
        if search_word.lower() in key.lower():
            result_list.append(key)
    if len(result_list) < 1:
        raise ValueError("Country does not exist!")
    return result_list

def get_country_year_data_megaton(country, year):
    """
    Takes a country and a year as argument and then returns the total emission of that country in that year in tons
    """
    year = int(year)
    for key in emission_data.country_data:
        if country in key:
            country = key
            country_id = emission_data.country_data[country]['id']
            break

    if year == 1990:        
        emissions = emission_data.emission_1990[country_id] * 1000000
    elif year == 2005:      
        emissions = emission_data.emission_2005[country_id] * 1000000
    elif year == 2017:
        emissions = emission_data.emission_2017[country_id] * 1000000
    else:
        raise ValueError("no such year")
    return emissions




def get_country_change_for_years(country, year1, year2):
    """
    Calculates the difference in percentage of emissions between a country in different years
    """
    emission_year1 = get_country_year_data_megaton(country, year1)
    emission_year2 = get_country_year_data_megaton(country, year2)
    diff = (emission_year1 - emission_year2) / emission_year1 * -100
    result = round(diff, 2)
    return result

def get_country_data(country_name):
    """
    Gets argument as country name and searches for all data from emission_data
     and saves them as variabels and return them in a dictionary
    """
    if country_name in emission_data.country_data:
        try:
            pop_90 = emission_data.country_data[country_name]['population'][0]
            pop_05 = emission_data.country_data[country_name]['population'][1]
            pop_17 = emission_data.country_data[country_name]['population'][2]
        except IndexError: 
            pop_90 = None
            pop_05 = None
            pop_17 = None
        
        emission_90 = get_country_year_data_megaton(country_name, "1990")
        emission_05 = get_country_year_data_megaton(country_name, "2005")
        emission_17 = get_country_year_data_megaton(country_name, "2017")

        diff_90 = get_country_change_for_years(country_name,"1990","2005")
        diff_17 = get_country_change_for_years(country_name,"2005","2017")

        my_dict = {
            "name" : country_name,
            "1990" : {"emission" : emission_90, "population" : pop_90},
            "2005" : {"emission" : emission_05, "population" : pop_05},
            "2017" : {"emission" : emission_17, "population" : pop_17},
            "emission_change" : (diff_90, diff_17)
        }
    return my_dict
    


def print_country_data(data):
    """
    Gets an argument as a dictionary and prints out keys and values from dictionary
    """
    print(data['name'])
    print("Emission - 1990:",data['1990']['emission'], 
    "2005:" ,data['2005']['emission'], "2017:",data['2017']['emission'])

    print("Emission change - 1990-2005:", str(data['emission_change'][0]) + "%", 
    "2005-2017:", str(data['emission_change'][1]) + "%")

    if data['1990']['population'] is None:
        print("Missing population data!")
    else:
        print("Population - 1990:",data['1990']['population'], 
        "2005:",data['2005']['population'], "2017:",data['2017']['population'])
