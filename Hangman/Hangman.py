from random import choice
import string


def library_list():
    word_list = ('python', 'java', 'swift', 'javascript')
    word = choice(word_list)
    return word


def word_checking(word, guess_list, check_word, attempts):
    if check_word not in word:
        print("That letter doesn't appear in the word.")
        attempts -= 1
    else:
        word_list = list(word)
        guess_list = list(guess_list)
        for index in range(len(word_list)):
            if check_word == word_list[index]:
                guess_list[index] = check_word
        guess_list = ''.join(guess_list)
    return guess_list, attempts


def letter_input(used_letters, check_word, word, guess_list, attempts):
    if len(check_word) != 1:
        print('Please, input a single letter')
    elif check_word not in string.ascii_lowercase:
        print('Please, enter a lowercase letter from the English alphabet.')
    elif check_word in used_letters:
        print("You've already guessed this letter.")
    else:
        used_letters += tuple(check_word)
        guess_list, attempts = word_checking(word, guess_list, check_word, attempts)
    return check_word, used_letters, guess_list, attempts


def game():
    used_letters = tuple()
    word = library_list()
    guess_list = '-' * len(word)
    attempts = 8
    while attempts > 0 and guess_list != word:
        print('')
        print(guess_list)
        print('Input a letter:')
        check_word = input()
        check_word, used_letters, guess_list, attempts = letter_input(used_letters, check_word, word, guess_list, attempts)
    else:
        if guess_list == word:
            print(f'You guessed the word {word}!\nYou survived!')
            game_stats[0] += 1
        else:
            print('You lost!')
            game_stats[1] += 1
    return game_stats


game_stats = [0, 0]
print('H A N G M A N')
while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit')
    player_choice = input()
    if player_choice == 'play':
        game_stats = game()
    elif player_choice == 'results':
        print(f'You won: {game_stats[0]} times.\nYou lost: {game_stats[1]} times.')
    elif player_choice == 'exit':
        break
