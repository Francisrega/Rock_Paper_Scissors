class Game:
  def __init__(self):
    self.player1 = None
    self.player2 = None
    self.game = game(player1, player2)



def game(player1, player2):
  if player1 == player2:
    print("It's a draw. Please try again.\n")
  elif player1 == "Rock":
    if player2 == "Scissors":
      print(player1 + " wins!\n")
    else:
      print(player2 + " wins:\n")
  elif player1 == "Paper":
    if player2 == "Scissors":
      print(player2 + " wins!\n")
    else:
      print(player1 + " wins!\n")
  elif player1 == "Scissors":
    if player2 == "Rock":
      print(player2 + " wins!\n")
    else: 
      print(player1 + " wins!\n")
def check(player1, player2):
  if player1 != "Rock" and player1 != "Paper" and player1 != "Scissors":
    print("You did not enter rock, paper or scissors. Please try again.\n")

  elif player2 != "Rock" and player2 != "Paper" and player2 != "Scissors":
    print("You did not enter rock, paper or scissors. Please try again.\n")
while True:
  player1 = str(input("Rock, Paper or Scissors?\n"))
  player2 = str(input("Rock, Paper or Scissors?\n"))

  check(player1, player2)
  game(player1, player2)
  break