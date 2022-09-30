"""
Emission functions
"""

import emission_data as em

def search_country(search):
    """
    Searches for a country in database
    """
    search = search.lower()
    #Create country list
    li = []
    for land in em.country_data:
        temp = land.lower()
        if search in temp:
            li.append(land)

    #Print final string
    if len(li) > 0:
        return li
    raise ValueError

def get_country_year_data_megaton(country, year):
    """
    Get tons of emission data
    """
    #Wrong year check
    if year not in ('1990', '2005', '2017'):
        raise ValueError("Wrong year!")

    #Comment
    i = em.country_data[country]["id"]
    temp = "emission_" + str(year)
    temp = getattr(em, temp)

    return temp[i] * 1000000


def get_country_change_for_years(country, year1, year2):
    """
    Get emission difference
    """
    #Check if it exists
    if not country in em.country_data:
        return print("Country does not exist!")

    if year1 not in ('1990', '2005', '2017'):
        if year2 not in ('1990', '2005', '2017'):
            raise ValueError

    a = get_country_year_data_megaton(country, year1)
    b = get_country_year_data_megaton(country, year2)
    x = float((b / a) - 1) * 100
    return round(x, 2)


def get_country_data(country):
    """
    Get country data
    """
    if not country in em.country_data:
        raise KeyError

    #kanske o effektiv..
    try:
        pop90 = em.country_data[country]["population"][0]
        pop05 = em.country_data[country]["population"][1]
        pop17 = em.country_data[country]["population"][2]
    except IndexError:
        pop90 = None
        pop05 = None
        pop17 = None

    change1 = get_country_change_for_years(country, "1990", "2005")
    change2 = get_country_change_for_years(country, "2005", "2017")
    dataa = {
        'name': country,
        '1990': {'emission': get_country_year_data_megaton(country, "1990"), 'population': pop90},
        '2005': {'emission': get_country_year_data_megaton(country, "2005"), 'population': pop05},
        '2017': {'emission': get_country_year_data_megaton(country, "2017"), 'population': pop17},
        'emission_change': (change1, change2)
    }

    return dataa

def print_country_data(dataa):
    """
    Print the data
    """
    #Create population string
    if dataa['1990']['population'] is None:
        popString = "Missing population data!"
    else:
        popString = f"1990: {dataa['1990']['population']}      "
        popString += f"2005: {dataa['2005']['population']}      "
        popString += f"2017: {dataa['2017']['population']}"

    print(f"""
    {dataa['name']}
    Emission         - 1990: {dataa['1990']['emission']}     2005: {dataa['2005']['emission']}    2017: {dataa['2017']['emission']}
    Emission change  - 1990-2005: {dataa['emission_change'][0]}%    2005-2017: {dataa['emission_change'][1]}%
    Population       - {popString}""")
