import sys
from Game import Game
 
class Menu:
    def __init__(self):
        self.app = Game()
        self.options = {

      "1": self.playgame,

      "2": self.rules,

      "3": self.weaponMenu,

      "4": self.showResults,

      "5": self.endProgram


    }
      

    def display_options(self):

        print(""" 
                ************* MAIN MENU *************
                Rock Paper Scissors !!! 

                Please choose one of the options below:
    
                1. Play Game
    
                2. See Rules
    
                3. View Weapons 

                4. Show game results

                5. Quit
                   
                """)




    def playgame(self):
        player1 = str(input("Rock, Paper or Scissors?\n")).lower()
        player2 = str(input("Rock, Paper or Scissors?\n")).lower()
        self.app.playGame(player1, player2)

    def rules(self):
        print("RULES")
        print("Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")

 
    def weaponMenu(self):
        print("Your weapons !!!")
        print("(1) Rock")
        print("(2) Paper")
        print("(3) Scissors")
    
    def showResults(self):
        self.app.showResults()
        

    def endProgram(self):
        self.app.quit()
     
       
    
    def run(self):

        while True:
            self.display_options()
            option = input("Enter an option: ")
            action = self.options.get(option)

            if action:
                action()
            else:
                print("{0} is not a valid option, Please try again".format(option))