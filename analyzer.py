"""
Text file analyzing
"""
import menu

def textanalyzer(choice):
    """
    Text analyzer
    """
    with open(menu.textfile, "r", encoding="utf-8") as filehandle:
        content = filehandle.read()
    file = ''.join(content)

    if choice == "letters":
        avoid = [" ", ".", ",", "-", "\n"]
        letters = len(file)
        for letter in file:
            if any(char in letter for char in avoid):
                letters -= 1
            else:
                pass
        return letters

    if choice == "words":
        words = 0
        for letter in file:
            #if letter == " " or letter == "\n":
            if letter in (" ", "\n"):
                words += 1
            else:
                pass
        return words + 1 #1-an är det sista ordet eftersom ordet inte har varken mellanrum eller endline

    if choice == "lines": #pylint: disable=no-else-return
        lines = 0
        for line in file:
            if line == "\n":
                lines += 1
            else:
                pass
        return lines + 1 #1-an är sista raden eftersom den inte har \n

    else:
        return("Wrong input")

def word_frequency(choice):
    """
    Word frequency
    """
    if choice == "word_frequency":
        with open(menu.textfile, "r", encoding="utf-8") as filehandle:
            content = filehandle.read()
            content = content.lower()
            content_list = content.split()
            updated_list = []
            result_dict = {}
            sorted_dict = []
            list1 = []

            for words in content_list:
                avoid = [" ", ".", ","]
                if any(char in words for char in avoid):
                    updated_list.append(words[:-1])
                else:
                    updated_list.append(words)

            result = sorted(updated_list, key = updated_list.count, reverse = True)

            for item in result:
                if item not in result_dict:
                    result_dict[item] = 1
                else:
                    result_dict[item] += 1

            #sorted_dict = sorted(result_dict, key=result_dict.get, reverse=True)
            sorted_dict = dict(sorted(result_dict.items(), key=lambda i: (i[1],i[0]), reverse=True))
            for value in sorted_dict:
                number = result_dict[value]
                list1.append(f"{value}: {number} | {round(((number/len(updated_list)) * 100), 1)}%\n")

            list1 = list1[:7]
            list1 = "".join(list1)
            list1 = list1[:-1]

        return list1

    if choice == "letter_frequency": #pylint: disable=no-else-return
        """
        Letter frequency
        """
        with open(menu.textfile, "r", encoding="utf-8") as filehandle:
            content = filehandle.read()
            content = content.lower()
            updated_content = []
            updated_dict = {}
            sorted_dict = []
            list1 = []
            
            for char in content:
                avoid = [" ", ".", ",", "-", "\n"]
                if any(word in char for word in avoid):
                    pass
                else:
                    updated_content.append(char)
                
            for item in updated_content:
                if item not in updated_dict:
                    updated_dict[item] = 1
                else:
                    updated_dict[item] += 1
            
            #sorted_dict = sorted(updated_dict, key=updated_dict.get, reverse = True)
            sorted_dict = dict(sorted(updated_dict.items(), key=lambda i: (i[1],i[0]), reverse=True))
            for value in sorted_dict:
                number = updated_dict[value]
                list1.append(f"{value}: {number} | {round(((number/len(updated_content)) * 100), 1)}%\n")
            
            list1 = list1[:7]
            list1 = "".join(list1)
            
        return list1

    else:
        return("Wrong input")

def totalanalyzer():
    """
    All of the analysis
    """
    numbers = []
    numbers.append(str(textanalyzer("letters")))
    numbers.append(str(textanalyzer("words")))
    numbers.append(str(textanalyzer("lines")))
    
    sortednumbers = sorted(numbers)
    
    sortednumbers = "\n".join(sortednumbers)

    print(sortednumbers)
    print(word_frequency("word_frequency"))
    print(word_frequency("letter_frequency"))

def change():
    """
    Change text file
    """
    textfile = input("Type the name of the text file: ")
    return textfile
