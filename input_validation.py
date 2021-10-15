def validate_input(valid_type, value, difficulty):
    try:
        value = int(value)
        if valid_type == 'game':
            if 1 <= value <= 3:
                return value
            elif value == 0 or value > 3:
                raise BaseException('Please enter a valid number between 1-3!')

        if valid_type == 'difficulty':
            if 1 <= value <= 5:
                return value
            elif value == 0 or value > 5:
                raise BaseException('Please enter a valid number between 1-5!')

        if valid_type == 'memory_game':
            value = str(value)
            if len(value) == difficulty:
                return value
            elif len(value) != difficulty:
                raise BaseException('Please enter a valid number of digits-' + str(difficulty))

        if valid_type == 'guess_game':
            if 1 <= value <= difficulty:
                return value
            elif value == 0 or value > difficulty:
                raise BaseException('Please enter a valid number between 1-' + str(difficulty) + '!')
    except ValueError:
        raise ValueError('Please enter a valid number')
    except BaseException as error:
        raise BaseException(error)
