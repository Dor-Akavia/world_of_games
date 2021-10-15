import random
import sys
import time
from input_validation import validate_input


def generate_sequence(difficulty):
    sequence_string = ''
    for i in range(0, difficulty):
        n = str(random.randint(1, 10))
        sequence_string = n + sequence_string

    sys.stdout.write(sequence_string)
    time.sleep(0.7)
    for x in sequence_string:
        sys.stdout.write('\b \b')

    return sequence_string


def get_list_from_user(difficulty):
    guess_pending = True
    while guess_pending is True:
        try:
            guessed_sequence = input('Please enter the right sequence:')
            user_valid_input = validate_input('memory_game', guessed_sequence, difficulty)
            guess_pending = False
            return user_valid_input
        except BaseException as error:
            print(error)
            continue


def is_list_equal(secret_sequence, guessed_sequence):
    if secret_sequence == guessed_sequence:
        return True
    elif secret_sequence != guessed_sequence:
        return False


def play(difficulty):
    secret = generate_sequence(difficulty)
    guess = get_list_from_user(difficulty)
    result = is_list_equal(secret, guess)
    if result:
        print('You Won! Are you a psychic?! :)')
    elif not result:
        print('You lost, ' + 'Answer was:', str(secret) + '\nMaybe another time.')
    return
