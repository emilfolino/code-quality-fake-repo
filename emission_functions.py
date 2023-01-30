"""
Emission functions

    """
import emission_data


def search_country(search_word):
    """
search for country

    """
    country_keys = emission_data.country_data.keys()
    search_results=[]
    #search_word = search_word.lower()
    
    for keys in country_keys:
        lower_keys = keys.lower()
        search_word = search_word.lower()
        if search_word in lower_keys:
            search_results.append(keys)
    if search_results == []:
        raise ValueError('Country does not exist')
    
    
    return search_results

def get_country_year_data_megaton(country,year):
    """
get the country data in megaton

    """
    countries = emission_data.country_data
    
    if "1990" in year:
        year_data = emission_data.emission_1990
    elif "2005" in year:
        year_data = emission_data.emission_2005
    elif "2017" in year:
        year_data = emission_data.emission_2017
    else:
        raise ValueError('Wrong year!')
    country_id = countries[country]['id']
    country_emission = year_data[country_id]
    country_emission = country_emission*1000000
    return country_emission
    #except ValueError:
        #print('Wrong year!')

def get_country_change_for_years(country, year1, year2):
    """
get the emission change for country between years 

    """
    try:
        emission1 = get_country_year_data_megaton(country,year1)
        emission2 = get_country_year_data_megaton(country, year2)
    
        if emission1 < emission2:
            emission_diff = emission2 - emission1
            results = round(emission_diff/emission1*100,2)
        else:
            emission_diff = emission2 - emission1
            results = round(emission_diff/emission1*100,2)
        result = results
    except TypeError:
        result = "Wrong year!"

    return result

def get_country_data(country_name):
    """
get the data of country

    """
    countries = emission_data.country_data

    emission_1990 = get_country_year_data_megaton(country_name,'1990')
    emission_2005 = get_country_year_data_megaton(country_name,'2005')
    emission_2017 = get_country_year_data_megaton(country_name,'2017')

    try:
        population_1990 = countries[country_name]['population'][0]
    except IndexError:
        population_1990 = None
    try:
        population_2005 = countries[country_name]['population'][1]
    except IndexError:
        population_2005 = None
    try:
        population_2017 = countries[country_name]['population'][2]
    except IndexError:
        population_2017 = None

    emission_change1 = get_country_change_for_years(country_name, '1990', '2005')
    emission_change2 = get_country_change_for_years(country_name, '2005', '2017')
    emssion_change = (emission_change1, emission_change2)

    data = {
        'name':country_name,
        '1990': {
            'emission': emission_1990,
            'population': population_1990,
        },
        '2005': {
            'emission': emission_2005,
            'population': population_2005,
        },
        '2017': {
            'emission': emission_2017,
            'population': population_2017,
        },
        'emission_change': emssion_change
                            
        
    }

    return data
    
def print_country_data(data):
    """
print data of country

    """
    emission_1990 = str(data['1990']['emission'])
    emission_2005 = str(data['2005']['emission'])
    emission_2017 = str(data['2017']['emission'])  

    emission_change1 = str(data["emission_change"][0])
    emission_change2 = str(data["emission_change"][1])

    pop_1990 = str(data['1990']['population'])
    pop_2005 = str(data['2005']['population'])
    pop_2017 = str(data['2017']['population'])

    if pop_2017 == "None":
        pop_2017 = "Missing population data!"
    if pop_2005 == "None":
        pop_2005 = "Missing population data!"
    if pop_1990 == "None":
        pop_1990 = "Missing population data!"

    print(data['name'])
    print("Emission\t- " + "1990: " + emission_1990 + "\t"+"2005: " + emission_2005 + "\t"+ "2017: " + emission_2017)
    print("Emission change\t- " + "1990-2005: " + emission_change1 + "%" + "\t" + "2005-2017: " + emission_change2 +"%")
    print("Population\t- " + "1990: "+ pop_1990 + "\t"+ "2005: " + pop_2005 + "\t"+ "2017: " + pop_2017) 
