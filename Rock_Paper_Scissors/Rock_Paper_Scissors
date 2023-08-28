import random

def winner_choice(player, computer): 
    choice_list = ['rock', 'paper', 'scissors', 'rock']
    winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
    if player == computer:
        return 1
    for item in  winning_cases:
        if player == item:
            if computer in winning_cases[item]:
                return 2
            else:
                return 0


def player_turn():
    player_choice = input()
    if player_choice == '!exit':
        print('Bye')
    return player_choice
  

def readname(name):
    with open('rating.txt', 'r') as rating_file:
        for line in rating_file:
            if name in line:
                player_rating = line.split(' ')[1].strip()
                return player_rating
            else:
                return '0'


#def writerating(name, win_state):
   # score = 0
    #if win_state == 1:
        #score = 50
    #elif win_state == 2:
       # score = 100
  #  updated_lines = []    
 #   with open('rating.txt', 'r') as rating_file:
  #      for line in rating_file:
  #          if name in line:
  #              parts = line.split()
  #              new_rating = int(parts[1]) + score
  #              updated_line = f'{name} {new_rating}\n'
 #               updated_lines.append(updated_line)
 #           else:
  #              updated_lines.append(line)
    
 #   with open('rating.txt', 'w') as rating_file:
  #      rating_file.writelines(updated_lines)
def rating_check(player_rating, win_state):
    score = 0
    if win_state == 1:
        score = 50
    elif win_state == 2:
        score = 100
    player_rating = str(int(player_rating) + score)
    return player_rating
    

default_options = ['rock', 'paper', 'scissors']
player_options = ['!rating', '!exit']
computer_options = None
print('Enter your name:')
name = input()
print(f'Hello, {name}')
player_rating = readname(name)
#player_rating = '0'
options_input = input()
options_list = options_input.split(',')
if not options_input:
    computer_options = default_options
else:
    computer_options = options_list
print(computer_options)
print("Okay, let's start")
player_choice = player_turn()
while player_choice != '!exit':
    computer_choice = random.choice(computer_options)
    result = [f'Sorry, but the computer chose {computer_choice}',
          f'There is a draw {computer_choice}',
          f'Well done. The computer chose {computer_choice} and failed']
    if (player_choice not in computer_options) and (player_choice not in player_options):
        print('Invalid input')
    elif player_choice == '!rating':
        print(player_rating)
    else:
        win_state = winner_choice(player_choice, computer_choice)
        player_rating = rating_check(player_rating, win_state)
        print(result[win_state])
    player_choice = player_turn()  
