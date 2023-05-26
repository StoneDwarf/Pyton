import random

def starting_input():
  while True:
      try:
          pencil = int(input())
          if pencil <= 0:
              print('The number of pencils should be positive')
          else:
              break
      except ValueError:
          print('The number of pencils should be numeric')
  return pencil


def player_choice():
  players = ['John', 'Jack']
  player = input()
  while player not in players:
      print("Choose between 'John' and 'Jack'")
      player = input()
  return (player)


def player_turn():
  global pencil
  while True:
      new_pencil = input()
      if new_pencil not in ['1', '2', '3']:
          print("Possible values: '1', '2' or '3'")
      elif pencil < int(new_pencil):
          print('Too many pencils were taken')
      else:
          return int(new_pencil)
          break


def bot_turn():
  global pencil
  if pencil > 4 and pencil % 4 == 1:
      bot_pencil = random.choice([1, 2, 3])
  elif pencil >= 4 and pencil % 4 == 0:
      bot_pencil = 3
  elif pencil > 4 and pencil % 4 == 3:
      bot_pencil = 2  
  elif pencil == 3:
      bot_pencil = 2 
  else:
      bot_pencil = 1
  print(bot_pencil)
  return bot_pencil


print('How many pencils would you like to use:')
pencil = starting_input()
print('Who will be the first (John, Jack):')
player = player_choice()


while pencil != 0:
    print('|' * pencil) 
    if player == 'John':
        print("John's turn:")
        pencil -= int(player_turn())
        player = 'Jack'      
    elif player == 'Jack':
        print("Jack's turn:") 
        pencil -= bot_turn()
        player = 'John'    
else:      
    if player == 'John':
        print("John won!")
    else:
        print("Jack won!")
