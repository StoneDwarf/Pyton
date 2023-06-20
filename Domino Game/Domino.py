from random import choice
from collections import Counter

def deck_prepare():
    the_deck = []
    for i in range(0, 7):
        for z in range(i, 7):
            dominoe = [i, z]
            the_deck.append(dominoe)
    return the_deck


def deck_shuffle(the_deck):
    player_pieces = []
    computer_pieces = []
    while len(player_pieces) < 7:
        dominoe = choice(the_deck)
        player_pieces.append(dominoe)
        the_deck = [piece for piece in the_deck if piece not in player_pieces]
    while len(computer_pieces) < 7:
        dominoe = choice(the_deck)
        computer_pieces.append(dominoe)
        the_deck = [piece for piece in the_deck if piece not in computer_pieces]
    stock_pieces = the_deck
    return stock_pieces, computer_pieces, player_pieces


def check_double(computer_pieces, player_pieces):
    doubles_play = []
    doubles_comp = []
    for i in player_pieces:
        if i[0] == i[1] and (not doubles_play or doubles_play[0] < i[0]):
            doubles_play = i
    for i in computer_pieces:
        if i[0] == i[1] and (not doubles_comp or doubles_comp[0] < i[0]):
            doubles_comp = i
    return doubles_comp, doubles_play


def check_first(computer_pieces, player_pieces, doubles_comp, doubles_play):
    snake = []
    first_piece = (max(doubles_comp, doubles_play))
    snake.append(first_piece)
    if snake[0] == doubles_comp:
        computer_pieces.remove(snake[0])
        status = 'player'
    else:
        player_pieces.remove(snake[0])
        status = 'computer'
    return computer_pieces, player_pieces, snake, status


def player_check(snake_input): #needs check player input
    if snake_input[0] == '-':
        if snake_input[1][1] == snake[0][0]:
            check_sum = 1
        elif snake_input[1][0] == snake[0][0]:
            snake_input[1].reverse()
            check_sum = 1
        else:
            check_sum = 0
    elif snake_input[0] == '+':
        if snake_input[1][0] == snake[-1][1]:
            check_sum = 1
        elif snake_input[1][1] == snake[-1][1]:
            snake_input[1].reverse()
            check_sum = 1
        else:
            check_sum = 0
    return snake_input, check_sum


def user_input(player_pieces, stock_pieces, snake):
    user_options = [index + 1 for index, _ in enumerate(player_pieces)]
    while True:
        user_input = []
        try:
            some_input = input()
            for i in some_input:
                user_input.append(i)
            if user_input[0] == '0' and len(user_input) == 1:
                stock_pieces, random_piece = stock_check(stock_pieces)
                if len(random_piece) > 0:
                    player_pieces.append(random_piece)
                return player_pieces, stock_pieces, random_piece
            elif len(user_input) == 2 and user_input[0] == '-' and int(user_input[1]) in user_options:
                snake_input = [user_input[0]] + [player_pieces[int(user_input[1]) - 1]]
                snake_input, check_sum = player_check(snake_input)
                if check_sum == 1:
                    player_pieces.remove(snake_input[1])
                    return player_pieces, stock_pieces, snake_input
                elif check_sum == 0:
                    print('Illegal move. Please try again.')
            elif len(user_input) == 1 and int(user_input[0][0]) in user_options:
                snake_input = ['+'] + [player_pieces[int(user_input[0]) - 1]]
                snake_input, check_sum = player_check(snake_input)
                if check_sum == 1:
                    player_pieces.remove(snake_input[1])
                    return player_pieces, stock_pieces, snake_input
                elif check_sum == 0:
                    print('Illegal move. Please try again.')
            else:
                print('Invalid input. Please try again.')
        except:
            print('Invalid input. Please try again.')


def bot_piece_cash(computer_pieces, snake): #chooses which dominoes can be added to a snake
    computer_pieces = bot_logic(computer_pieces, snake)
    snake_list_input = []
    for index, item in enumerate(computer_pieces):
        if item[1] == snake[0][0] or item[0] == snake[0][0] or item[1] == snake[-1][1] or item[0] == snake[-1][1]:
            snake_list_input = item
            del computer_pieces[index]
            return  snake_list_input, computer_pieces
    return snake_list_input, computer_pieces


