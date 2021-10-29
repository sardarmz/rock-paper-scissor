import random

from config import GAME_CHOICES, RULES, scoreboard


def user_choice():
    user_input = input("Enter your choice please (r, p, s): ")
    if user_input not in GAME_CHOICES:
        print('Oops! wrong choice, try again please...')
        return user_choice()
    return user_input


def system_choice():
    """system select random from (r, p, s)"""
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    match = {user, system}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
    else:
        scoreboard['system'] += 1

    print('*' * 20)
    print('*' * 20)
    print(f'user: {scoreboard["user"]}'.ljust(16), '**')
    print(f'system: {scoreboard["system"]}'.ljust(16), '**')
    print('*' * 20)
    print('*' * 20)


def play():
    result = {'user': 0, 'system': 0}

    while result['user'] < 3 and result['system'] < 3:
        user_select = user_choice()
        system_select = system_choice()
        winner = find_winner(user_select, system_select)

        if winner == user_select:
            result['user'] += 1
            msg = 'You win'
        elif winner == system_select:
            result['system'] += 1
            msg = 'You lose'
        else:
            msg = 'Draw'
        print(f'user : {user_select}\nsystem : {system_select}\nresult : {msg}')

    update_scoreboard(result)

    play_again = input('Do you want to play again ? (y/n)')
    if play_again == 'y':
        play()


if __name__ == '__main__':
    play()
