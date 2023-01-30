
""" -- """
import emission_data as ed

def search_country(search_word):
    """ -- """
    lis = []
    for key in ed.country_data:
        if search_word.lower() in key.lower():
            lis.append(key)
    if len(lis) == 0:
        raise ValueError
    return lis

years = ["1990", "2005", "2017"]

def get_country_year_data_megaton(c, y):
    """ -- """
    k = ed.country_data[c]["id"]
    if y not in years:
        raise ValueError

    num = ""

    if y == "1990":
        num = ed.emission_1990[k] * 1000000
    elif y == "2005":
        num = ed.emission_2005[k] * 1000000
    elif y == "2017":
        num = ed.emission_2017[k] * 1000000

    return num

def get_country_change_for_years(c, y, y2):
    """ -- """
    year1 = get_country_year_data_megaton(c, y)
    year2 = get_country_year_data_megaton(c, y2)

    result = ((year2 - year1) / year1) * 100
    return round(result, 2)



def get_country_data(country):
    """ -- """
    pop = ed.country_data[country]['population']
    if pop == []:
        pop = (None, None, None)
    
    data = {
        'name': country,
        '1990': {'emission': get_country_year_data_megaton(country, "1990"), 'population': pop[0]},
        '2005': {'emission': get_country_year_data_megaton(country, "2005"), 'population': pop[1]},
        '2017': {'emission': get_country_year_data_megaton(country, "2017"), 'population': pop[2]},
        'emission_change': (get_country_change_for_years(country, "1990", "2005"),
        get_country_change_for_years(country, "2005", "2017"))
    }   

    return data


def print_country_data(data):
    """ -- """
    country = data['name']
    e1990 = data["1990"]["emission"]
    e2005 = data["2005"]["emission"]
    e2017 = data["2017"]["emission"]
    pop90 = data["1990"]["population"]
    pop05 = data["2005"]["population"]
    pop17 = data["2017"]["population"]
    ec9005 = data["emission_change"][0]
    ec0517 = data["emission_change"][1]

    print("{} \n Emission - 1990: {} 2005: {} 2017: {} \n Emission change - 1990-2005: {}% 2005-2017: {}%"
    .format(country, e1990, e2005, e2017, ec9005, ec0517))
    if pop90 is None:
        print("Missing population data!")
    else:
        print("Population - 1990: {} 2005: {} 2017: {}".format(pop90, pop05, pop17))
