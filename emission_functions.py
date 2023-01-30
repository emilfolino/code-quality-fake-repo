# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long

"""
Filen för att ta hand om alla beräkningar för utsläppen
"""
import emission_data

def search_country(search_word):
    """
    Hämta alla länder som matchar en sträng
    """
    countries = []
    for x in emission_data.country_data:
        if(search_word.lower() in x.lower()):
            countries.append(x)
    if len(countries) != 0:
        return countries
        
    raise ValueError()


def get_country_year_data_megaton(country, year):
    """
    Hämta landets utsläpp
    """
    countryName = ''
    emission = 0
    for k, v in emission_data.country_data.items():
        if(country.lower() == k.lower()):
            countryName = k
            if(year == "1990"):
                emission = emission_data.emission_1990[v["id"]]*1000000
            elif(year == "2005"):
                emission = emission_data.emission_2005[v["id"]]*1000000                
            elif(year == "2017"):
                emission = emission_data.emission_2017[v["id"]]*1000000
            else:
                raise ValueError("Wrong year!")
    print("{}:{}%".format(countryName, emission))
    return emission

def get_country_change_for_years(country, year1, year2):
    """
    Hämta utsläpps skillnaden
    """
    countryId = 0
    countryName = ""
    emission1 = 0
    emission2 = 0
    for k, v in emission_data.country_data.items():
        if(country.lower() in k.lower()):
            countryId = v['id']
            countryName = k
            if(year1 == "1990"):
                emission1 = emission_data.emission_1990[countryId]
            elif(year1 == "2005"):
                emission1 = emission_data.emission_2005[countryId]
            elif(year1 == "2017"):
                emission1 = emission_data.emission_2017[countryId]
            else:
                raise ValueError()
                
            
            if(year2 == "1990"):
                emission2 = emission_data.emission_1990[countryId]
            elif(year2 == "2005"):
                emission2 = emission_data.emission_2005[countryId]
            elif(year2 == "2017"):
                emission2 = emission_data.emission_2017[countryId]
            else:
                print("Wrong year!")
    res = [countryName, round(((emission2-emission1)/emission1)*100, 2)]
    print("{}:{}%".format(res[0], res[1]))
    return res[1]

def get_country_data(country_name):
    """
    Hämta länders data
    """
    data = {}
    for k, v in emission_data.country_data.items():
        if(country_name.lower() in k.lower()):
            if v['population']:
                data = {
                    'name': k,
                    '1990': {
                        'emission': get_country_year_data_megaton(k,'1990'),
                        'population': v['population'][0]
                    },
                    '2005' : {
                        'emission': get_country_year_data_megaton(k,'2005'),
                        'population': v['population'][1]
                    },
                    '2017':
                    {
                        'emission': get_country_year_data_megaton(k,'2017'),
                        'population': v['population'][2]
                    },
                    'emission_change': (get_country_change_for_years(k,'1990','2005'), get_country_change_for_years(k,'2005','2017'))
                }
            else:
                data = {
                    'name': k,
                    '1990': {
                        'emission': get_country_year_data_megaton(k,'1990'),
                        'population': None
                    },
                    '2005' : {
                        'emission': get_country_year_data_megaton(k,'2005'),
                        'population': None
                    },
                    '2017':
                    {
                        'emission': get_country_year_data_megaton(k,'2017'),
                        'population': None
                    },
                    'emission_change': (get_country_change_for_years(k,'1990','2005'), get_country_change_for_years(k,'2005','2017'))
                }
    return data

def print_country_data(data):
    """
    Skriv ut datan
    """
    print(data['name'])
    print("Emission" "\t", "1990:", data['1990']['emission'], " " "\t", "2005:", data['2005']['emission'], "\t", "2017:", data['2017']['emission'])
    print("Emission change" "\t", "1990-2005:", "{}%".format(data['emission_change'][0]), "\t" ,"2005-2017:", "{}%".format(data['emission_change'][1]))
    if data['1990']['population'] is not None:
        print("Population" "\t", "1990:", data['1990']['population'], " " "\t", "2005:", data['2005']['population'], "\t", "2017:", data['2017']['population'])
    else:
        print("Missing population data!")
