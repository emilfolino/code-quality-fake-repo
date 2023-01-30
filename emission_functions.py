"""
Functions that make use of emission data.
"""

# import pprint
from operator import itemgetter
import emission_data

def search_country(search_word):
    """
    Searches for a word or part of a word. 
    Returns the matches if there are any, raises ValueError otherwise.
    """
    l = []
    search_word = search_word.lower()
    for key in emission_data.country_data:
        if search_word in key.lower():
            l.append(key)
    if l == []:
        raise ValueError('Country does not exist!')
    return l

def find_id(country_input):
    """
    Finds ID of a country.
    called from:
        get_country_year_data_megaton
    """
    for country in emission_data.country_data:
        if country_input == country:
            identification = emission_data.country_data[country_input]['id']
    
    return identification

def decide_emission_data(year_input):
    """
    Decides which emission data to pull.
    called from:
        get_country_year_data_megaton
        ordered_co2_emissions
    """
    emission_data_selector = 'not valid'
    
    if year_input == '1990':
        emission_data_selector = emission_data.emission_1990
    elif year_input == '2005':
        emission_data_selector = emission_data.emission_2005
    elif year_input == '2017':
        emission_data_selector = emission_data.emission_2017
    
    return emission_data_selector

def get_country_year_data_megaton(country, year):
    """
    Finds emission data for a specific country and year.
    called from:
        get_country_change_for_years
        create_emission_tuple
    """
    og_data = ''
    if decide_emission_data(year) != 'not valid':
        og_data = decide_emission_data(year)[find_id(country)]
    else:
        raise ValueError("Wrong year!")
    return megaton_calculation(og_data)

