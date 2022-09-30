"""
emission functions to main.py
"""
import emission_data as data

def search_country(search_word):
    """
    search for country
    """
    result = []
    answer =""
    for key in list(data.country_data.keys()):
        if search_word.lower() in key.lower():
            result.append(key)
    if len(result) == 0:    
        raise ValueError("Country does not exist!")
    
    for plase in result:
        answer += plase + ", "
    answer = answer[:-2]
    print("Following countries were found:", answer)
    return result

def get_country_year_data_megaton(country, year):
    """
    get country year data megaton
    """
    c_data = data.country_data
    key = c_data[country]["id"]
    em_2017 = data.emission_2017
    em_2005 = data.emission_2005
    em_1990 = data.emission_1990
    million = 1000000
    if int(year) == 2017:
        result = em_2017[key] * million
    elif int(year) == 2005:
        result = em_2005[key] * million
    elif int(year) == 1990:
        result = em_1990[key] * million
    else:
        raise ValueError("Wrong year!")
    return result

def get_country_change_for_years(country, year1, year2):
    """
    get country change for years
    """
    answer_year1 = get_country_year_data_megaton(country, year1)
    answer_year2 = get_country_year_data_megaton(country, year2)
    result = -(1 -(int(answer_year2) / int(answer_year1))) *100
    result = round(result, 2)
    if year1 in ('1990', '2005', '2017'):
        print(f"Utsläppen har minskat med {result}% från {year1} till {year2}")
        answer = f"{country}:{result}%"
        print(answer)
    
    return result

def get_country_data(country_name):
    """
    get country data
    """
    save_data = {}
    save_data["name"] = {}
    save_data["1990"] = {}
    save_data["2005"] = {}
    save_data["2017"] = {}
    save_data["emission_change"] = {}

    save_data["name"] = country_name
    save_data["1990"]["emission"] = get_country_year_data_megaton(country_name, 1990)
    save_data["2005"]["emission"] = get_country_year_data_megaton(country_name, 2005)
    save_data["2017"]["emission"] = get_country_year_data_megaton(country_name, 2017)
    
    c_data = data.country_data
    population = c_data[country_name]["population"]
    if len(population) != 0:
        po_2017 = population[2]
        po_2005 = population[1]
        po_1990 = population[0]
        save_data["1990"]["population"] = po_1990
        save_data["2005"]["population"] = po_2005
        save_data["2017"]["population"] = po_2017
    else:
        save_data["1990"]["population"] = None
        save_data["2005"]["population"] = None
        save_data["2017"]["population"] = None

    data1 = get_country_change_for_years(country_name, 1990, 2005)
    data2 = get_country_change_for_years(country_name, 2005, 2017)
    save_data["emission_change"] = (data1, data2)
    print(save_data)
    return save_data    

def print_country_data(Data):
    """
    print country Data
    """
    re_em1 = Data["1990"]["emission"]
    re_em2 = Data["2005"]["emission"]
    re_em3 = Data["2017"]["emission"]

    em_change1 = Data["emission_change"][0]
    em_change2 = Data["emission_change"][1]

    population1 = Data["1990"]["population"]
    population2 = Data["2005"]["population"] 
    population3 = Data["2017"]["population"]
    print(*Data["name"])
    print("Emission          - ", f"1990: {re_em1}    ", f"2005: {re_em2}    ", f"2017: {re_em3}" )
    print("Emission change   - ", f"1990-2005: {em_change1}%    ", f"2005-2017: {em_change2}%")

    if Data["1990"]["population"] is not None:
        population1 = Data["1990"]["population"]
        population2 = Data["2005"]["population"] 
        population3 = Data["2017"]["population"]
        print("Population        - ", f"1990: {population1}    ", f"2005: {population2}    ", f"2017: {population3}")
    else:
        print(Data["name"], "      - Missing population data!")
    