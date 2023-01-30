"""
Module for displaying menu
"""


from analyzer import count_lines, count_words, count_letters, word_frequency,\
     letter_frequency, calculate_all, change_file


def menu_text():
    """
    Displays menu text
    """
    print("""
---------------------------------------
Program to analyze text in file.
---------------------------------------

lines) Calculate amount of lines.
words) Calculate amount of words.
letters) Calculate amount of letters.
all) Calculates all categories.
change) Cange text file.

q) Quit.
    """)

def main():
    """
    Contains loop for program
    """

    file_name = "phil.txt"
    
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        menu_text()
        choice = input("Enter your choice: ")
        if choice == "lines":
            print(count_lines(file_name))
        elif choice == "words":
            print(count_words(file_name))
        elif choice == "letters":
            print(count_letters(file_name))
        elif choice == "word_frequency":
            word_frequency(file_name)
        elif choice == "letter_frequency":
            letter_frequency(file_name)
        elif choice == "all":
            calculate_all(file_name)
        elif choice == "change":
            request = input("Enter file name: ")
            try:
                change_file(request)
                file_name = request
                print(f"Success! Now reading from {request}")
            except FileNotFoundError:
                print("Can't open file.")

        elif choice == "q":
            break
        else:
            print("That's not a valid option.")
        input("\nPress enter to continue.")
