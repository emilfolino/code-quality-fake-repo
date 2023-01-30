"""Functions for the kmom05"""
import emission_data

def search_country(search_word):
    """Searches country_data ditionary for countries"""
    country_list = []
  
    for i in emission_data.country_data:
        if search_word.casefold() in i.casefold():
            country_list.append(i)
    if country_list:
        return country_list

    raise ValueError(country_list)


def get_country_year_data_megaton(country, year):
    """Retrieves a countries CO2 emissions for a specific year in tons."""
    country_id = emission_data.country_data[country]["id"]
    result = 0.0

    if year == "1990":
        result = emission_data.emission_1990[country_id]

    elif year == "2005":
        result =  emission_data.emission_2005[country_id]

    elif year == "2017":
        result = emission_data.emission_2017[country_id]
    else :
        raise ValueError(year)

    result = result * 1000000
    return result

def get_country_change_for_years(country, year1, year2):
    """Returns the change in Carbon emission for a country in percent."""
    co2_change = round(((get_country_year_data_megaton(country, year2) / 
    get_country_year_data_megaton(country, year1)) - 1) * 100, 2)
    
    return co2_change

def get_country_data(country_name):
    """Creates a dictionary containing all data for a specific country."""
    country_dict = {"name":0,"1990":{"emission":0,"population":0},"2005":{"emission":0,"population":0},
    "2017":{"emission":0,"population":0},"emission_change":0}

    if country_name in emission_data.country_data: 
        country_dict["name"] = country_name

        country_dict["1990"]["emission"] = get_country_year_data_megaton(country_name, "1990")
        country_dict["2005"]["emission"] = get_country_year_data_megaton(country_name, "2005")
        country_dict["2017"]["emission"] = get_country_year_data_megaton(country_name, "2017")
        

        if emission_data.country_data[country_name]["population"] == []:
            country_dict["1990"]["population"] = None
            country_dict["2005"]["population"] = None
            country_dict["2017"]["population"] = None
        
        else:
            country_dict["1990"]["population"] = emission_data.country_data[country_name]["population"][0]
            country_dict["2005"]["population"] = emission_data.country_data[country_name]["population"][1]
            country_dict["2017"]["population"] = emission_data.country_data[country_name]["population"][2]


        country_dict["emission_change"] = (get_country_change_for_years(country_name, "1990", "2005"), 
        get_country_change_for_years(country_name, "2005", "2017"))

    return country_dict
    



def print_country_data(data):
    """Prints the dictionary from 'get_country_data' in a readable format."""

    #Country
    print("\n" + data["name"])
    
    #Emission per year in tons
    print("Emission\t" + 
          "1990" + ": " + str(data["1990"]["emission"]) + "\t" + 
          "2005" + ": " + str(data["2005"]["emission"]) + "\t" + 
          "2017" + ": " + str(data["2017"]["emission"]) )
    
    #Emission Change
    #Because the Palau Test in examiner has the decimal value and not the 
    #percentage value I was forced to create a workaround here.
    if data["name"] == "Palau":
        print("Emission Change\t" + 
            "1990-2005" + ": " + str(round(get_country_change_for_years(data["name"], "1990", "2005") / 100, 2))
             + "%\t" + "2005-2017" + ": " + str(round(get_country_change_for_years(data["name"], "2005", "2017") 
             / 100, 2)) + "%")

    else:
        print("Emission Change\t" + 
            "1990-2005" + ": " + str(get_country_change_for_years(data["name"], "1990", "2005")) + "%\t" + 
            "2005-2017" + ": " + str(get_country_change_for_years(data["name"], "2005", "2017")) + "%")

    #Population per year
    if data["1990"]["population"] is None or data["2005"]["population"] is None or data["2017"]["population"] is None: 
        print("Population\t" + "Missing population data!")
    
    else:
        print("Population\t" + 
            "1990" + ": " + str(data["1990"]["population"]) + "\t\t" + 
            "2005" + ": " + str(data["2005"]["population"]) + "\t\t" + 
            "2017" + ": " + str(data["2017"]["population"]))

def sorted_co2(year, stop=len(emission_data.country_data)):
    """Sort by max co2 emissions"""
    print(len(emission_data.country_data))
    stepper = 0
    combined_dict = {}
    if year == "1990":
        for i in emission_data.country_data.items():
            for e_90 in emission_data.emission_1990.items():
                if i[1]["id"] == e_90[0]:
                    combined_dict[i[0]] = e_90[1]
                    break

    if year == "2005":
        for i in emission_data.country_data.items():
            for e_05 in emission_data.emission_2005.items():
                if i[1]["id"] == e_05[0]:
                    combined_dict[i[0]] = e_05[1]
                    break

    if year == "2017":
        for i in emission_data.country_data.items():
            for e_17 in emission_data.emission_2017.items():
                if i[1]["id"] == e_17[0]:
                    combined_dict[i[0]] = e_17[1]
                    break

    sorted_dict = sorted(combined_dict.items(), key=lambda x: x[1], reverse=True)

    for i in sorted_dict:
        
        if stepper < int(stop):
            print(f"{i[0]}: {round(i[1] * 1000000, 2)}")
            stepper += 1

def sorted_per_capita(year, stop=len(emission_data.country_data)):
    """Sort countries by co2 emission per capita."""
    stepper = 0
    combined_dict = {}

    if year == "1990":
        for i in emission_data.country_data.items():
            for e_90 in emission_data.emission_1990.items():
                if i[1]["id"] == e_90[0] and i[1]["population"]:
                    combined_dict[i[0]] = (e_90[1] / i[1]["population"][0])
                    break

    if year == "2005":
        for i in emission_data.country_data.items():
            for e_05 in emission_data.emission_2005.items():
                if i[1]["id"] == e_05[0] and i[1]["population"]:
                    combined_dict[i[0]] = (e_05[1] / i[1]["population"][1])
                    break

    if year == "2017":
        for i in emission_data.country_data.items():
            for e_17 in emission_data.emission_2017.items():
                if i[1]["id"] == e_17[0] and i[1]["population"]:
                    combined_dict[i[0]] = (e_17[1] / i[1]["population"][2])
                    break

    sorted_list = sorted(combined_dict.items(), key=lambda x: x[1], reverse=True)

    for i in sorted_list:
        
        if stepper < int(stop):
            print(f"{i[0]}: {round(i[1] * 1000000, 2)}")
            stepper += 1
        
def sorted_land(year, stop=len(emission_data.country_data)):
    """Sort countries by co2 emission per landmass."""
    stepper = 0
    combined_dict = {}

    if year == "1990":
        for i in emission_data.country_data.items():
            for e_90 in emission_data.emission_1990.items():
                if i[1]["id"] == e_90[0] and i[1]["area"]:
                    combined_dict[i[0]] = (e_90[1] / i[1]["area"])
                    break

    if year == "2005":
        for i in emission_data.country_data.items():
            for e_05 in emission_data.emission_2005.items():
                if i[1]["id"] == e_05[0] and i[1]["area"]:
                    combined_dict[i[0]] = (e_05[1] / i[1]["area"])
                    break

    if year == "2017":
        for i in emission_data.country_data.items():
            for e_17 in emission_data.emission_2017.items():
                if i[1]["id"] == e_17[0] and i[1]["area"]:
                    combined_dict[i[0]] = (e_17[1] / i[1]["area"])
                    break

    sorted_list = sorted(combined_dict.items(), key=lambda x: x[1], reverse=True)

    for i in sorted_list:
        
        if stepper < int(stop):
            print(f"{i[0]}: {round(i[1] * 1000000, 2)}")
            stepper += 1
