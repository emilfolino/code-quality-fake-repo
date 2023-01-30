"""
Funktioner för emission
"""

from operator import itemgetter
import emission_data



def search_country(p_search):
    """
    Användaren ska kunna söka efter vilka länder som finns i country_data.
    Sökningen ska vara case insensitive och det ska gå att söka på hela namn
    och delar av namn. T.ex sökning på “sweden” ska skriva ut “Sweden” och
    sökning på “we” ger “Zimbabwe”, “Western Sahara” och “Sweden”.
    Sökningen ska vara case-insensitive.
    """
    p_search = p_search.lower()
    country_list = []

    for country in emission_data.country_data:
        if p_search in country.lower():
            country_list.append(country)

    if country_list == []:
        raise ValueError("Country does not exist!")

    return country_list

def get_country_year_data_megaton(country, year):
    """
    Hämta utsläppen för ett land ett visst år
    """
    dict_of_emission_data = {
        1990 : emission_data.emission_1990,
        2005 : emission_data.emission_2005,
        2017 : emission_data.emission_2017
    }
    if int(year) in dict_of_emission_data:
        country_id = emission_data.country_data[country]["id"]
    else:
        raise ValueError("Wrong year!")

    return dict_of_emission_data[int(year)][country_id] * 1000000

def get_country_change_for_years(country, year1, year2):
    """
    Förändringen av utsläpp för två år för ett land
    """
    try:
        first_year = get_country_year_data_megaton(country, year1)
    except ValueError as e:
        raise ValueError(e) from e

    try:
        second_year = get_country_year_data_megaton(country, year2)
    except ValueError as e:
        raise ValueError(e) from e

    return round(((second_year/first_year)-1)*100, 2)

def get_population(country, index):
    """
    Tar fram populationen för ett land för ett givet årsindex
    """
    if len(emission_data.country_data[country]["population"]) == 0:
        popyear = None
    else:
        popyear = emission_data.country_data[country]["population"][index]
    return popyear

def get_country_data(country_name):
    """
    Hämta data om ett land
    """

    pop1990 = get_population(country_name, 0)
    pop2005 = get_population(country_name, 1)
    pop2017 = get_population(country_name, 2)

    country_data = {
        "name" : country_name,
        "1990" : {"emission" : get_country_year_data_megaton(country_name, 1990), "population" : pop1990},
        "2005" : {"emission" : get_country_year_data_megaton(country_name, 2005), "population" : pop2005},
        "2017" : {"emission" : get_country_year_data_megaton(country_name, 2017), "population" : pop2017},
        "emission_change": (get_country_change_for_years(country_name, 1990, 2005),
                            get_country_change_for_years(country_name, 2005, 2017))
    }

    return country_data

def print_country_data(data):
    """
    Skriv ut utsläppen för ett visst land
    """

    if data["1990"]["population"] is None and data["2005"]["population"] is None and data["2017"]["population"] is None:
        pop_print = "Missing population data!"
    else:
        pop_print = "Population - 1990: " + str(data["1990"]["population"]) \
        + " 2005: " + str(data["2005"]["population"]) + " 2017: " + str(data["2017"]["population"])

    print(data["name"])
    print("Emission - 1990: " + str(data["1990"]["emission"]) \
    + " 2005: " + str(data["2005"]["emission"]) + " 2017: " + str(data["2017"]["emission"]))
    print("Emission change - 1990-2005: " + str(data["emission_change"][0]) \
    + "%" + " 2005-2017: " + str(data["emission_change"][1]) + "%")
    print(pop_print)


def emission_by_country():
    """
    Skriv ut hur mycket CO2 varje land släpper ut för ett av åren i storleks
    ordning, mest utsläpp först. Be Användaren om input där användaren
    skriver in vilket år som ska användas.
    """

    year_and_limit = input("Enter a year (1990, 2005, 2017) and a limit: ")

    year_and_limit = year_and_limit.split(" ")

    dict_of_emission_data = {
        1990 : emission_data.emission_1990,
        2005 : emission_data.emission_2005,
        2017 : emission_data.emission_2017
    }

    def function_for_emission(p_list):
        """
        Function that writes out emission and countryname
        """
        emisson_data_as_list = p_list.items()

        emission_data_sorted_on_values = sorted(emisson_data_as_list, key=itemgetter(1), reverse=True)

        counter = 0
        for id_emission, emission in emission_data_sorted_on_values:
            for country in emission_data.country_data.items():
                if id_emission == country[1]["id_emission"]:
                    emission_country = country[0]
            print(emission_country, emission)
            counter += 1
            if len(year_and_limit) == 2 and counter >= int(year_and_limit[1]):
                break

    if year_and_limit[0] == "1990":
        function_for_emission(dict_of_emission_data[1990])

    elif year_and_limit[0] == "2005":
        function_for_emission(dict_of_emission_data[2005])

    elif year_and_limit[0] == "2017":
        function_for_emission(dict_of_emission_data[2017])



