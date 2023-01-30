"""
Functions for using emissions data.
"""

import emission_data as em_d

id_dict = {data['id']: country_name for country_name, data in em_d.country_data.items()}

def search_country(search_word):
    """
    Searches for a matching substring in country_data dict keys.
    """
    search_word = search_word.lower()
    search_results = []
    for key in em_d.country_data:
        if search_word in key.lower():
            search_results.append(key)
    if search_results == []:
        raise ValueError("Country does not exist!")
    return search_results

def case_insensitive_country_lookup(country_query):
    """
    Returns country ID of country (full name only) or raises error if not found.
    Case insensitive, returns cased name.
    """
    country_query = country_query.lower()
    for country_name in em_d.country_data:
        if country_name.lower() == country_query:
            return country_name
    raise ValueError("Country does not exist!")

def get_country_year_data_megaton(country, year):
    """
    Gets emissions data from a country and returns a conversion from teratons (?) to megatons.
    (Jag tror nåt gick fel i uppgiften. Det står att datan redan är i megaton på ett ställe och
        att vi ska konvertera det till megaton på ett annat ställe. Jag tror att datan redan är
        i megaton och att den här funktionen konverterar det till ton, så funktionen är lite
        förvirrande feldöpt. Här låtsades jag som att teraton är en grej för att bevara intern
        logik eftersom funktionerna måste bli döpta enligt uppgiften...)
    """
    country_id = em_d.country_data[case_insensitive_country_lookup(country)]['id']
    if year == '1990':
        teratons = em_d.emission_1990[country_id]
    elif year == '2005':
        teratons = em_d.emission_2005[country_id]
    elif year == '2017':
        teratons = em_d.emission_2017[country_id]
    else:
        raise ValueError("Wrong year!")
    return teratons * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Returns the percent change in emissions in a certain country from year1 to year2.
    """
    year1_megatons = get_country_year_data_megaton(country, year1)
    year2_megatons = get_country_year_data_megaton(country, year2)
    return round(((year2_megatons - year1_megatons) / year1_megatons * 100), 2)

def get_country_data(country_name):
    """
    Reformats data (emissions, emission change, population) from one input country into a new dict.
    """
    country_name = case_insensitive_country_lookup(country_name)
    data = {'name': country_name}
    for i, year in enumerate(('1990', '2005', '2017')):
        data[year] = {'emission': get_country_year_data_megaton(country_name, year)}
        if em_d.country_data[country_name]['population'] == []:
            data[year]['population'] = None
        else:
            data[year]['population'] = em_d.country_data[country_name]['population'][i]
    data['emission_change'] = (get_country_change_for_years(country_name, '1990', '2005'),
        get_country_change_for_years(country_name, '2005', '2017'))
    return data

def print_country_data(data):
    """
    Prints data from get_country_data function.
    """
    print(data['name'])
    print("Emissions:\t\t1990: {}\t2005: {}\t2017: {}".format(
            str(data['1990']['emission']),
            str(data['2005']['emission']),
            str(data['2017']['emission']))
        )
    print("Change in emissions:\t\t1990-2005: {}%\t2005-2017: {}%".format(
            str(data['emission_change'][0]),
            str(data['emission_change'][1]))
        )
    if isinstance(em_d.country_data[data['name']]['population'], tuple):
        print("Population:\t\t1990: {}\t2005: {}\t2017: {}".format(
                str(data['1990']['population']),
                str(data['2005']['population']),
                str(data['2017']['population']))
            )
    else:
        print("Missing population data!")

def emissions_country_list_for_year(year):
    """
    Outputs an unsorted list of all countries (IDs converted to country names) and their 
    emissions (converted) in given year. Each item in the list is a list: [emissions, country_name].
    """
    if year == '1990':
        year_data = em_d.emission_1990
    elif year == '2005':
        year_data = em_d.emission_2005
    elif year == '2017':
        year_data = em_d.emission_2017
    else:
        raise ValueError("Wrong year!")
    return [[id_dict[country_id], emissions * 1000000] for country_id, emissions in year_data.items()]

def top_emissions_gross(year, top_n=False):
    """
    Returns a string listing countries with emission data for the given year, ordered by descending
    amount of emissions, optionally limited to a user-specified number of countries.
    """
    emissions_str = ""
    emissions_list = sorted(emissions_country_list_for_year(year), key=lambda x: x[1], reverse=True)
    if top_n:
        try:
            emissions_list = emissions_list[:int(top_n)]
        except ValueError("Number must be an integer!") as e:
            raise e
    for country, emissions in emissions_list:
        emissions_str += f"{country}: {round(emissions, 2)}" + "\n"
    return emissions_str

def top_emissions_per_capita(year, top_n=False):
    """
    Returns a string listing countries with emission data per capita for the given year,
    in descending order, optionally limited to a user-specified number of countries.
    """
    emissions_str = ""
    emissions_list = emissions_country_list_for_year(year)
    for i, [country, emissions] in enumerate(emissions_list):
        population = em_d.country_data[country]['population']
        if population:
            if year == '1990':
                population = population[0]
            elif year == '2005':
                population = population[1]
            elif year == '2017':
                population = population[2]
            emissions_list[i][1] = emissions / population
        else:
            emissions_list[i][1] = None
    emissions_list[:] = (v for v in emissions_list if v[1] is not None)
    emissions_list = sorted(emissions_list, key=lambda x: x[1], reverse=True)
    if top_n:
        try:
            emissions_list = emissions_list[:int(top_n)]
        except ValueError("Number must be an integer!") as e:
            raise e
    for country, emissions in emissions_list:
        emissions_str += f"{country}: {round(emissions, 2)}" + "\n"
    return emissions_str

def emissions_per_km2(year, top_n=False):
    """
    Returns a string listing countries with emission data per square km for the given year,
    in descending order, optionally limited to a user-specified number of countries.
    """
    emissions_str = ""
    emissions_list = emissions_country_list_for_year(year)
    for i, [country, emissions] in enumerate(emissions_list):
        area = em_d.country_data[country]['area']
        if area > 0:
            emissions_list[i][1] = emissions / area
        else:
            emissions_list[i][1] = None
    emissions_list[:] = (v for v in emissions_list if v[1] is not None)
    emissions_list = sorted(emissions_list, key=lambda x: x[1], reverse=True)
    if top_n:
        try:
            emissions_list = emissions_list[:int(top_n)]
        except ValueError("Number must be an integer!") as e:
            raise e
    for country, emissions in emissions_list:
        emissions_str += f"{country}: {round(emissions, 2)}" + "\n"
    return emissions_str

# if __name__ == '__main__':
#     print(top_emissions_per_capita("2017", "3"))


# try adding map() where applicable instead of for-loops
