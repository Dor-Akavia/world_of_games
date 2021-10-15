import random
from input_validation import validate_input


def generate_number(difficulty):
    secret_number = random.randrange(1, difficulty + 1, 1)
    return secret_number


def get_guess_from_user(difficulty):
    guess_pending = True
    while guess_pending is True:
        try:
            guessed_number = input('What is your guess?')
            user_valid_input = validate_input('guess_game', guessed_number, difficulty)
            guess_pending = False
            return user_valid_input
        except BaseException as error:
            print(error)
            continue


def compare_results(secret_number, guessed_number):
    if secret_number == guessed_number:
        return True
    elif secret_number != guessed_number:
        return False


def play(difficulty):
    secret = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    result = compare_results(secret, guess)
    if result:
        print('You Won! Are you a psychic?! :)')
    elif not result:
        print('You lost, ' + 'Secret was:', str(secret) + '\nMaybe another time.')
    return
