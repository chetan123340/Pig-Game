import random

def roll():
  start = 1
  stop = 6
  return random.randint(start , stop)

max_value = 50

while True:
  player_no = input("Enter the number of players(2-5):- ")
  if player_no.isdigit():
    player_no = int(player_no)
    if player_no<6 and player_no>=2:
      break
    else:
      print("Player number should be between 2 to 5")
  else:
    print("Invalid try again")


player_score = [0 for _ in range(player_no)]
player_index = 0
while max(player_score) < 50:
  print("\nPlayer ",player_index+1 , " turn has begun\n")
  print("Total score = ", player_score[player_index])
  score = 0
  while True:
    decision = input("Do you want to roll again(y/n): ")
    if decision.islower != 'y':
      break
 
    value = roll()
    if value == 1:
      print("You have rolled a 1. Your turn is over")



