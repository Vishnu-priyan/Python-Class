def main():
    movieCollectionDict = {"Munich":[2005, "Steven Spielberg"],
                       "The Prestige": [2006, "Christopher Nolan"],
                       "The Departed": [2006, "Martin Scorsese"],
                       "Into the Wild": [2007, "Sean Penn"],
                       "The Dark Knight": [2008, "Christopher Nolan"],
                       "Mary and Max": [2009, "Adam Elliot"],
                       "The King\'s Speech": [2010, "Tom Hooper"],
                       "The Help": [2011, "Tate Taylor"],
                       "The Artist": [2011, "Michel Hazanavicius"],
                       "Argo": [2012, "Ben Affleck"],
                       "12 Years a Slave": [2013, "Steve McQueen"],
                       "Birdman": [2014, "Alejandro G. Inarritu"],
                       "Spotlight": [2015, "Tom McCarthy"],
                       "The BFG": [2016, "Steven Spielberg"]}
    promptForYear = True
    while promptForYear:
        yearChoice = int(input("Enter a year between 2005 and 2016:\n"))
        if yearChoice<2005 or yearChoice>2016:
            print("N/A")   
        else:
            for key, value in movieCollectionDict.items():
                if value[0] == yearChoice:
                    print(key + ", " + value[1])#change1
            promptForYear = False          
    menu = "MENU" \
       "\nSort by:" \
       "\ny - Year" \
       "\nd - Director" \
       "\nt - Movie title" \
       "\nq - Quit\n"
    promptUser = True
    while promptUser:
        print("\n" + menu)
        userChoice = input("Choose an option:\n")
        if userChoice == "q":
            promptUser = False
        elif userChoice=="y":
            prev_years = []
            for key, value in sorted(movieCollectionDict.items(), key=lambda item: (item[1], item[0])):
                if value[0] in prev_years:
                    print("\t"+key + ", " + str(value[1]))
                else:
                    print (value[0],end=':\n')
                    print("\t"+key + ", " + str(value[1]))
                prev_years.append(value[0])
        elif userChoice == "d":
            for key, value in sorted(movieCollectionDict.items(), key=lambda key_value: key_value[1][1]):
                print(value[1],end=':\n')
                print("\t" + key + ", " + str(value[0]))
        elif userChoice == "t":
            for key, value in sorted(movieCollectionDict.items(), key=lambda item: (item[0], item[1])):
                print(key,end=':\n')
                print("\t" + str(value[1]) + ", " + str(value[0]))
        else:
            print("Invalid input") 
main()
