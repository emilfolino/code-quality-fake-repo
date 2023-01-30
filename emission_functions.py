"""
here are all the emission functions for marvin
"""
from operator import itemgetter
import emission_data

def search_country(search_word, printing=1):
    """
    searches for country in emission_data by name or a part of the name
    """
    search_word = search_word.lower() #change to lower case to make it not case-sensitive
    list1 = [] # we're gonna store the found countries in a list
    found = 0 # keeps track of whether a country has been found
    for key in emission_data.country_data: # go through each keyname on the list
        if key.lower().find(search_word) != -1: # if the key (lower case) contains the search_word
            list1.append(key) # add that key to the list
            found += 1 # count how many matching countries have been found
    if found == 0: # if none of the keys match the search word
        raise ValueError("Country does not exist!") #raise an exception
    if printing == 1:
        print("Following countries were found: " + ", ".join(list1)) # print the found countries
    return list1 # in the assignment it doesn't say that this function should return a value!
    # but the validation fails if it doesn't. Unclear instructions?

def handle_input13(input13):
    """
    handles the input from menu choice 13 and uses it to call get_country_change_for_years
    """
    commands = input13.split(",") #splits user unput into separate strings to handle
    if len(commands) < 3:
        raise ValueError("This function requires 3 arguments: country,year1,year2")
    country = str(search_country(commands[0], 0)[0]) #find the country and check if it exists
    # possibly too complicated, might be better to just raise an exception in get_country_change?
    # I can't figure out how to handle the exception though
    valid_years = "1990", "2005", "2017"
    if commands[1] in valid_years:
        start = commands[1]
    else:
        raise ValueError("Wrong year! {} is not a valid year!".format(commands[1]))
    if commands[2] in valid_years:
        end = commands[2]
    else:
        raise ValueError("Wrong year! {} is not a valid year!".format(commands[2]))
    result = get_country_change_for_years(country, start, end)
    return result

def get_country_change_for_years(country, year1, year2, printing=1):
    """
    Calculates the % change in emissions for a chosen country between chosen years
    """
    emissions1 = get_country_year_data_megaton(country,year1)
    emissions2 = get_country_year_data_megaton(country,year2)
    dif = float(emissions2) - float(emissions1)
    dif = dif / emissions1
    dif *= 100
    dif = round(dif,2)
    if printing == 1:
        print("{}:{}%".format(country,dif))
    return dif

def get_country_year_data_megaton(country, year):
    """
    calculates how much emissions a given country released in a given year
    """
    emissions = ""
    country_id = emission_data.country_data[country]["id"]
    if year == "1990":
        emissions = emission_data.emission_1990[country_id] * 1000000 
        #aren't the emissions ALREADY in megatons? Why am I converting them to tons?????
    elif year == "2005":
        emissions = emission_data.emission_2005[country_id] * 1000000
    elif year == "2017":
        emissions = emission_data.emission_2017[country_id] * 1000000
    else:
        raise ValueError("Wrong year!")
    return emissions

def get_country_data(country_name):
    """
    gets data about a country
    """
    country = (search_country(country_name, 0))[0] # search_country returns a list, not a str

    emission1990 = get_country_year_data_megaton(country, "1990")
    emission2005 = get_country_year_data_megaton(country, "2005")
    emission2017 = get_country_year_data_megaton(country, "2017")

    try:
        pop1990 = emission_data.country_data[country]["population"][0]
    except IndexError:
        pop1990 = None
    try:
        pop2005 = emission_data.country_data[country]["population"][1]
    except IndexError:
        pop2005 = None
    try:
        pop2017 = emission_data.country_data[country]["population"][2]
    except IndexError:
        pop2017 = None

    change1 = get_country_change_for_years(country, "1990", "2005", 0)
    change2 = get_country_change_for_years(country, "2005", "2017", 0)

    data = {
    'name' : country,
    '1990' : {'emission': emission1990, 'population': pop1990},
    '2005' : {'emission': emission2005, 'population': pop2005},
    '2017' : {'emission': emission2017, 'population': pop2017},
    'emission_change' : (change1, change2)
    }

    return data

def print_country_data(data):
    """
    formats and prints country data
    """
    if data["1990"]["population"] is None:
        population = "Missing population data!"
    else:
        population = ("\nPopulation - \t1990: {p1}\t 2005: {p2}\t 2017: {p3}"
                      .format(p1 = data["1990"]["population"], 
                      p2 = data["2005"]["population"], p3 = data["2017"]["population"]))

    print(data["name"]
        + "\nEmission - \t1990: {em1}\t2005: {em2}\t2017: {em3}"
        .format(em1=data["1990"]["emission"], em2=data["2005"]["emission"], em3=data["2017"]["emission"])
        + "\nEmission change - \t1990-2005: {c1}%\t2005-2017: {c2}%"
        .format(c1=data["emission_change"][0],c2=data["emission_change"][1])
        + population)

def e1(input_e1):
    """
    prints the emissions per country in a given year, descending, for the chosen no. of countries
    """
    commands = input_e1.split(" ")
    valid_years = "1990", "2005", "2017"
    if commands[0] in valid_years:
        year = commands[0]
    else:
        raise ValueError("Wrong year! {} is not a valid year!".format(commands[0]))
    try:
        no_countries = int(commands[1])
    except ValueError:
        print("The number of countries needs to be an integer!")
        return
    except IndexError:
        print("You need to write a year and the desired number of countries.")
        return

    if year == "1990":
        as_list = emission_data.emission_1990.items()
    elif year == "2005":
        as_list = emission_data.emission_2005.items()
    elif year == "2017":
        as_list = emission_data.emission_2017.items()
    sorted_list = sorted(as_list, key=itemgetter(1), reverse=True)
    sorted_list = sorted_list[0:no_countries]
    print(sorted_list)
    new_list = []
    for i, element in enumerate(sorted_list):
        for key, value in emission_data.country_data.items():
            if (value["id"]) == element[0]:
                new_list.append((str(key),sorted_list[i][1]))
    for i, element in enumerate(new_list):
        print("{country}: {emissions}".format(country = element[0], emissions = element[1]))

