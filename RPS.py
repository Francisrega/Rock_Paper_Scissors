#making a rock paper scissors game.

first_person = input("First players name: ")
second_person = input("Second players name: ")

def check(player1, player2):
    if player1 != "Rock" and player1 != "Paper" and player1 != "Scissors":
        print("You did not enter rock, paper or scissors. Please try again.\n")

    elif player2 != "Rock" and player2 != "Paper" and player2 != "Scissors":
        print("You did not enter rock, paper or scissors. Please try again.\n")
def game(player1, player2):
  if player1 == player2:
    print("It's a draw. Please try again.\n")
  elif player1 == "Rock":
    if player2 == "Scissors":
      print(first_person + " wins!\n")
    else:
      print(second_person + " wins:\n")
  elif player1 == "Paper":
    if player2 == "Scissors":
      print(second_person + " wins!\n")
    else:
      print(first_person + " wins!\n")
  elif player1 == "Scissors":
    if player2 == "Rock":
      print(second_person + " wins!\n")
    else: 
      print(first_person + " wins!\n")

while True:
  player1 = str(input("Rock, Paper or Scissors?\n"))
  player2 = str(input("Rock, Paper or Scissors?\n"))

  check(player1, player2)
  game(player1, player2)
  break