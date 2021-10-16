from input_validation import validate_input
from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
from CurrencyRouletteGame import play as play_currency_roulette_game


def welcome(name):
    game_text = 'Hello ' + name + ' and welcome to the World of Games (WoG).\nHere you can find many cool games to ' \
                                  'play. '
    print(game_text)
    game_text = 'Please choose a game to play:\n 1. Memory Game - a sequence of numbers will appear for 1 second and ' \
                'you have to guess it back\n 2. Guess Game - guess a number and see if you chose like the computer\n ' \
                '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n Enter game number ' \
                'here: '
    game_pending = True
    while game_pending is True:
        try:
            game_option = input(game_text)
            chosen_game = validate_input('game', game_option, 0)
            game_pending = False
        except BaseException as error:
            print(error)
            continue

    difficulty_pending = True
    while difficulty_pending is True:
        try:
            difficulty = input('Please choose game difficulty from 1 to 5:')
            chosen_difficulty = validate_input('difficulty', difficulty, 0)
            difficulty_pending = False
            load_game(chosen_game, chosen_difficulty)
            return
        except BaseException as error:
            print(error)
            continue


def load_game(chosen_game, chosen_difficulty):
    if chosen_game == 1:
        play_memory_game(chosen_difficulty)
    if chosen_game == 2:
        play_guess_game(chosen_difficulty)
    if chosen_game == 3:
        play_currency_roulette_game(chosen_difficulty)





