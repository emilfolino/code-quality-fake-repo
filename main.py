'''This is code for the chatbot Marvin'''
import marvin as m
import inventory as i
import emission_functions as e
    
def main():
    '''
    docsstring
    '''
    #running = True
    backpack = []
    while True:
        print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        m.chat()
        print( "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        choise = input("Hej: ")
        choiselist = choise.split()

        if choise == "1":
            m.greet()

        elif choise == "2":
            temp = int( input( "Vad vill du transformera? ") )
            m.celcius_to_farenheit( temp )

        elif choise == "3":
            word = str( input( "Vilket ord vill du manipulera? " ) )
            count = int( input( "Hur många gånger vill du läsa upp ordet? " ) )
            m.word_manipulation( word, count )

        elif choise == "4":
            m.sum_and_average()

        elif choise == "5":
            string = str( input( "Vilket ord vill du hyphen? " ) )
            m.hyphen_string( string )

        elif choise == "6":
            string = str( input( "Skriv in vad du vill kolla om det är ett isogram " ) )
            m.is_isogram( string )

        elif choise == "7":
            num_list = []
            num_run = True
            print( "Skriv in nummret 0 för att avsluta")
            while num_run:
                n = int( input( "Välj ett nummer " ) )
                if n == "0":
                    num_run = False
            m.compare_numbers( num_list )

        elif choise == "8":
            '''
            string_randomizer
            '''
            string = input("Enter a string to randomize: ")
            svar = m.randomize_string(string)
            print(svar)

        elif choise == "9":
            '''
            acronym generator
            '''
            string = input("Give me a word, both upper and lower case letters " )
            print(m.get_acronym(string))

        elif  choise == "10":
            '''
            string masker
            '''
            args = input("Give me a word to mask: ")
            print(m.mask_string(args))
            
        elif choise == "11":
            '''
            Shows how many indexes
            '''
            arg1 = input("First string: ")
            arg2 = input("String to look for: ")
            
            print(m.find_all_indexes(arg1, arg2))
        
        elif choise == "12":
            '''
            country finder
            '''

            country = input("Search for a country ")
            try:
                results = e.search_country(country)
                print("Following countries were found: " + ", ".join(results))
            except ValueError:
                print("Country does not exist!")
            

        elif choise == "13":
            '''
            emisiosn change
            '''

            search = input("Enter country year and year: ")

            search_split = search.split(",")
            try:
                resultat = e.get_country_change_for_years(search_split[0], search_split[1], search_split[2])
                print(f"{search_split[0]}:{resultat}% ")
            except ValueError:
                print("Country does not exist!")
            
            

        elif choise == "14":
            '''
            show all data
            '''
            land = input("Show data for a country: ")
            data = e.get_country_data(land)
            if data is not None:
                e.print_country_data(data)
            else:
                print("Invalid country")
        elif choise in ( 'q', 'Q' ):
            break

        else:      
            print( "Det var inte ett valid input. prova igen. " )

        try:
            if choiselist[0] == "inv": 
                if len(choiselist) == 1:
                    i.inventory(backpack)
                elif choiselist[1] == "pick":
                    '''
                    picker
                    '''
                    if len(choiselist) == 3:
                        i.pick(backpack,choiselist[2])
                    if len(choiselist) == 4:
                        i.pick(backpack,choiselist[2],int(choiselist[3]))
                elif choiselist[1] == "drop":
                    if len(choiselist) == 3:
                        i.drop(backpack, choiselist[2])
                elif choiselist[1] == "swap":
                    if  len(choiselist) == 4:
                        i.swap(backpack, choiselist[2], choiselist[3])
        except IndexError:
            print ("Try again")
                        
                    
                        
                



            
                
            

       

if __name__ == "__main__":
    main()
