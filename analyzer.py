#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Funktioner för analys av texter
"""
# import av de moduler som behövs
from operator import itemgetter

def change():
    """
    byte av infil
    """
    return input("namn på önskad fil --> ")

def init_incoming_data(filename):
    """
    öppnar och läser infilen
    initierar listor med rader, ord och bokstäver
    returnerar dictionary med initierade listorna
    """
    try:
        with open(filename, "r") as f:
            file = f.read().strip()
    except FileNotFoundError:
        print("fil saknas, ange ny fil eller fortsätt med tidigare ")
        return None

    data_dict = init(file)
    return data_dict

def init(file):
    """
    delar upp indata i rader, ord och bokstäver
    returnerar dictionary med tre listor
    """
    # alla tecken ska vara lower (små bokstäver)
    file = file.lower()
    
    # rader delas av vid radbryt
    data_dict = {}
    list_line = []
    split_line = file.split("\n")

    for line in split_line:
        list_line.append(line)

    data_dict["dict_lines"] = list_line

    # ord delas av vid mellanslag
    list_word = []
    for line in list_line:
        split_word = line.split(" ")

        for word in split_word:
            word = clean(word)
            list_word.append(word)

    data_dict["dict_words"] = list_word

    # varje bokstav för sig
    list_letter = []
    for word in list_word:
        for letter in word:
            list_letter.append(letter)

    data_dict["dict_letters"] = list_letter
    return data_dict

def clean(item):
    """
    tar bort tecken som inte ska vara med i statistiken
    """
    unwanted = (".", ",", "!", "-")
    for take_away in unwanted: 
        item = item.replace(take_away, "")
    return item

def lines(list_line):
    """
    returnerar antal rader i indata
    """
    return len(list_line)

def words(list_word):
    """
    returnerar antal ord i indata
    """
    return len(list_word)

def letters(list_letter):
    """
    returnerar antal bokstäver i indata
    """
    return len(list_letter)

def word_frequency(list_word): 
    """
    statistik för ord
    """  
    # skapar statistik för förekomst av ord
    list_stat = create_statistic(list_word, 7)

    # hämtar totala mängden ord 
    total = words(list_word)

    # räknar ut procent, skapar utskriftsrader
    return create_output_line(list_stat, total)

def letter_frequency(list_letter):
    """
    statistik för bokstäver
    """
    list_stat = create_statistic(list_letter, 7)

    # hämtar totala mängden bokstäver
    total = letters(list_letter)

    # räknar ut procent, skapar utskriftsrader
    return create_output_line(list_stat, total)

def create_statistic(list_input, choosen_nr): 
    """
    statistik för ord eller bokstäver
    """  
    # räknar antal förekomster av varje ord/bokstav
    list_stat = {}
    for item in list_input:
        list_stat = add_statistic(list_stat, item)

    # sortering på antal förekomster, skapar en lista 
    sorted_stat = sorted(list_stat.items(),
                        key=itemgetter(1),
                        reverse=True)

    # hämtar den sista raden som ska vara med (brytpunkt)
    # hämtar alla rader med samma antal som brytpunkten
    # dessa måste sorteras inbördes
    border_value = sorted_stat[choosen_nr - 1]
    list_second_sorting = get_same_value(sorted_stat, border_value)

    # sparar index för de platser i den totala listan som påverkas
    # tar bort dessa index från listan som ska sorteras
    change_places_i = save_the_place(list_second_sorting)
    list_second_sorting = remove_index(list_second_sorting)

    # utvalda rader sorteras på ord/bokstav 
    # de sorterade raderna läggs tillbaka i den totala listan
    list_second_sorting = sorted(list_second_sorting, reverse=True)
    first_i = change_places_i[0]
    last_i = change_places_i[1]
    sorted_stat[first_i:last_i] = list_second_sorting

    # returnerar önskat antal rader
    return sorted_stat[:choosen_nr]

def create_output_line(input_list, total):
    """
    räknar ut procent för varje ord/bokstav
    lägger utskriftsraderna i en lista
    """
    output_lines = []
    for item in input_list:
        percent = calc_percent(item[1], total)
        line = (f"{item[0]}: {item[1]} | {percent}%")
        output_lines.append(line)
    return output_lines

def add_statistic(dict_stat, stat_key):
    """
    skapar statistik för ord/bokstäver från indata
    """
    try:
        dict_stat[stat_key] += 1
    except KeyError:
        dict_stat[stat_key] = 1
    return dict_stat

def save_the_place(list_input):
    """
    sparar index för de platser som påverkas
    """
    first_i = list_input[0][0]
    last_i = list_input[len(list_input)-1][0]
    return(first_i, last_i)

def get_same_value(input_list, input_value):
    """
    hämtar alla rader med samma antal som brytpunktens
    dessa måste sorteras inbördes
    value[0] = ord/bokstav
    value[1] = antal förekomster
    """
    list_second_sorting = []
    for i, value in enumerate(input_list):
        if value[1] == input_value[1]:
            same_value = (i, value[0], value[1])
            list_second_sorting.append(same_value)
    return list_second_sorting

def remove_index(input_list):
    """
    tar bort nuvarande index från listan som ska sorteras
    """
    for i, value in enumerate(input_list):
        value = (value[1], value[2])
        input_list[i] = value
    return input_list

def calc_percent(part, total):
    """
    beräknar procent
    """
    return round(float(part / total * 100), 1)

def execute_all(data_dict):
    """
    anropar alla övriga funktioner 
    anropar funktion som skriver ut
    """
    output_list = []
    output_list.append(lines(data_dict["dict_lines"]))
    output_list.append(words(data_dict["dict_words"]))
    output_list.append(letters(data_dict["dict_letters"]))
    output_list.append(word_frequency(data_dict["dict_words"]))
    output_list.append(letter_frequency(data_dict["dict_letters"]))
    return output_list

def output(list_input):
    """
    sköter utskrift listor
    """
    for line in list_input:
        if isinstance(line, list):
            for detail_line in line:
                print(detail_line)
        else: 
            print(line)

# används vid test av enbart denna modul
# exekveras inte när modulen importeras till annan fil
if __name__ == "__main__":
    print(change())
