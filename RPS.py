#RPS.py
#Name:Ryder Anderson
#Date:02/05/2025
#Assignment:Rock Paper Scissor
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  playagain = "Y"
  while playagain == "Y":
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R" , "P" , "S"] )
    player = input("pick your weapon [R, P, S]:")
    #Prompt the user for their RPS selection

    #Determine winner and state what happened to the user
    if player == "R":
      print("player picked Rock")
    elif player == "P":
      print("player picked Paper")
    elif player == "S":
      print("player picked scissors")
    else:
      print("invalid option")
    
    if computer == "R":
      print("computer picked Rock")
    elif computer == "P":
      print("computer picked paper")
    elif computer == "S":
      print("computer picked scissors")
    else:
      print("invalid option")
    
    if player == "R" and computer == "R":
      print ("TIES")
      ties = ties + 1
    if player == "R" and computer == "P":
      print ("LOSS")
      losses = losses + 1
    if player == "R" and computer == "S":
      print ("WIN")
      wins = wins + 1

    if player == "P" and computer == "S":
      print ("LOSS")
      losses = losses + 1
    if player == "P" and computer == "P":
      print ("TIE")
      ties = ties + 1
    if player == "P" and computer == "R":
      print ("WIN")
      wins = wins + 1
    
    if player == "S" and computer == "S":
      print ("TIES")
      ties = ties + 1
    if player == "S" and computer == "R":
      print ("LOSS")
      losses = losses + 1
    if player == "S" and computer == "P":
      print ("WIN")
      wins = wins + 1

    playagain = input("Playagain (Y/N): ")

  #Ask the user if they would like to play again.
  playagain = input("play again (Y/N)")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