def bot_logic(computer_pieces, snake):
    total_list = snake + computer_pieces
    piece_summary = [inner for outer in total_list for inner in outer]
    check_list = Counter(piece_summary)
    piece_values = []
    computer_pieces = [tuple(piece) for piece in computer_pieces]
    for piece in computer_pieces:
        piece_value = check_list[piece[0]] + check_list[piece[1]]
        piece_values.append(piece_value)
    weight_list = {computer_pieces[i]: piece_values[i] for i in range(len(computer_pieces))}
    computer_pieces = sorted(computer_pieces, key=lambda x: weight_list[x], reverse=True)
    computer_pieces = [list(piece) for piece in computer_pieces]
    return computer_pieces


def stock_check(stock_pieces):
    if len(stock_pieces) >= 1:
        random_piece = choice(stock_pieces)
        stock_pieces.remove(random_piece)
    else:
          random_piece = []
    return stock_pieces, random_piece


def bot_turn(computer_pieces, snake, stock_pieces):
    wait = input()
    snake_list_input, computer_pieces = bot_piece_cash(computer_pieces, snake)
    try:
        if snake_list_input[1] == snake[0][0]:
            snake_input = ['-'] + [snake_list_input]
        elif snake_list_input[0] == snake[0][0]:
            snake_list_input.reverse()
            snake_input = ['-'] + [snake_list_input]
        elif snake_list_input[0] == snake[-1][1]:
            snake_input = ['+'] + [snake_list_input]
        elif snake_list_input[1] == snake[-1][1]:
            snake_list_input.reverse()
            snake_input = ['+'] + [snake_list_input]
        return computer_pieces, snake_input, stock_pieces
    except:
        stock_pieces, random_piece = stock_check(stock_pieces)
        if len(random_piece) > 0:
            computer_pieces.append(random_piece)
        snake_input = []
        return computer_pieces, snake_input, stock_pieces


def output(stock_pieces, computer_pieces, snake, player_pieces, status):
    print('=' * 70)
    print(f'Stock pieces: {len(stock_pieces)}\nComputer pieces: {len(computer_pieces)}\n')
    if len(snake) == 1:
        print(f'{snake[0]}\n\nYour pieces:')
    elif len(snake) <= 6:
        printable_snake = ''.join([str(item) for item in snake])
        print(f'{printable_snake}\n\nYour pieces:')
    else:
        left_snake = ''.join([str(item) for item in snake[:3]])
        right_snake = ''.join([str(item) for item in snake[-3:]])
        print(f'{left_snake}...{right_snake}\n\nYour pieces:')
    for index, piece in enumerate(player_pieces):
        print(f'{index + 1}: {piece}')


def snake_status(snake, snake_input):
    try:
        if snake_input[0] == '+':
            snake.append(snake_input[1])
        elif snake_input[0] == '-':
            snake.insert(0, snake_input[1])
        else:
            snake = snake
        return snake
    except:
        return snake


def winner_check(computer_pieces, player_pieces, snake):
    snake_len = [inner for outer in snake for inner in outer]
    if len(computer_pieces) == 0 and len(player_pieces) != 0:
        print("Status: The game is over. The computer won!")
        winner = 1
    elif len(computer_pieces) != 0 and len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        winner = 1
    elif snake_len.count(snake[0][0]) == 8 and snake_len.count(snake[-1][1]) == 8:
        print("Status: The game is over. It's a draw!")
        winner = 1
    else:
        winner = 0
    return winner


def turn_print(status):
    if status == "computer":
        print('\nStatus: Computer is about to make a move. Press Enter to continue...')
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")


def the_game(stock_pieces, computer_pieces, snake, player_pieces, status):
    output(stock_pieces, computer_pieces, snake, player_pieces, status)
    winner = 0
    while winner == 0:
        turn_print(status)
        if status == 'computer':
            computer_pieces, snake_input, stock_pieces = bot_turn(computer_pieces, snake, stock_pieces)
            status = 'player'
        else:
            player_pieces, stock_pieces, snake_input = user_input(player_pieces, stock_pieces, snake)
            status = 'computer'
        snake = snake_status(snake, snake_input)
        output(stock_pieces, computer_pieces, snake, player_pieces, status)
        winner = winner_check(computer_pieces, player_pieces, snake)


the_deck = deck_prepare()
while True:
    stock_pieces, computer_pieces, player_pieces = deck_shuffle(the_deck)
    doubles_comp, doubles_play = check_double(computer_pieces, player_pieces)
    if doubles_comp or doubles_play:
        computer_pieces, player_pieces, snake, status = check_first(computer_pieces, player_pieces, doubles_comp,
                                                                    doubles_play)
        the_game(stock_pieces, computer_pieces, snake, player_pieces, status)
        break
