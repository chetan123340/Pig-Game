import random

def roll():
  start = 1
  stop = 6
  return random.randint(start , stop)


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


player_scores = [0 for _ in range(player_no)]
max_value = 50

while max(player_scores) < max_value:
  for player in range(player_no):
    print("\nPlayer ",player+1 , " turn has begun\n")
    print("Total score = ", player_scores[player])
    score = 0

    while True:
      decision = input("Do you want to roll again(y/n): ")
      if decision.lower() != 'y':
        break
  
      value = roll()
      if value == 1:
        print("You have rolled a 1. Your turn is over")
        score = 0
        break
      else:
        score += value
        print("You have rolled a ", value)

      print("Current Score = ", score)

    player_scores[player] += score
    print("your total score is : ", player_scores[player])
    
max_score = max(player_scores)
max_index = player_scores.index(max_score)

print("Player ", max_index+1," has won with a score of ",max_score)
