"""
DOCSTRING
"""

import emission_data

emission_dataa = emission_data.country_data
emission_dataaa = emission_data.emission_1990
emission_dataaaa = emission_data.emission_2005
emission_dataaaaa = emission_data.emission_2017


def search_country(search_word):
    """
    Looks if substring is in string
    """
    l = []
    for keys in emission_dataa:
        search_word = search_word.lower()
        key = keys.lower()
        if search_word in key:
            l.append(keys)
    if not l:
        raise ValueError("Country does not exist!")
    return l

def get_country_year_data_megaton(country, year):
    """
    Looks up megaton emissions
    """
    year = int(year)
    idd = emission_dataa[country]['id']
    if year == 1990:
        for (k, v) in emission_dataaa.items():
            if idd == k:
                return v * 1000000
    elif year == 2005:
        for (k, v) in emission_dataaaa.items():
            if idd == k:
                return v * 1000000
    elif year == 2017:
        for (k, v) in emission_dataaaaa.items():
            if idd == k:
                return v * 1000000
    else:
        raise ValueError("Wrong year!")
    return None

def get_country_change_for_years(country, year1, year2):
    """
    Compare emissions by year
    """
    x = get_country_year_data_megaton(country, year1)
    y = get_country_year_data_megaton(country, year2)
    try:
        p = ((y - x) / x) * 100
        p = round(p, 2)
    except ValueError:
        return ValueError
    return p


def get_country_data(country_name):
    """
    Takes data puts data in dict
    """
    Name = country_name
    e = get_country_year_data_megaton(country_name, 1990)
    d = get_country_year_data_megaton(country_name, 2005)
    f = get_country_year_data_megaton(country_name, 2017)
    pop = emission_dataa[Name]
    try:
        pop1 = pop['population'][0]
    except IndexError:
        pop1 = None  
    try:
        pop2 = pop['population'][1]
    except IndexError:
        pop2 = None 
    try:
        pop3 = pop['population'][2]
    except IndexError:
        pop3 = None
    change1 = get_country_change_for_years(country_name, 1990, 2005)
    change2 = get_country_change_for_years(country_name, 2005, 2017)
    
    d = {
        'name': Name,
        '1990': {'emission': e, 'population': pop1 },
        '2005': {'emission': d, 'population': pop2 },
        '2017': {'emission': f, 'population': pop3 },
        'emission_change': (change1, change2)
    }
    return d




def print_country_data(data):
    """
    Prints out dict really nice
    """
    pop1 = data['1990']['population']
    pop2 = data['2005']['population']
    pop3 = data['2017']['population']
    e = str(data['emission_change'][0])
    e = e + "%"
    d = str(data['emission_change'][1])
    d = d + "%"
    if not pop1:
        pop1 = "Missing population data!" 
    if not pop2:
        pop2 = "Missing population data!" 
    if not pop3:
        pop3 = "Missing population data!" 

    print(data['name'])
    print("Emissions", '1990:',
     data['1990']['emission'], '2005:',
      data['2005']['emission'], '2017:',
       data['2017']['emission'])
    print('Emission change', '1990-2005:', e ,'2005-2017:', d )
    print('Population', '1990:', pop1, '2005:', pop2, '2017:', pop3)


def high_emission(year, placement):
    """
    Gets tops emissioners
    """
    high = ""
    counter = 1
    placement = int(placement)
    if year == "1990":
        a = sorted(emission_dataaa.items(), key=lambda x: x[1], reverse=True)
        e = (a[0: placement])
    elif year == "2005":
        a = sorted(emission_dataaaa.items(), key=lambda x: x[1], reverse=True)
        e = (a[0: placement])
    elif year == "2017":
        a = sorted(emission_dataaaaa.items(), key=lambda x: x[1], reverse=True)
        e = (a[0: placement])
    else:
        raise ValueError("Wrong year!")
    for k in e:
        e = (k[0])
        for (x, y) in emission_dataa.items():
            if y['id'] == e:
                j = a[counter - 1:counter]
                high = high + x + ": " + str(j[0][1] * 1000000) + "\n"
                counter = counter + 1
    return high
    