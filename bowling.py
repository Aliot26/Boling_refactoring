game_list = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
max_score = 10
char_I = '/'
char_X = 'X'
char_x = 'x'


def score(game):
    result = 0
    frame = 1
    last = 0
    in_first_half = True
    for i in range(len(game)):
        if game[i] == char_I:
            result += max_score - last
        else:
            result += get_value(game[i])

        if frame < max_score and get_value(game[i]) == max_score:
            result = calculate_result(game, result, i)

        last = get_value(game[i])

        if not in_first_half:
            frame += 1
        in_first_half = reverse(in_first_half)

        if game[i] == char_X or game[i] == char_x:
            in_first_half = True
            frame += 1
    return result


def calculate_result(game, result, i):
    result += get_value(game[i+1])
    if game[i] == char_X or game[i] == char_x:
        if game[i+2] == char_I:
            result += max_score - get_value(game[i+1])
        else:
            result += get_value(game[i+2])
    return result


def reverse(flag):
    if flag:
        return False
    return True


def get_value(char):
    if char in game_list:
        return int(char)
    elif char == char_X or char == char_x or char == char_I:
        return max_score
    elif char == '-':
        return 0
    else:
        raise ValueError()
