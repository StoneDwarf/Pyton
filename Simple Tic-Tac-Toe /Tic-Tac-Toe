import string


def the_game(input_storage):
    if len(input_storage) != 9:
        print("Invalid input")
        return
    marks = ('X', 'O')
    game0 = input_storage[:3]
    game1 = input_storage[3:6]
    game2 = input_storage[6:]
    game = [game0, game1, game2]
    x, o = input_storage.count('X'), input_storage.count('O')
    if abs(x - o) > 1:
        return print_game(game), print('Impossible')
    else:
        print_game(game)
        starter = 'O'
        while True:
            winner, starter = player_turn(game, marks, starter)
            if winner == 1:
                break


def player_turn(game, marks, starter):
    digits = ('1', '2', '3')
    while True:
        new_sign = list(input().replace(' ', ''))
        check = len(new_sign)
        if not new_sign:
            print('You should enter numbers!')
        elif any(number not in string.digits for number in new_sign):
            print('You should enter numbers!')
        elif check != 2:
            print('Coordinates should be from 1 to 3')
        elif any(number not in digits for number in new_sign):
            print('Coordinates should be from 1 to 3')
        elif game[int(new_sign[0]) - 1][int(new_sign[1]) - 1] in marks:
            print('This cell is occupied! Choose another one!')
        else:
            break
    if starter == 'O':
        starter = 'X'
    else:
        starter = 'O'
    game[int(new_sign[0]) - 1][int(new_sign[1]) - 1] = starter
    print_game(game)
    winner = winner_choice(game, marks)
    if not any(' ' in row for row in game) and winner != 1:
        print('Draw')
        winner = 1
    return winner, starter


def winner_choice(game, marks):
    horizontal = [row[0] for row in game if row[0] == row[1] and row[0] == row[2]]
    vertical = [game[0][x] for x in range(3) if game[0][x] == game[1][x] == game[2][x]]
    diagonal = [game[1][1] if game[1][1] == game[0][0] == game[2][2]
                or game[1][1] == game[0][2] == game[2][0] else []]
    if any(mark in marks for mark in horizontal):
        print(f'{horizontal[0]} wins')
        winner = 1
        return winner
    elif any(mark in marks for mark in vertical):
        print(f'{vertical[0]} wins')
        winner = 1
        return winner
    elif any(mark in marks for mark in diagonal):
        print(f'{diagonal[0]} wins')
        winner = 1
        return winner


def print_game(game):
    print('---------')
    for row in game:
        print(f'| {row[0]} {row[1]} {row[2]} |')
    print('---------')


input_storage = list(' ' * 9)
the_game(input_storage)
