import random

def roll():
  start = 1
  stop = 6
  return random.randint(start , stop)

max_value = 50

while True:
  player_no = input("Enter the number of players(2-5):- ")
  if player_no.isdigit():
    if player_no<6 and player_no>=2:
      break
    else:
      print("Player number should be between 2 to 5")