import re


def _evaluate_game(game_record: list[str], bag: dict) -> tuple[bool, int]:
    is_possible = True
    minimum_bag = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for record in game_record:
        record_results = record.split(',')
        for result in record_results:
            result_color = re.compile(r'[a-z]+').search(result).group()
            result_value = int(re.compile(r'[0-9]+').search(result).group())

            if result_value > minimum_bag[result_color]:
                minimum_bag[result_color] = result_value

            if result_value > bag[result_color] \
                    or result_value < 0:
                is_possible = False

    power = minimum_bag['red'] * minimum_bag['blue'] * minimum_bag['green']

    return is_possible, power


def find_possible_games(games_input: str, bag: dict) -> tuple[list[int], list[int]]:
    possible_games = []
    power_per_game = []
    games = games_input.strip().splitlines()
    for game in games:
        game_record = game[game.find(':') + 1:].strip().split(';')
        is_possible, power = _evaluate_game(game_record, bag)
        if is_possible:
            game_id = re.compile(r'[0-9]+').search(game[:game.find(':')]).group()
            possible_games.append(int(game_id))
        power_per_game.append(power)
    return possible_games, power_per_game


if __name__ == '__main__':
    with open('day_2_input.txt', 'r') as file:
        bag = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        possible_games_ids, power_per_game = find_possible_games(file.read(), bag)

        print(sum(possible_games_ids))
        print(sum(power_per_game))
