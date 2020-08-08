from random import randint
 
 
def mainMenu():
    #intro and menu
    print("Welcome to Rock, Paper Scissors!\n")
    print("MENU")
    print("(1) See Rules")
    print("(2) Single Player")
    print("(3) Two Player")
    print("(4) Exit\n")
 
    #choosing which menu option 
    choice = input("")
     
    if choice == "1":
        print(rules())
    elif choice == "2":
        singlePlayer()
    elif choice == "3":
        twoPlayer()
    elif choice == "4":
        endProgram()
         
    #rules module    
def rules():
    print("RULES")
    print("Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")
     
    mainMenu()
 
def weaponMenu():
    print("Choose your weapon!")
    print("(1) Rock")
    print("(2) Paper")
    print("(3) Scissors")
    print("(4) Main Menu")

def endProgram():
     
    end = input("Would you like to end the program? (yes or no) ")
    if end == "no":
        mainMenu()
    else:
        quit()
 
mainMenu()