"""This is the analyzer module. it contains all the functions for analyzing a textfile"""
filename = 'phil.txt'



def read_file():
    """Read and return data from textfile."""
    with open(filename) as f:
        content = f.readlines()
    return content

def Change():
    """Changes the textfile."""
    global filename
    new_file = input('What is the name of the new file?\n')
    try:
        fh = open(new_file, 'r')
    except FileNotFoundError as message:
        print(message)
    else:
        fh.close()
        filename = new_file
    return ''

def Counters(instance):
    """Takes the user input as an argument, and counts the amount of whatever instance the user has chosen"""
    my_dict = {}
    count = 0
    file_content = read_file()
    file_content[-1] = file_content[-1].strip('\n')
    for line in file_content:
        if len(line.strip()) > 0 and instance == 'line':
            count += 1
        elif instance == 'letter':
            new_line = line.strip('\n')
            new_line = new_line.lower()
            for letter in new_line:
                if letter.isalpha() is True:
                    count += 1
                    if letter in my_dict:
                        my_dict[letter] += 1
                    else:
                        my_dict[letter] = 1
        else:
            line = line.replace('.', ' ')
            line = line.replace(',', ' ')
            line = line.lower()
            word_list = line.split()
            for word in word_list:
                count += 1
                if word in my_dict:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
    return count, my_dict

def Frequencies(choice):
    """calculates the seven most common words or letters, and a percentage"""
    count, my_dict = Counters(choice)
    sort_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]), reverse = True)
    i = 0
    result = ''
    for key, value in sort_dict:
        if i == 7:
            break
        txt = '{key:s}: {value:d} | {perc:.1f}%\n'
        result += txt.format(key = key, value = value, perc = (100*value)/count)
        i += 1
    return result

def All():
    """Calls all functions, for all instances of the function and prints the result"""
    result = ''
    for key, value in Function_Options.items():
        if key not in ('all', 'change'):
            result += str(value[0](value[1])) + '\n'
    return result

Function_Options = {
'lines' : [Counters, 'line', True],
'words' : [Counters, 'word', True],
'letters' : [Counters, 'letter', True],
'word_frequency' : [Frequencies, 'word', True],
'letter_frequency' : [Frequencies, 'letter', True],
'all' : [All, 'all', False],
'change' : [Change, 'change', False]
}

def function_call(choice):
    """Takes the user choise as amn argument and starts the corresponding function"""
    try:
        if Function_Options[choice][2]:
            result = Function_Options[choice][0](Function_Options[choice][1])
        else:
            result = Function_Options[choice][0]()
    except KeyError:
        print('Invalid input, please chose from the menu!')

    else:
        print(result)
