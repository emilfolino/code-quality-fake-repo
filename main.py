"""skall enbart innehålla kommandoloopen"""

import menu
import analyzer


def main():
    """Main function calling different functions"""
    file_name = "phil.txt"
    not_done = True
    while not_done:
        # Open textfile
        all_data = analyzer.file_opener(file_name)

        # Print and choose option
        menu.printmenu(file_name)       
        choice = input("What would you like to do? ")

        # Menu options
        if choice == "q":
            not_done = False

        elif choice == "lines":
            analyzer.line_count(all_data)

        elif choice == "words":
            print(analyzer.word_count(all_data))

        elif choice == "letters":
            print(analyzer.letter_count(all_data))

        elif choice == "word_frequency":
            analyzer.word_frequency(all_data)

        elif choice == "letter_frequency":
            analyzer.letter_frequency(all_data)

        elif choice == "all":
            analyzer.do_all(all_data)

        elif choice == "change":
            old_file_name = file_name
            file_name = input("Enter new filename: ")
            all_data = analyzer.file_opener(file_name)
            if all_data is None:
                print("Not a valid name, try again!")
                file_name = old_file_name
                
        else:
            print("Not a valid choice")


if __name__ == "__main__":
    main()
    