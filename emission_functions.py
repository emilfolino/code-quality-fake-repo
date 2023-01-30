"""
Emission_fun
"""
import emission_data

def search_country(search_word):
    """
    search_country
    """
    Con = []
    for key in emission_data.country_data:
        if search_word.upper() in key.upper():
            Con.append(key)
    if "".join(Con) == "":
        raise ValueError("Country does not exist!")
    return Con

def get_country_year_data_megaton(country, year):
    """
    get_country_year_data_megaton
    """
    if year not in ("1990","2005","2017"):
        raise ValueError("Wrong year!")  
    yearAfter = 0 
    val = emission_data.country_data.get(country).get('id')
    if year == "2017":
        yearAfter = emission_data.emission_2017.get(val) * 1000000
    elif year == "2005":
        yearAfter = emission_data.emission_2005.get(val) * 1000000
    elif year == "1990":
        yearAfter = emission_data.emission_1990.get(val) * 1000000
    return yearAfter


def get_country_change_for_years(country, year1, year2):
    """
    get_country_change_for_years
    """
    firstYear = get_country_year_data_megaton(country,year1)
    secondYear = get_country_year_data_megaton(country,year2)
    firstNum =  float(secondYear) - float(firstYear)
    secondNum = (firstNum / float(firstYear)) * 100
    return round(secondNum,2)
   

def get_country_data(country_name):
    """
    get_country_data
    """
    pop = emission_data.country_data.get(country_name).get('population')
    popStr = list(pop)
    conData = {}
    if len(popStr) == 3:
        emission_1990 = get_country_year_data_megaton(country_name,'1990')
        emission_2005 = get_country_year_data_megaton(country_name,'2005')
        emission_2017 = get_country_year_data_megaton(country_name,'2017')
        emChange_1990_2005 = get_country_change_for_years(country_name,"1990","2005")
        emChange_2005_2017 = get_country_change_for_years(country_name,"2005","2017")
        conData = {
                 'name': country_name,
                 '1990': {'emission': emission_1990 , 'population': popStr[0]},
                 '2005': {'emission': emission_2005  , 'population': popStr[1]},
                 '2017': {'emission': emission_2017  , 'population': popStr[2]},
                 'emission_change': (emChange_1990_2005, emChange_2005_2017)
                   }
        print_country_data(conData)
    elif len(popStr) == 2:
        emission_1990 = get_country_year_data_megaton(country_name,'1990')
        emission_2005 = get_country_year_data_megaton(country_name,'2005')
        emission_2017 = get_country_year_data_megaton(country_name,'2017')
        emChange_1990_2005 = get_country_change_for_years(country_name,"1990","2005")
        emChange_2005_2017 = get_country_change_for_years(country_name,"2005","2017")
        conData = {
                 'name': country_name,
                 '1990': {'emission': emission_1990 , 'population': popStr[0]},
                 '2005': {'emission': emission_2005  , 'population': popStr[1]},
                 '2017': {'emission': emission_2017  , 'population': None},
                 'emission_change': (emChange_1990_2005, emChange_2005_2017)
                   }
        print_country_data(conData)
    elif len(popStr) == 1:
        emission_1990 = get_country_year_data_megaton(country_name,'1990')
        emission_2005 = get_country_year_data_megaton(country_name,'2005')
        emission_2017 = get_country_year_data_megaton(country_name,'2017')
        emChange_1990_2005 = get_country_change_for_years(country_name,"1990","2005")
        emChange_2005_2017 = get_country_change_for_years(country_name,"2005","2017")
        conData = {
                 'name': country_name,
                 '1990': {'emission': emission_1990 , 'population': popStr[0]},
                 '2005': {'emission': emission_2005  , 'population': None},
                 '2017': {'emission': emission_2017  , 'population': None},
                 'emission_change': (emChange_1990_2005, emChange_2005_2017)
                   }
        print_country_data(conData)
    else:
        emission_1990 = get_country_year_data_megaton(country_name,'1990')
        emission_2005 = get_country_year_data_megaton(country_name,'2005')
        emission_2017 = get_country_year_data_megaton(country_name,'2017')
        emChange_1990_2005 = get_country_change_for_years(country_name,"1990","2005")
        emChange_2005_2017 = get_country_change_for_years(country_name,"2005","2017")
        conData = {
                  'name': country_name,
                  '1990': {'emission': emission_1990 , 'population': None},
                  '2005': {'emission': emission_2005  , 'population': None},
                  '2017': {'emission': emission_2017  , 'population': None},
                  'emission_change': (emChange_1990_2005, emChange_2005_2017)
                    }
        print_country_data(conData)
    
    return conData

def print_country_data(data):
    """
    print_country_data
    """
    if (data["1990"]["population"] and data["2005"]["population"] and data["2017"]["population"]) is None:
        print("Missing population data!")
    countryName = f'{data["name"]}\n'
    emissions = f'Emission  - 1990: {data["1990"]["emission"]}   2005:'\
    f' {data["2005"]["emission"]}  2017: {data["2017"]["emission"]}\n'
    emChange = f'Emission change  - 1990-2005: {data["emission_change"][0]}%  '\
    f'        2005-2017: {data["emission_change"][1]}%\n'
    popShow = f'Population - 1990: {data["1990"]["population"]}      '\
    f' 2005: {data["2005"]["population"]}    2017: {data["2017"]["population"]}'
    print(countryName, emissions, emChange, popShow)
    