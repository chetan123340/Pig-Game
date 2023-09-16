import random

def roll():
  start = 1
  stop = 6
  return random.randint(start , stop)

print(roll())