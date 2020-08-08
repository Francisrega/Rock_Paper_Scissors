import sys
#from Game import Game
 
class Menu:
    def __init__(self):
        Menu()
      

      
    def mainMenu(self):
    #intro and menu
        print("Welcome to Rock, Paper, Scissors!\n")
        print("MENU")
        print("(1) See Rules")
        print("(2) Play Game")
        print("(3) Exit\n")
        choice = input("")
 
 
     #choosing which menu option 
     
        if choice == "1":
            self.rules()
        elif choice == "2":
            self.game = Game()
        else:
            sys.exit(0)
         
    #rules module    
    def rules(self):
        print("RULES")
        print("Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")

        self.Menu()
 
    def weaponMenu(self):
        print("Choose your weapon!")
        print("(1) Rock")
        print("(2) Paper")
        print("(3) Scissors")
        print("(4) Main Menu")

    def endProgram(self):
     
        end = input("Would you like to end the program? (yes or no) ")
        if end == "no":
            self.Menu()
        else:
            quit()
 
    Menu()