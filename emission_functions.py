"""
Emission functions
"""

from operator import itemgetter
import emission_data


def search_country(search_word):
    """
    creates new list, assigns the keys(names) of original dict to the list
    if argument is in the list, it adds to the new list and returns
    if it's not in the list it raises error
    """
    liste = []
    listem = list(emission_data.country_data.keys())
    for country in listem:
        if search_word.lower() in country.lower():
            liste.append(country)
    if not liste:
        raise ValueError ("Country does not exist!")

    return liste


def get_country_year_data_megaton(country, year):
    """
    Get country info for a specific year
    """
    years = [1990, 2005, 2017]
    year = int(year)

    if search_country(country):
        if year not in years:
            raise ValueError ("Wrong year!")
        for country_found in search_country(country):
            if year == 2017:
                return emission_data.emission_2017[emission_data.country_data[country_found]['id']]*1000000
            if year == 1990:
                return emission_data.emission_1990[emission_data.country_data[country_found]['id']]*1000000
            if year == 2005:
                return emission_data.emission_2005[emission_data.country_data[country_found]['id']]*1000000
    
    return None

def get_country_change_for_years(country, year1, year2): #1990-2005
    """
    get emission chagne for a country between two years
    """

    total_change = get_country_year_data_megaton(country, year2) - get_country_year_data_megaton(country, year1)
    total_perc = (total_change / get_country_year_data_megaton(country, year1)) * 100
    return round(total_perc,2)


def get_country_data(country):
    """
    create a new list for a country
    """

    data_dict = {}
    data_dict['name'] = country
    data_dict['1990']= {}
    data_dict['2005']= {}
    data_dict['2017']= {}
    data_dict['1990']['emission'] =  get_country_year_data_megaton(country, 1990)
    data_dict['2005']['emission'] =  get_country_year_data_megaton(country, 2005)
    data_dict['2017']['emission'] =  get_country_year_data_megaton(country, 2017)
    if not emission_data.country_data[country]['population']:
        data_dict['1990']['population'] = None
        data_dict['2005']['population'] = None
        data_dict['2017']['population'] = None
    else:
        data_dict['1990']['population'] = emission_data.country_data[country]['population'][0]
        data_dict['2005']['population'] = emission_data.country_data[country]['population'][1]
        data_dict['2017']['population'] = emission_data.country_data[country]['population'][2]
    data_dict['emission_change'] = (get_country_change_for_years(country, 1990, 2005) ,
    get_country_change_for_years(country, 2005, 2017))

    return data_dict

def print_country_data(country):
    """
    Print the created dictionary
    """
    strx = "Missing population data!"

    for x in range(0,len(country.items())):
        if x == 1:
            print("""Emission           -    1990: """ + str(country['1990']['emission'])
            +"""   2005: """ + str(country['2005']['emission']) +
            """    2017: """+ str(country['2017']['emission'])
            )
        if x == 2:
            print("""Emission change    -    1990-2005: """ + str(country['emission_change'][0]) + "%"
            +"""    2005-2017: """ + str(country['emission_change'][1]) +"%"
            )
        if x == 3:
            if country['1990']['population'] is None:
                print("""Population         -    1990: """ + strx
            +"""    2005: """ + strx
            +"""    2017: """ + strx
            )
            else:

                print("""Population         -    1990: """ + str(country['1990']['population'])
                +"""    2005: """ + str(country['2005']['population'])
                +"""    2017: """ + str(country['2017']['population'])
                )

        if x==0:
            print(str(country['name']))


def arabul(date, numara):
    """
    Sorts the dictionares based on values
    then gets the megaton values on each year and prints it

    """
    liste_co2_1 = sorted(emission_data.emission_1990.items(),key=itemgetter(1),reverse=True) #list
    liste_co2_2 = sorted(emission_data.emission_2005.items(),key=itemgetter(1),reverse=True)
    liste_co2_3 = sorted(emission_data.emission_2017.items(),key=itemgetter(1),reverse=True)
    #ID : Co2 [(x,y), (a,b)]

    for num in range(0, numara):
        for x,y in emission_data.country_data.items():
            if date == 1990:
                if y['id'] == liste_co2_1[num][0]:
                    print(x + ": " +str(get_country_year_data_megaton(x,1990)))
            elif date == 2005:
                if y['id'] == liste_co2_2[num][0]:
                    print(x + ": " +str(get_country_year_data_megaton(x,2005)))
            elif date == 2017:
                if y['id'] == liste_co2_3[num][0]:
                    print(x + ": " +str(get_country_year_data_megaton(x,2017)))

def per_cap (date, numara=None):
    """
    Per cap function which creates a new dictionary
    Assigns keys and values of original dict to lists
    Iterates over the original dict and gets the emission data
    Uses math operations and assigns the vales to the new dictionary
    sorts the dictionary on the value
    """
    # first find all emissions per country
    dicT = {}
    x = 1000000
    #dict : Country : utslapp co2
    list_con = list(emission_data.country_data.keys()) #country list
    val = list(emission_data.country_data.values()) #list of dict
    for i in range(0,len(emission_data.country_data)):
        if emission_data.country_data[list_con[i]]['population']:
            if date  == 2017:
                dicT[list_con[i]] = round((emission_data.emission_2017[val[i]['id']] * x)/val[i]['population'][2],2)
            elif date == 2005:
                dicT[list_con[i]] = round((emission_data.emission_2005[val[i]['id']] * x)/val[i]['population'][1],2)
            elif date == 1990:
                dicT[list_con[i]] = round((emission_data.emission_1990[val[i]['id']] * x)/val[i]['population'][0],2)

    new_cap_dict = dict(sorted(dicT.items(),key=itemgetter(1),reverse=True))


    if numara is not None:
        for x,y in list(new_cap_dict.items())[:numara]:
            print(x + ": " + str(y))
    if numara is None:
        print(new_cap_dict)

def per_area(year, numara):
    """
    Per area function which creates a new dictionary
    Assigns keys and values of original dict to lists
    Iterates over the original dict and gets the population data
    Uses math operations and assigns the vales to the new dictionary
    sorts the dictionary on the value
    """
    cap_dict = {}
    mal = 1000000
    #dict : Country : utslapp co2
    l_con = list(emission_data.country_data.keys()) #country list
    l_val = list(emission_data.country_data.values()) #list of dict
    for i in range(0,len(emission_data.country_data)):
        if emission_data.country_data[l_con[i]]['population']:
            if year  == 2017:
                cap_dict[l_con[i]] = round(((emission_data.emission_2017[l_val[i]['id']] * mal))/l_val[i]['area'],2)
            elif year == 2005:
                cap_dict[l_con[i]] = round(((emission_data.emission_2005[l_val[i]['id']] * mal))/l_val[i]['area'],2)
            elif year == 1990:
                cap_dict[l_con[i]] = round(((emission_data.emission_1990[l_val[i]['id']] * mal))/l_val[i]['area'],2)

    new_cap_dict = dict(sorted(cap_dict.items(),key=itemgetter(1),reverse=True))


    if numara is not None:
        for x,y in list(new_cap_dict.items())[:numara] :
            print(x + ": " + str(y))
    if numara is None:
        print(new_cap_dict)
    # find population [country]
    # find emission/population
    # make list - key: country value: emission/population
