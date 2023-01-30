"""
emission funktions
"""

import emission_data


def search_country(the_input):
    """
    hitta länder i listan
    """
    contry_match = []
    for contry in emission_data.country_data:
        if str(the_input).lower() in str(contry).lower():
            contry_match.append(contry)

    
    if len(contry_match) == 0:
        raise ValueError ("Country does not exist!")
            
    return contry_match



def get_country_year_data_megaton(contry, year):
    """
    gets the emission data
    """
    try:
        contry_info = emission_data.country_data[contry]
        the_id = contry_info["id"]

    except KeyError:
        return KeyError ("Country does not exist!")



    if int(year) == 1990:
        the_year = emission_data.emission_1990[the_id]
    elif int(year) == 2005:
        the_year = emission_data.emission_2005[the_id]
    elif int(year) == 2017:
        the_year = emission_data.emission_2017[the_id]
    else:
        raise ValueError ("Wrong year!")
    the_year = the_year * 1000000

    return int(the_year)

def get_country_change_for_years(contry, year1, year2):
    """
    get the change in emition
    """


    
    emision1 = get_country_year_data_megaton(contry, year1)
    emision2 = get_country_year_data_megaton(contry, year2)


    if isinstance(emision1, KeyError):
        raise KeyError ("Country does not exist!")

    if isinstance(emision1, ValueError) or isinstance(emision2, ValueError):
        raise ValueError ("Wrong year!")

    emission_change = procent_calc(emision2, emision1)
    return round(emission_change, 2)


def procent_calc(x, y):
    """
    procent calk
    """
    change = x - y
    new_num = change / y
    procent = new_num * 100
    return procent

    



def get_country_data(country_name):
    """
    a funktion that gets the contry data
    """

    validation = search_country(country_name)
    if  isinstance(validation, ValueError):
        return print('Country does not exist!')


    the_yers = [1990, 2005, 2017]
    the_return_dic = {
        'name': country_name,
    '1990': {},
    '2005': {},
    '2017': {},
    'emission_change': None
    }
    c = 0

    for year in the_yers: 
        try:
            emmision = get_country_year_data_megaton(validation[0], year)
            the_return_dic[str(year)]["emission"] = float(emmision)  

        except ValueError:
            the_return_dic[str(year)]["emission"] = None

        try:
            population = emission_data.country_data[validation[0]]["population"][c]
            the_return_dic[str(year)]["population"] = population
            c += 1
        except KeyError:
            the_return_dic[str(year)]["population"] = None
        except IndexError:
            the_return_dic[str(year)]["population"] = None

    change1 = get_country_change_for_years(validation[0], 1990, 2005)
    change2 = get_country_change_for_years(validation[0], 2005, 2017)
    the_return_dic['emission_change'] = (change1, change2)

    return the_return_dic


def print_country_data(the_return_dic):
    """
    prints the diktionary
    """

    p = []
    em = []

    
    for i in the_return_dic.values():
        try:
            p.append(i["population"])
            em.append(round(i["emission"], 1))
        except TypeError:
            r = i
    
    if p[1] is not None and em[1] is not None:
        print(f"""
{the_return_dic["name"]}
Emission          - 1990: {em[0]}    2005: {em[1]}        2017: {em[2]}
Emission change   -   1990-2005: {r[0]}%        2005-2017: {r[1]}%
Population        - 1990: {p[0]}       2005: {p[1]}   2017: {p[2]}         
            """)

    if p[1] is None:
        print(f"""
{the_return_dic["name"]}
Emission          - 1990: {em[0]}    2005: {em[1]}        2017: {em[2]}
Emission change   -   1990-2005: {r[0]}%        2005-2017: {r[1]}%
Population        - "Missing population data!"         
            """)
