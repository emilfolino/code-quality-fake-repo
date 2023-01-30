"""
    Text analyzer
"""
import menu
import analyzer


def main():
    """
    Main program of analyzer
    """
    file_to_use = "phil.txt"
    menu.the_menu()
    analyzer_on = True
    while analyzer_on:
        
        choice = input("What do you want to do: ")

        if choice == 'q':
            analyzer_on = False
        
        if choice == 'menu':
            menu.the_menu()
        
        if choice == 'lines':
            try:
                to_print = analyzer.lines(file_to_use)
                print(to_print)
            except FileNotFoundError:
                continue
        
        if choice == 'letters':
            try:
                to_print = analyzer.letters(file_to_use)
                print(to_print)
            except FileNotFoundError:
                continue
            
        if choice == 'words':
            try:
                to_print = analyzer.words(file_to_use)
                print(to_print)
            except FileNotFoundError:
                continue
        
        if choice == 'word_frequency':
            try:
                analyzer.word_frequency(file_to_use)
            except FileNotFoundError:
                continue
        
        if choice == 'letter_frequency':
            try:
                analyzer.letter_frequency(file_to_use)
            except FileNotFoundError:
                continue
        
        if choice == 'all':
            try:
                analyzer.print_all(file_to_use)
            except FileNotFoundError:
                continue
        if choice == "change":
            new_file = input("Enter Filename: ")
            file_to_use = new_file
if __name__ == "__main__":
    main()
