import json
import sys

class Game:
  def __init__(self):
    self.player1 = None
    self.player2 = None
    self.results = []

  def playGame(self, player1, player2):
    
    self.check(player1, player2)
    self.game(player1, player2)
    
    

   
  def game(self, player1, player2):
    if player1 == player2:
      print("It's a draw. Please try again.\n")
      self.results.append("Draw")
    elif player1 == "rock":
      if player2 == "scissors":
        print(player1 + " wins!\n")
        to_appened = f"player1 played {player1}"
        self.results.append(to_appened)
      else:
        print(player2 + " wins:\n")
        to_appened = f"player2 played {player2}"
        self.results.append(to_appened)
        
    elif player1 == "paper":
      if player2 == "scissors":
        print(player2 + " wins!\n")
        to_appened = f"player2 played {player2}"
        self.results.append(to_appened)
        
      else:
        print(player1 + " wins!\n")
        
        to_appened = f"player1 played {player1}"
        self.results.append(to_appened)

    elif player1 == "scissors":
      if player2 == "rock":
        print(player2 + " wins!\n")
        
        to_appened = f"player2 played {player2}"
        self.results.append(to_appened)
      else: 
        print(player1 + " wins!\n")
        to_appened = f"player1 played {player1}"
        self.results.append(to_appened)

        
  def check(self, player1, player2):
    if player1 != "rock" and player1 != "paper" and player1 != "scissors":
      print("You did not enter rock, paper or scissors. Please try again.\n")
      return
  
  def showResults(self):
    for x in self.results:
      print (x)

  def save(self, results):
    with open("game_results.json", "w") as output_file:
      new = json.dumps(results,default=lambda o: o.__dict__, sort_keys=True, indent= 4)
      json.dump(new, output_file)
  
  def quit(self):
    all_results = self.results
    choice = input("Would you like to save all changes (y/n): ")
    if choice == 'y' or choice== 'Y':

      self.save(all_results)
    sys.exit(0)


 
   