def megaton_calculation(emissions):
    """
    Converts emissions to megatons.
    called from:
        get_country_year_data_megaton
        ordered_co2_emissions
    """
    return emissions * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Gets emissions for two years and compares the ratio between them.
    """
    first_input_emission = get_country_year_data_megaton(country, year2)
    second_input_emission = get_country_year_data_megaton(country, year1)

    return emission_difference(first_input_emission, second_input_emission)

def emission_difference(data1, data2):
    """
    Changes decimal to percentage and rounds to two decimals.
    called from:
        get_country_change_for_years
    """
    diff = round((((data1/data2) - 1) * 100), 2)
    return diff

def create_emission_tuple(country_name):
    """
    Creates a tuple with emission data for 1990, 2005, 2017.
    called from:
        load_unedited_data
    """
    emission_1990 = get_country_year_data_megaton(country_name, '1990')
    emission_2005 = get_country_year_data_megaton(country_name, '2005')
    emission_2017 = get_country_year_data_megaton(country_name, '2017')
    return (emission_1990, emission_2005, emission_2017)

def get_country_data(country_name):
    """
    Creates an edited dictionary of country data.
    called from:
        print_country_data
    """
    # Loads unedited data w/ name and emissions.
    unedited_country_dic = {}
    emissions = create_emission_tuple(country_name)
    for country in emission_data.country_data:
        if country_name == country:
            unedited_country_dic = emission_data.country_data[country_name]
            unedited_country_dic['name'] = country_name
            unedited_country_dic['emissions'] = emissions
    
    edited_country_dic = unedited_country_dic

    # Assigns each year as key with emission/population dict as value
    years = ('1990', '2005', '2017')
    for i, year in enumerate(years):
        try:
            edited_country_dic[year] = dict({'emission': edited_country_dic['emissions'][i], 
                                        'population': edited_country_dic['population'][i]})
        except IndexError:
            edited_country_dic[year] = dict({'emission': edited_country_dic['emissions'][i], 'population': None})
    
    # Adds emission difference tuple to main dictionary
    emission_diff_1990_2005 = get_country_change_for_years(country_name, '1990', '2005')
    emission_diff_2005_2017 = get_country_change_for_years(country_name, '2005', '2017')
    edited_country_dic['emission_change'] = (emission_diff_1990_2005, emission_diff_2005_2017)
    
    # Removes unnecessary keys from main dictionary
    popped_keys = ['area', 'id', 'population', 'emissions']
    for key in popped_keys:
        edited_country_dic.pop(key)

    return edited_country_dic

def print_country_data(data):
    """
    Formats and prints the data from get_country_data
    """
    
    # Creates a string with emission data
    years = ('1990', '2005', '2017')
    emission_list = []
    for year in years:
        emission_list.append(data[year]['emission'])
    emission_string = 'Emission\t'
    for i, year in enumerate(years):
        emission_string += year + ': ' + str(emission_list[i]) + "\t"

    # Creates a string with emission changes in two periods
    first, second = data['emission_change']
    emission_change_string = f'Emission change\t1990-2005: {first}%\t 2005-2017: {second}%'

    # Creates a string with population data
    population_list = []
    for year in years:
        population_list.append(data[year]['population'])
    population_string = 'Population\t'
    for i, year in enumerate(years):
        if population_list[i] is None:
            population_string += year + ': ' + 'Missing population data!' + "\t"
        else:
            population_string += year + ': ' + str(population_list[i]) + "\t"

    # Prints name of country and strings generated above
    print_variables = (data['name'], emission_string, emission_change_string, population_string)
    for variables in print_variables:
        print(variables)

# EXTRA EXTRA EXTRA #
def ordered_co2_emissions(year, amount):
    """
    Outputs top CO2 offenders for a specific year, amount of countries controlled by 'amount'.
    """
    emission_data_per_year = decide_emission_data(year)
    sorted_emission_data = sort_top_first(emission_data_per_year)

    for i in range(amount):
        country_name = id_to_country(sorted_emission_data[i][0])
        emission_amount = megaton_calculation(sorted_emission_data[i][1])
        print(f'{country_name}: {emission_amount}')

def id_to_country(ident):
    """
    Converts an ID (ident) to the corresponding country name and returns it.
    called from:
        ordered_co2_emissions
    """
    country_data = emission_data.country_data
    country_keys = country_data.keys()

    key_to_return = ''

    for key in country_keys:
        country_id = country_data[key]["id"]
        if ident == country_id:
            key_to_return = key
    return key_to_return

def get_population_data_per_year(year):
    """
    Gets population data per year.
    called from:
        emissions_per_capita
    """
    data_from_country = emission_data.country_data
    population_dic = {}

    if year == '1990':
        tuple_index = 0
    elif year == '2005':
        tuple_index = 1
    elif year == '2017':
        tuple_index = 2
    
    for key, value in data_from_country.items():
        try:
            population_dic[key] = value['population'][tuple_index]
        except IndexError:
            population_dic[key] = 0

    return population_dic

def emissions_per_capita(year, amount=None):
    """
    Calculates and prints emissions per capita.
    """
    emission = decide_emission_data(year)
    population = get_population_data_per_year(year)
    capita_dic = create_dic(population, emission)
    sorted_capita_dic = sort_top_first(capita_dic)
    print_results(sorted_capita_dic, amount)

def get_area_per_country():
    """
    Gets area per country.
    called from:
        emissions_per_area
    """
    country_data = emission_data.country_data
    area_dic = {}
    for key, value in country_data.items():
        area_dic[key] = value['area']
    return area_dic

def emissions_per_area(year, amount=None):
    """
    Calculates and prints emissions per area.
    """
    emission = decide_emission_data(year)
    area = get_area_per_country()
    epa_dic = create_dic(area, emission)
    sorted_epa_dic = sort_top_first(epa_dic)
    print_results(sorted_epa_dic, amount)

def sort_top_first(data):
    """
    Sorts dictionaries based on values in descending order.
    called from:
        emissions_per_capita, emissions_per_area
    """
    data = sorted(data.items(), key=itemgetter(1), reverse=True)
    return data

def print_results(sorted_dic, amount):
    """
    Prints the data from dictionaries generated by emissions_per_capita and emissions_per_area
    called from:
        emissions_per_capita, emissions_per_area
    """
    for j, ki in enumerate(sorted_dic):
        if amount is None or j < amount:
            print(f'{ki[0]}: {ki[1]}')
        

def create_dic(data, emission):
    """
    Creates a new dictionary with data from pop or area.
    called from:
        emissions_per_capita, emissions_per_area
    """
    new_dic = {}
    for key, value in data.items():
        country_id = find_id(key)
        mega_emission = megaton_calculation(emission[country_id])
        pop_or_area = value
        if pop_or_area != 0:
            per_unit = mega_emission / pop_or_area
            new_dic[key] = round(per_unit, 2)
        else:
            new_dic[key] = 0
    
    return new_dic
