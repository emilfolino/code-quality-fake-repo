#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Funktioner för Mr Marvins menyval
"""
import random

def greet():
    """
    Menyval 1
    Frågar efter namn, skriver hälsning
    """
    name = input("Vad heter du? ")
    print()
    print("Mr Marvin hälsar: ")
    print(f"Hej {name}! Trevligt att råkas.")


def celcius_to_farenheit():
    """
    Menyval 2
    omvandlar celcius till farenheit
    resultatet avrundas till två decimaler
    """
    temp_C = float(input("Ange en temperatur i Celcius: "))
    temp_F = round(temp_C * 9 / 5 + 32, 2)
    print()
    print(f"Motsvarar {temp_F} grader i Fahrenheit")


def word_manipulation():
    """
    Menyval 3
    skriver ut angivet ord x antal gånger
    """
    word_in = input("Skriv ett ord. ")
    times = input("Skriv antal. ")
    print()
    print(multiply_str(word_in, times))


def sum_and_average():
    """
    Menyval 4
    beräknar summa och medelvärde
    """
    count_more = True
    counter = 0
    total_sum = 0.0
    while count_more is True:
        new_nr = input("ange tal (done för att avsluta): ")

        if new_nr == "done":
            count_more = False
        else: 
            counter += 1
            total_sum += float(new_nr)
    
    print()
    if counter > 0:
        average = round(total_sum / counter, 2)
        print(f"Summan av inlästa tal är {total_sum}")
        print(f"Antal inlästa nummer är {counter}")
        print(f"Genomsnittet av inlästa nummer är {average}")
    else:
        print("ingen beräkning kunde göras")


def hyphen_string():
    """
    Menyval 5
    upprepa bokstäver, antalet ökar för varje bokstav
    skriv inläst bokstav
    kopiera bokstaven 'i' antal gånger
    avsluta varje inläst bokstav med '-'
    """
    word_in = input("skriv in ett ord: ")

    # sista bokstaven ska inte efterföljas av '-'
    word_new = word_in[0]
    for i in range(1, len(word_in)):
        word_new += "-"
        word_new += multiply_str(word_in[i], i+1)

    print()
    print(f"nytt ord: {word_new}")

    
def is_isogram():
    """
    Menyval 6
    isogram = ord som inte innehåller dubbletter av något tecken  
    """
    word_in = input("skriv in ett ord: ")
    used_letters = ""
    isogram_word = True
    result = "Match!"

    # 'break' avslutar loopen om dubblett hittas
    for letter in word_in:
        if isogram_word is False: 
            break

        if letter in used_letters:
            result = "No match!"
            isogram_word = False
        else:
            used_letters += letter

    print()
    print(result)


def compare_numbers():
    """
    Menyval 7
    jämförelse av nummer
    """
    first_time = True
    compare_again = True
    saved_number = 0.0

    while compare_again is True:
        print()
        if first_time is True:
            print("ange första värdet ('done' för att avsluta)")
        else:
            print("skriv ett tal att jämföra med det förra ('done' för att avsluta)")

        # 'break' avslutar pågående loop
        input_str = input("--> ")
        if input_str == "done":
            compare_again = False
            break
        
        # inläst värde omvandlas till decimaltal
        try: 
            input_number = float(input_str)

        # tar hand om felaktig inmatning
        # 'continue' avslutar pågående varv i loopen
        except ValueError:
            print("not a number! Try again")
            continue

        # angivet värde jämförs med sparat värde
        # jämförelsen görs först när båda talen lästs in
        if first_time is not True:
            if input_number < saved_number:
                print("smaller!")
            elif input_number > saved_number:
                print("larger!")
            else:
                print("same!")
        # markerar att första talet är inläst
        else:
            first_time = False

        # angivet värde sparas 
        saved_number = input_number


def randomize_string(word_in):
    """
    Menyval 8
    kastar om bokstäver
    'random.randint' slumpar fram index för en bokstav i strängen
    den utvalda bokstaven flyttas till det nya ordet som skapas
    """
    result = word_in + " --> "

    # tills 'word_in' är tömd på sitt innehåll
    while word_in:
        char_index = random.randint(0, len(word_in)-1)
        result += word_in[char_index]

        # bokstaven på plats 'char_index' plockas bort
        word_in = word_in[0:char_index] + word_in[char_index+1:]
    return result

def get_acronym(word_in):
    """ 
    menyval 9
    plockar ut alla stora bokstäver ur en sträng 
    """
    word_out = ""
    for char in word_in:
        if char.isupper():
            word_out += char
    return word_out


def mask_string(word_in):
    """
    menyval 10
    maskera del av strängen
    """
    # indata för kort
    if len(word_in) <= 4:
        return word_in

    number_to_change = len(word_in) - 4
    word_out = multiply_str("#", number_to_change)
    word_out += word_in[number_to_change:]
    return word_out
 
    
def find_all_indexes(search_str, wanted_str):
    """
    menyval 11
    leta efter specificerade tecken i en sträng
    """
    result_display = ""
    search_i = 0
    end_of_search = False

    while end_of_search is not True:
        try: 
            found_i = search_str.index(wanted_str, search_i)
        except ValueError:
            end_of_search = True
            continue

        result_display += str(found_i) + ","
        search_i = found_i + 1
        
    # sista positionen ska inte med i utskriften
    result_display = result_display[0:len(result_display)-1]
    return result_display


def multiply_str(word_in, times):
    """
    skriver ut angivet ord x antal gånger
    """
    return (word_in * int(times))


def a1():
    """
    leta efter specificerade tecken i en sträng
    """
    print("vilket ord/vilka tecken vill du undersöka?")
    free_choice_word = input("-->")
    print("vilka tecken måste vara med?")
    must_have_letters = input("-->")

    # båda textsträngarna omvandlas till små bokstäver
    free_choice_word_small = free_choice_word.casefold()
    must_have_letters_small = must_have_letters.casefold()

    result = "Match!"
    for letter in must_have_letters_small:       
        if letter not in free_choice_word_small:
            result = "No match!"
    print(result)


def a2():
    """
    summerar tal och räknar ut genomsnittet
    """
    number_to_check = input("ange ett tal att multiplicera ")

    max_attempt_str = input("ange max antal försök ")
    max_attempt = int(max_attempt_str)

    must_haves = "1234567890"
    all_number_matched = False
    counter = 0

    while all_number_matched is False:
        if counter >= max_attempt:
            break

        # kontrollera att alla nummer finns representerade
        # obs! numren ligger i en sträng, konverteras vid beräkning
        error_found = False
        for number in must_haves:  

            # kontroll om numret finns med i beräknat tal  
            if number not in number_to_check:
                error_found = True

        # om fel hittats,beräkna nytt belopp  
        if error_found is True:
            new_number = int(number_to_check) * 2
            number_to_check = str(new_number)
            counter += 1
        else:
            all_number_matched = True

    # redovisa resultatet
    print()
    if all_number_matched is True:
        print(f"Answer: {counter} times") 
    else:
        print("Answer: -1 times") 

def a3():
    """
    ersätter 'tab'-tecknet med mellanslag
    """
    print('skriv ett ord som innehåller "tab"')
    input_str = input("--> ")
    output_str = ""

    # '\t' är tecknet för tab, byts till 3 blanktecken
    for letter in input_str:
        if letter == "\t":
            output_letter = "   "
        else:
            output_letter = letter
        output_str = output_str + output_letter
    
    # resultatet skrivs ut
    print(output_str)

def a4():
    """
    slå ihop två ord
    """
    separator = "aeiouy"
    output_str = ""

    # spara konsonanter fram till första vokalen
    input_str = input("första namnet: ")
    stop_searching = False

    for letter in input_str:
        if stop_searching is True:
            break

        if letter not in separator:
            output_str = output_str + letter
        else:
            stop_searching = True

    # skippa konsonanter fram till första vokalen
    # ta sedan med både vokaler och konsonater
    input_str = input("andra namnet: ")
    stop_searching = False

    for letter in input_str:
        # efter första vokalen ska alla tecken hämtas
        if stop_searching is True:
            output_str = output_str + letter
        
        # första vokalen ska med till det nya ordet
        # tecken före första konsonanten ska inte med
        elif letter in separator:
            output_str = output_str + letter
            stop_searching = True

    print(output_str)       

def a5():
    """
    räkna ut poäng för spelare
    """
    search_str = input("skriv sträng med resultat ")
    search_str_lower = search_str.lower()
    searched_player = ""
    result_display = ""
    
    # loop genom inläst resultat-lista (konverterad till små bokstäver)
    # hoppa över numeriska karaktärer
    # hoppa över spelare som redan beräknats
    for low_char in search_str_lower:
        result_sum = 0
        if low_char.isdigit():
            continue
        if low_char in searched_player:
            continue

        # räkna totalresult för aktuell spelare
        # hoppa över övriga spelare
        searched_player += low_char
        for i, player in enumerate(search_str):
            if (player != low_char) and (player != low_char.upper()):
                continue

            # konvertera resultat till int och beräkna
            result_int = int(search_str[i + 1])
            if player == low_char:
                result_sum += result_int
            else:
                result_sum -= result_int

        # lägg resultat för aktuell spelare till resultat för utskrift
        result_display += str(f"{low_char} {result_sum}, ")

    # de två sista positionerna ska inte med i utskriften
    result_display = result_display[0:len(result_display)-2]
    print(result_display)
    

def points_to_grade(max_point, point):
    """
    menyval b1
    betygsättning
    för att omvandla 0.5 till 50% används '*100'
    """
    max_point = float(max_point)
    point = float(point)
    result = point / max_point * 100

    if result >= 90:
        grade = "A"
    elif result >= 80:
        grade = "B"
    elif result >= 70:
        grade = "C"
    elif result >= 60:
        grade = "D"
    else:
        grade = "F"

    return "score: " + grade


def has_strings(total_string, start, middle, stop):
    """
    menyval b2
    kontroll av stäng
    """
    if total_string.startswith(start):
        if string_contains(total_string, middle):
            if total_string.endswith(stop):
                return "Match"
    return "No match"


def string_contains(given_word, search_word):
    """
    leta efter specificerade tecken i en sträng
    """
    if search_word in given_word:
        return True
    return False
