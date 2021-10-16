import math
import random
from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
    secret_number = random.randrange(1, 100, 1)
    api = CurrencyConverter(decimal=True)
    full_result = api.convert(secret_number, 'USD', 'ILS')
    rounded_result = math.trunc(full_result)
    max_diff = rounded_result + difficulty
    min_diff = rounded_result - difficulty
    secret = [min_diff, rounded_result, max_diff, secret_number ]
    return secret


def get_guess_from_user(usd):
    guess_pending = True
    while guess_pending is True:
        try:
            guessed_number = input('Please guess how much a $' + str(usd) + ' is worth in ILS:')
            guessed_number = int(guessed_number)
            guess_pending = False
            return guessed_number
        except ValueError:
            print('Please enter a valid number')
            continue


def play(difficulty):
    secret = get_money_interval(difficulty)
    low_bar = secret[0]
    total = secret[1]
    high_bar = secret[2]
    USD = secret[3]
    guess = get_guess_from_user(USD)

    if low_bar <= guess <= high_bar or guess == total:
        print('You Won! Are you a psychic?! :)')

    elif low_bar >= guess >= high_bar or guess != total:
        print('You lost, ' + 'Answer was:', str(total) + '\nMaybe another time.')
    return
