"""funktionerna som har med utsläppen att göra"""

import emission_data as ED

def search_country(search_word):
    """Titta om sökordet finns bland länderna"""
    countries = []

    for key in ED.country_data:
        if search_word.lower() in key.lower():
            countries.append(key)
    
    if len(countries) == 0:
        raise ValueError("Country not found")

    return countries
   

def get_country_year_data_megaton(country, year):
    """Ta fram utsläppen för landet ett visst år"""
    country_id = ED.country_data[country]["id"]
    if year == "2017":
        emission = ED.emission_2017.get(country_id)
    elif year == "2005":
        emission = ED.emission_2005.get(country_id)
    elif year == "1990":
        emission = ED.emission_1990.get(country_id)
    else:
        raise ValueError
    emission *= 1000000
    return emission


def get_country_change_for_years(country, year1, year2):
    """Räkna ut föränding i utsläpp mellan 2 år"""
    em_year1 = get_country_year_data_megaton(country, year1)
    em_year2 = get_country_year_data_megaton(country, year2)
    if (em_year2 / em_year1) < 0:
        diff = round((em_year2 / em_year1)*100, 2)
    else:
        diff = round((em_year2 / em_year1)*100-100, 2)
    
    return diff
 

def pop(country_name, index):
    """Funktion för att ta ut populationen. Saknas data blir värdet None"""
    try:
        population = ED.country_data[country_name]["population"][index]
    except IndexError:
        population = None
    return population


def get_country_data(country_name):
    """Funktion för att samla ihop information om population, utsläpp och förändring"""
    #1990
    em_1990 = get_country_year_data_megaton(country_name, "1990")
    pop_1990 = pop(country_name, 0) 
    data_1990 = {"emission" : em_1990, "population" : pop_1990}   

    # 2005
    em_2005 = get_country_year_data_megaton(country_name, "2005")
    pop_2005 = pop(country_name, 1) 
    data_2005 = {"emission" : em_2005, "population" : pop_2005}

    # 2017
    em_2017 = get_country_year_data_megaton(country_name, "2017") 
    pop_2017 = pop(country_name, 2) 
    data_2017 = {"emission" : em_2017, "population" : pop_2017}
    
    # change in emission
    change1 = get_country_change_for_years(country_name, "1990", "2005")
    change2 = get_country_change_for_years(country_name, "2005", "2017")
    changes = (change1, change2)

    country_data = {
        "name" : country_name,
        "1990" : data_1990,
        "2005" : data_2005,
        "2017" : data_2017,
        "emission_change" : changes
    }
    return country_data


def print_country_data(data):
    """Funktion för att skriva ut datan"""
    if data["1990"]["population"] is None:
        data["1990"]["population"]= "Missing population data!"
        data["2005"]["population"]= "Missing population data!"
        data["2017"]["population"]= "Missing population data!"
    print(
        data["name"] + "\n" + 
        "Emmision: "+
        "1990: " + str(data["1990"]["emission"]) + "   "+
        "2005: " + str(data["2005"]["emission"]) +"   "+
        "2017: " + str(data["2017"]["emission"]) + "\n"+ 
        "Population: ", 
        "1990: " + str(data["1990"]["population"]) + "   "+
        "2005: " + str(data["2005"]["population"]) + "   "+
        "2017: " + str(data["2017"]["population"]) + "\n"+
        "Emission change: "
        "1990-2005: " + str(data["emission_change"][0]) + "%   "+
        "2005-2017: " + str(data["emission_change"][1]) + "%"
        )


def id_to_country_dict():
    """All countries in a dict, id as key"""
    countries = {}
    for country, data in ED.country_data.items():
        my_id = data["id"]
        countries[my_id] = country
    return countries


def decending_emission_list(year):
    """A decending list of all emission per country"""
    if year == "1990":
        all_emissions = sorted( [(em,country) for country, em in ED.emission_1990.items()], reverse=True)
    elif year == "2005":
        all_emissions = sorted( [(em,country) for country, em in ED.emission_2005.items()], reverse=True)
    elif year == "2017":
        all_emissions = sorted( [(em,country) for country, em in ED.emission_2017.items()], reverse=True)
    else:
        print("Wrong year!")
    return all_emissions


def top_emission(year,no=1):
    """Länder med störst utsläpp"""  
    all_emissions = decending_emission_list(year)
    countries = id_to_country_dict()

    top_countries = []
    for key in range(no):
        emission = round(all_emissions[key][0]*1000000,2)
        the_id = all_emissions[key][1]
        the_country = countries[the_id]
        top_countries.append((the_country, emission))
        
    for i,_ in enumerate(top_countries):
        land = top_countries[i][0]
        utslapp = str(top_countries[i][1])
        print(land + ": " + utslapp)


def year_index(year):
    """Turns the year into an index"""
    if year == "1990":
        index = 0
    elif year == "2005":
        index = 1
    elif year == "2017":
        index = 2
    else:
        print("Wrong year!")
    return index


def emission_per_capita(year, no=-1):
    """Länder med högst utsläpp per capita"""
    
    all_emissions = decending_emission_list(year)
    countries = id_to_country_dict()
    index = year_index(year)

    em_per_ca_list = []
    for key, _ in enumerate(all_emissions):
        emission = all_emissions[key][0]*1000000
        the_id = all_emissions[key][1]
        country_name = countries[the_id]
        population = pop(country_name, index)
        if population is None:
            continue
        em_p_ca = round((emission / population),2)
        em_per_ca_list.append((em_p_ca, country_name))
    
    em_per_ca_list.sort(reverse=True)
    
    #Längden på listan av länder som har pop-data
    if no == -1:
        no = len(em_per_ca_list)

    for i in range(no):
        land = em_per_ca_list[i][1]
        utslapp_per_ca = str(em_per_ca_list[i][0])
        print(land + ": " + utslapp_per_ca)
    

def emission_per_area(year, no=-1):
    """Länder med högst utsläpp per capita"""
    
    all_emissions = decending_emission_list(year)
    countries = id_to_country_dict()

    em_per_area_list = []
    for key, _ in enumerate(all_emissions):
        emission = all_emissions[key][0]*1000000
        the_id = all_emissions[key][1]
        country_name = countries[the_id]
        area = ED.country_data[country_name]["area"]
        if area == 0:
            continue
        em_p_ca = round((emission / area),2)
        em_per_area_list.append((em_p_ca, country_name))
    
    em_per_area_list.sort(reverse=True)
    
    #Längden på listan med länder som har area
    if no == -1:
        no = len(em_per_area_list)

    for i in range(no):
        land = em_per_area_list[i][1]
        utslapp_per_ca = str(em_per_area_list[i][0])
        print(land + ": " + utslapp_per_ca)

if __name__ == "__main__":
    id_to_country_dict()
    
