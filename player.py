def singlePlayer():
 
    #create a list of play options
    moves = ["rock", "paper", "scissors"]
  
    #assign a random play to the computer
    computer = moves[randint(0,2)]
  
    #set player to False
    player = False
 
    while player == False:
    #set player to True
     player = input("Choose rock, paper, or scissors! ")
    if player == computer:
      print("Tie!")
      print(score)
                 
    elif player == "rock":
      if computer == "paper":
        print("You lose!", computer, "covers", player)
      computerScore = computerScore + 1
      print(score)
      return computerScore
    else:
      print("You win!", player, "smashes", computer)
    
    elif player == "paper":
     if computer == "scissors":
        print("You lose!", computer, "cut", player)
      else:
        print("You win!", player, "covers", computer)
      elif player == "scissors":
      if computer == "rock":
        print("You lose...", computer, "smashes", player)
      else:
        print("You win!", player, "cut", computer)
      else:
        print("That's not a valid play. Check your spelling!")
 
 
def twoPlayer():
    print("Choose Rock Paper or Scissors, try to hide your choice!\n")
    player1 = input("Player 1 : ")
    player2 = input("Player 2 : ")
    print("")
     
 
    if (player1 == 'rock' and player2 == 'scissors'):
      print ("Player 1 wins.")
 
    elif (player1 == 'rock' and player2 == 'rock'):
      print ("Tie")
 
    elif (player1 == 'scissors' and player2 == 'paper'):
      print ("Player 1 wins.")
 
    elif (player2 == 'scissors' and player2 == 'scissors'):
      print ("Tie")
 
    elif (player1 == 'paper' and player2 == 'paper'):
      print ("Tie")
 
    elif (player1 == 'paper' and player2 == 'scissors'):
      print ("Player 2 wins.")
 
    elif (player1 == 'rock'and player2 == 'paper'):
      print ("Player 2 wins.")
 
    elif (player1 == 'paper' and player2 == 'rock'):
      print ("Player 1 wins.")
 
    elif (player1 == 'scissors' and player2 == 'rock'):
      print ("Player 2 wins.")
 