def emission_per_capita():
    """
    Räkna ut emission per capita
    """
    year_and_limit = input("Enter year and limit: ")
    year_and_limit = year_and_limit.split(" ")

    dict_of_emission_data = {
        1990 : emission_data.emission_1990,
        2005 : emission_data.emission_2005,
        2017 : emission_data.emission_2017
    }

    def funt_for_emission_per_capita(p_dict, p_population_year, p_year_and_limit):

        new_dict_emission_per_capita = {}

        for id_pop, emission in p_dict.items():
            for country in emission_data.country_data.items():
                #Nedan känns tyvärr som en fullösning där jag helst hade velat
                #att den hade kollat om listan/tupeln för population inte är tom
                #men i och med att jag ser att area är 0 för de länder som saknar
                #population så gör jag på detta sätt.
                if id_pop == country[1]["id_pop"] and country[1]["area"] > 0:
                    emission_country = country[0]
                    emission_country_population = country[1]["population"][p_population_year]
                    new_dict_emission_per_capita[emission_country] = emission / emission_country_population

        emission_capita_as_list = new_dict_emission_per_capita.items()

        emission_capita_sorted = sorted(emission_capita_as_list, key=itemgetter(1), reverse=True)

        counter = 0
        for country, emission_capita in emission_capita_sorted:
            print(country, emission_capita)
            counter += 1
            if len(p_year_and_limit) == 2 and counter == int(p_year_and_limit[1]):
                break

    if year_and_limit[0] == "1990":
        funt_for_emission_per_capita(dict_of_emission_data[1990], 0, year_and_limit)

    elif year_and_limit[0] == "2005":
        funt_for_emission_per_capita(dict_of_emission_data[2005], 1, year_and_limit)

    elif year_and_limit[0] == "2017":
        funt_for_emission_per_capita(dict_of_emission_data[2017], 2, year_and_limit)



def emission_per_area():
    """
    Användaren ska skriva in ett år och få utskriften varje lands
    utsläpp per landyta, sortera i storleksordning. Det ska även gå
    att skriva in hur många länder som ska skriva ut. Om användaren
    enbart skriver in ett år ska alla länder skrivas ut.
    """

    year_and_limit = input("Enter year and limit: ")
    year_and_limit = year_and_limit.split(" ")

    dict_of_emission_data = {
        1990 : emission_data.emission_1990,
        2005 : emission_data.emission_2005,
        2017 : emission_data.emission_2017
    }


    def funt_for_emission_per_area(p_dict, p_year_and_limit):
        """
        En funktion som gör en lista och räknar ut emission per area.
        """

        new_dict_emission_per_area = {}

        for id_area, emission in p_dict.items():
            for country in emission_data.country_data.items():
                if id_area == country[1]["id_area"] and country[1]["area"] > 0:
                    emission_country = country[0]
                    emission_country_area = country[1]["area"]
                    new_dict_emission_per_area[emission_country] = emission / emission_country_area


        emission_area_as_list = new_dict_emission_per_area.items()

        emission_area_sorted = sorted(emission_area_as_list, key=itemgetter(1), reverse=True)

        counter = 0
        for country, emission_area in emission_area_sorted:
            print(country, emission_area)
            counter += 1
            if len(p_year_and_limit) == 2 and counter == int(p_year_and_limit[1]):
                break

    if year_and_limit[0] == "1990":
        funt_for_emission_per_area(dict_of_emission_data[1990], year_and_limit)

    elif year_and_limit[0] == "2005":
        funt_for_emission_per_area(dict_of_emission_data[2005], year_and_limit)

    elif year_and_limit[0] == "2017":
        funt_for_emission_per_area(dict_of_emission_data[2017], year_and_limit)
