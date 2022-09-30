"""
emission functions for marvin
"""
import emission_data

def search_country(search_word):
    """
    search for country names or parts thereof
    """
    lc_seach_word = search_word.lower()
    result_list = []
    for name in emission_data.country_data:
        if lc_seach_word in name.lower():
            result_list.append(name)
    if len(result_list) == 0:
        raise ValueError("Country does not exist!")
    return result_list


def get_country_year_data_megaton(country, year):
    """
    Calculate the country's emission a particular year, in megatons
    """
    valid_years = '1990', '2005', '2017' # en tuple med godkända år
    if year in valid_years:
        country_id = emission_data.country_data[country]['id'] #id att skicka till rätt dictionary
        if year == '1990':
            emissions_of_the_year = 1000000 * emission_data.emission_1990.get(country_id)
        elif year == '2005':
            emissions_of_the_year = 1000000 * emission_data.emission_2005.get(country_id)
        elif year == '2017':
            emissions_of_the_year = 1000000 * emission_data.emission_2017.get(country_id)
        return emissions_of_the_year
    
    raise ValueError("Wrong year!")
    

def get_country_change_for_years(country, year1, year2):
    """
    Calculate change in emissions between two years
    """
    first_year = get_country_year_data_megaton(country, year1)
    second_year = get_country_year_data_megaton(country, year2)
    change_procent = round(100 * (second_year - first_year) / first_year, 2)
    return change_procent

def get_country_data(country_name):
    """
    Build a dictionary with country data
    """
    em_data1990 = get_country_year_data_megaton(country_name, '1990') 
    em_data2005 = get_country_year_data_megaton(country_name, '2005')
    em_data2017 = get_country_year_data_megaton(country_name, '2017')
    try: 
        pop_1990 = emission_data.country_data[country_name]['population'][0]
        pop_2005 = emission_data.country_data[country_name]['population'][1]
        pop_2017 = emission_data.country_data[country_name]['population'][2]
    except IndexError:
        pop_1990 = None #"Missing population data!"
        pop_2005 = None
        pop_2017 = None

    em_change_1990_2005 = get_country_change_for_years(country_name, '1990', '2005')
    em_change_2005_2017 = get_country_change_for_years(country_name, '2005', '2017')
    data = {
        'name': country_name,
        '1990': {'emission': em_data1990, 'population': pop_1990},
        '2005': {'emission': em_data2005, 'population': pop_2005},
        '2017': {'emission': em_data2017, 'population': pop_2017},
        'emission_change': (em_change_1990_2005, em_change_2005_2017)
        #emission_change': (<skillnad mellan 1990-2005>, <skillnad mellan 2005-2017>)
                        }
    return data

def print_country_data(data):
    """
    Print data for a country
    """
    em_1990 = data.get('1990', {}).get('emission')
    em_2005 = data.get('2005', {}).get('emission')
    em_2017 = data.get('2017', {}).get('emission')
    if (data.get('1990', {}).get('population') is not None):
        pop_1990 = data.get('1990', {}).get('population')
        pop_2005 = data.get('2005', {}).get('population')
        pop_2017 = data.get('2017', {}).get('population')
    else:
        pop_1990 = "Missing population data!"
        pop_2005 = "Missing population data!"
        pop_2017 = "Missing population data!"
    em_change1 = data['emission_change'][0]
    em_change2 = data['emission_change'][1]
    print(data.get('name'))
    print(f"Emission:\t\t 1990: {em_1990}\t2005: {em_2005}\t2017: {em_2017}")
    print(f"Population:\t\t 1990: {pop_1990}\t\t2005: {pop_2005}\t\t2017: {pop_2017}")
    print(f"Emission change:\t 1990-2005: {em_change1}%\t2005-2017: {em_change2}%")
###

def sort_countries(year, numbers = -1):
    """
    Sort countries by CO2-emissions a certain year
    """
    CO2_list, _ = list_maker(year)
    #print(CO2_list)
    sorted_CO2_list = sorted(CO2_list, reverse = True)
    if numbers == -1:
        numbers = len(sorted_CO2_list)
    result = ""
    for i in range(numbers):
        a = round(1000000 * float(sorted_CO2_list[i][0]), 2)
        result += f"{sorted_CO2_list[i][1]}: {a}\n"
    return result


def countries_CO2_pc(year, numbers = -1):
    """
    Sort countries by CO2-emissions per capita for a certain year
    """
    CO2_list, year_index = list_maker(year)

    result = ""
    newl = [] 
    for i, _ in enumerate(CO2_list):
        c = emission_data.country_data[CO2_list[i][1]]["population"]
        if len(c) != 0:
            b = round(1000000*CO2_list[i][0]/emission_data.country_data[CO2_list[i][1]]["population"][year_index], 2)
            newl.append((b, CO2_list[i][1]))
    sorted_newl = sorted(newl, reverse = True)
    if numbers == -1:
        numbers = len(sorted_newl)
    for i in range(numbers):
        result += f"{sorted_newl[i][1]}: {sorted_newl[i][0]}\n"
    return result


def list_maker(year):
    """
    Create a list with CO2-emissions for each country
    """
    CO2_list = []
    if year == '1990':
        year_index = 0
        for key, value in emission_data.country_data.items():
            CO2_list.append((emission_data.emission_1990[value['id']], key))
    elif year == '2005':
        year_index = 1
        for key, value in emission_data.country_data.items():
            CO2_list.append((emission_data.emission_2005[value['id']], key))
    elif year == '2017':
        year_index = 2
        for key, value in emission_data.country_data.items():
            CO2_list.append((emission_data.emission_2017[value['id']], key))
    return CO2_list, year_index


def countries_CO2_area(year, numbers = -1):
    """
    Sort countries by CO2-emissions per area for a certain year.
    """
    CO2_list, _ = list_maker(year)

    result = ""
    newl = []
    for i, _ in enumerate(CO2_list):
        c = emission_data.country_data[CO2_list[i][1]]["area"]
        if c != 0:
            b = round(1000000*CO2_list[i][0]/emission_data.country_data[CO2_list[i][1]]["area"], 2)
            newl.append((b, CO2_list[i][1]))
    sorted_newl = sorted(newl, reverse = True)
    if numbers == -1:
        numbers = len(sorted_newl)
    for i in range(numbers):
        result += f"{sorted_newl[i][1]}: {sorted_newl[i][0]}\n"
    return result


###
if __name__ == "__main__":
    print("Hello from emission_functions.py")
    sort_countries('1990', numbers = -1)
    result2 = countries_CO2_pc('2017', numbers = 4)
    #result3 = countries_CO2_area('1990', numbers = 2)
    print(result2)