def input_for_e2_e3(input_e2_e3):
    """
    return emissions_as_list, countries_by_id, pop (1, 2 or 3, corresponding to the year), no_c (desired countries)
    handles the input for functions e2, e3, since they require similar handling
    """
    commands = input_e2_e3.split(" ") #split the input into the year and possibly no.countries
    valid_years = "1990", "2005", "2017"
    countries_exist = len(emission_data.country_data) #the number of countries on the list
    if commands[0] in valid_years:
        year = commands[0]
    else:
        raise ValueError("Wrong year! {} is not a valid year!".format(commands[0]))
    if len(commands) > 1: #if the user put in the no. of countries
        try:
            no_c = int(commands[1]) #check if it's an integer
        except ValueError:
            print("The number of countries needs to be an integer!")
            return -1
        if no_c > countries_exist: #check if the no. of countries is a valid index
            raise ValueError("There are only {x} countries on the list.".format(x = countries_exist))
    else:
        no_c = countries_exist #if the user hasnät specified the no. of countries, take all of them

    if year == "1990": #find the relevant dictionary and turn it into a list
        emissions_as_list = list(emission_data.emission_1990.items())
        pop = 0
    elif year == "2005":
        emissions_as_list = list(emission_data.emission_2005.items())
        pop = 1
    else: #year == "2017"
        emissions_as_list = list(emission_data.emission_2017.items())
        pop = 2

    #sort the country data by id:
    countries_by_id = sorted(emission_data.country_data.items(), key = lambda tup: (tup[1]["id"]))
    
    return emissions_as_list, countries_by_id, pop, no_c

def e2(input_e2):
    """
    Användaren ska skriva in ett år och få utskriften varje lands utsläpp per capita,
    sortera i storleksordning, avrunda till 2 decimaler. 
    Det ska även gå att skriva in hur många länder som ska skriva ut. 
    Om användaren enbart skriver in ett år ska alla länder skrivas ut.
    """
    try:
        tup_from_input = input_for_e2_e3(input_e2)
        emissions_as_list = tup_from_input[0]
        countries_by_id = tup_from_input[1]
        pop = tup_from_input[2]
        no_c = tup_from_input[3]
    except TypeError: #if there was an error in input_for_e2_e3, it returns -1 which is not subscriptable
        return

    #create a list that contains: country id, country name, country emissions in year, country pop in year
    compiled_list = []
    for i, element in enumerate(countries_by_id):
        try:
            compiled_list.append((emissions_as_list[i][0], element[0], emissions_as_list[i][1], 
            element[1]["population"][pop]))
        except IndexError: #no population available
            compiled_list.append((emissions_as_list[i][0], element[0], emissions_as_list[i][1], None))

    #create a list that contains: name, emissions per capita
    for i, element in enumerate(compiled_list):
        try:
            compiled_list[i] = (element[1], round((element[2]*1000000/element[3]), 2))
        except TypeError: #if there is no population data, write emissions per capita =-1
            compiled_list[i] = (element[1], -1)

    #sort the list by emissions per capita
    compiled_list.sort(key = lambda tup: tup[1], reverse=True)

    for i in range(no_c): #for the desired no. of countries
        if compiled_list[i][1] == -1:
            print("{c}: No population data. Can't calculate emissions per capita.".format(c=compiled_list[i][0]))
        else:
            print("{c}: {e}".format(c=compiled_list[i][0], e=compiled_list[i][1]))

def e3(input_e3):
    """
    Användaren ska skriva in ett år och få utskriften varje lands utsläpp per landyta, 
    sortera i storleksordning, avrunda till 2 decimaler. 
    Det ska även gå att skriva in hur många länder som ska skriva ut. 
    Om användaren enbart skriver in ett år ska alla länder skrivas ut.
    """
    try:
        tup_from_input = input_for_e2_e3(input_e3)
        emissions_as_list = tup_from_input[0]
        countries_by_id = tup_from_input[1]
        no_c = tup_from_input[3]
    except TypeError: #if there was an error in input_for_e2_e3, it returns -1 which is not subscriptable
        return

    #create a list that contains: country id, country name, country emissions in year, country area
    compiled_list = []
    for i, element in enumerate(countries_by_id):
        compiled_list.append((emissions_as_list[i][0], element[0], emissions_as_list[i][1], element[1]["area"]))

        #create a list that contains: name, emissions per area
    for i, element in enumerate(compiled_list):
        try:
            compiled_list[i] = (element[1], round((element[2]*1000000/element[3]), 2))
        except ZeroDivisionError: #if there is no area data, write emissions per capita =-1
            compiled_list[i] = (element[1], -1)

    #sort the list by emissions per area
    compiled_list.sort(key = lambda tup: tup[1], reverse=True)

    for i in range(no_c): #for the desired no. of countries
        if compiled_list[i][1] == -1:
            print("{c}: No area data. Can't calculate emissions per area.".format(c=compiled_list[i][0]))
        else:
            print("{c}: {e}".format(c=compiled_list[i][0], e=compiled_list[i][1]))
