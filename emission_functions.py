'''
Emission docstring
'''
import emission_data as e 

def search_country(search_word):
    '''
    docs
    '''


    found_countries = []
    
    for country in e.country_data:
        if search_word.lower() in country.lower():
            found_countries.append(country)
    
    if len(found_countries) == 0:
        print("Country does not exist!")
        raise ValueError
        

    return found_countries
        

def get_country_year_data_megaton(country, year):
    '''
    get country osv
    '''
    
    data = e.country_data[country]

    country_id = data["id"]
    if year == "1990" :
        return e.emission_1990[country_id] *1000000
    if year == "2005" :
        return e.emission_2005[country_id] *1000000
    if year == "2017" :
        return e.emission_2017[country_id] * 1000000
    
    print("Wrong year!")
    raise ValueError
    


def get_country_change_for_years(country, year1, year2):
    '''
    doc
    '''    
    if year1 not in ("1990","2005","2017") or year2 not in ("1990","2005","2017"):
        print("Wrong year!")
        raise ValueError
    
    if country not in e.country_data:
        print("Country does not exist!")
        raise ValueError
        
    
    emission1 = get_country_year_data_megaton(country, year1)
    emission2 = get_country_year_data_megaton(country, year2)

    procentskillnad = (emission2 - emission1) / emission1 * 100 
    resultat = round(procentskillnad, 2)

    return resultat
    
    
def get_country_data(country_name):

    '''
    docs
    '''


    data = {}
    pop_data = e.country_data[country_name]["population"]

    data["name"] = country_name

    if pop_data == []:
        pop_1990 = None
        pop_2005 = None
        pop_2017 = None
    else:
        pop_1990 = pop_data[0]  
        pop_2005 = pop_data[1]  
        pop_2017 = pop_data[2]  

    em1990 = get_country_year_data_megaton(country_name,"1990")
    em2005 = get_country_year_data_megaton(country_name,"2005")
    em2017 = get_country_year_data_megaton(country_name,"2017")

    change1 = get_country_change_for_years(country_name,"1990","2005")
    change2 = get_country_change_for_years(country_name,"2005","2017")

    data["1990"] = {"emission": em1990, "population": pop_1990}
    data["2005"] = {"emission": em2005, "population": pop_2005}
    data["2017"] = {"emission": em2017, "population": pop_2017}
    data["emission_change"] = (change1,change2)

    return data
        

def print_country_data(data):

    '''
    docs
    '''

    print(data["name"])
    print("Emissions:")
    print("1990: " + str(data["1990"]["emission"]))
    print("2005: " + str(data["2005"]["emission"]))
    print("2017: " + str(data["2017"]["emission"]))
    print("Emissions change:")
    print("1990-2005: " + str(data["emission_change"][0]) + "%")
    print("2005-2017: " + str(data["emission_change"][1]) + "%")
    print("Population:")
    if data["1990"]["population"] is not None:
        print("1990: " + str(data["1990"]["population"]))
        print("2005: " + str(data["2005"]["population"]))
        print("2017: " + str(data["2017"]["population"]))
    else:
        print("Missing population data!")
        
