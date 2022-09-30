"""
For emissions function
"""
import emission_data
def search_country(search_word):
    "Search for country and find in list"
    schword = search_word
    dataout = []
    if schword in emission_data.country_data:
        dataout.append(schword)
    else:
        for i in emission_data.country_data:
            if schword.lower() in i.lower():
                dataout.append(i)
    if dataout == []:
        raise ValueError
    print(dataout)
    return dataout
    
    
    

def get_country_year_data_megaton(country, year):
    "Get emmision data from dict"
    emmission = 0
    
    if year == "1990":
        emmission = emission_data.emission_1990.get(emission_data.country_data[country]['id'])
    elif year == "2005":
        emmission = emission_data.emission_2005.get(emission_data.country_data[country]['id'])   
    elif year == "2017":
        emmission = emission_data.emission_2017.get(emission_data.country_data[country]['id'])
    else:
        raise ValueError
    return emmission * 1000000
    
    

def get_country_change_for_years(country, year1, year2):
    "Get the change of emission between 2 years in country"

    
    if year1 not in "1990" and year1 not in "2005" and year1 not in "2017":
        if year2 not in "1990" and year2 not in"2005" and year2 not in "2017":
            raise ValueError
    year_1 = get_country_year_data_megaton(country, year1)
    year_2 = get_country_year_data_megaton(country, year2)
    answer = (year_2/year_1) * 100
    answer = answer - 100
    return round(answer, 2)
  
        
def get_country_data(country_name):
    "Get all country data"
    
    try:
        populat = emission_data.country_data[country_name]['population']
        if populat == []:
            answerdata = {  
            'name': country_name,
            '1990': {'emission': get_country_year_data_megaton(country_name, "1990"), 'population': None}, 
            '2005': {'emission': get_country_year_data_megaton(country_name, "2005"), 'population': None}, 
            '2017': {'emission': get_country_year_data_megaton(country_name, "2017"), 'population': None},
            'emission_change': (get_country_change_for_years(country_name, "1990", "2005")
            , get_country_change_for_years(country_name, "2005", "2017"))
            }
        else:

            answerdata = {  
                'name': country_name,
                '1990': {'emission': get_country_year_data_megaton(country_name, "1990"), 'population': populat[0]},
                '2005': {'emission': get_country_year_data_megaton(country_name, "2005"), 'population': populat[1]},
                '2017': {'emission': get_country_year_data_megaton(country_name, "2017"), 'population': populat[2]},
                'emission_change': (get_country_change_for_years(country_name, "1990", "2005")
                , get_country_change_for_years(country_name, "2005", "2017"))
        
        }
        
    except ValueError:
        print("Not a country")
    return answerdata
    
def print_country_data(data):
    "Prints all the country data"
    print(data['name'])
    print("Emission          - 1990: " + 
    str(data['1990']['emission']) + "    " + "-2005: " + 
    str(data['2005']['emission']) + "    " + "-2017: " + str(data['2017']['emission']) + "    ")
    print("Emission change   -   1990-2005: " 
    + str(data['emission_change'][0]) + "%" + "        2005-2017: " + str(data['emission_change'][1]) + "%")
    if data['1990']['population'] is None:
        print("Missing population data!")
    else:
        print("Population        - 1990: " + 
        str(data['1990']['population']) + "       2005: " + 
        str(data['2005']['population']) + "   2017: " + str(data['2017']['population']))
    