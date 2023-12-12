import re


def _is_game_possible(game_record: list[str], bag: dict) -> bool:
    for record in game_record:
        record_results = record.split(',')
        for result in record_results:
            result_color = re.compile(r'[a-z]+').search(result).group()
            result_value = int(re.compile(r'[0-9]+').search(result).group())
            if result_color not in bag.keys() \
                    or result_value > bag[result_color] \
                    or result_value < 0:
                return False
    return True


def find_possible_games(games_input: str, bag: dict) -> list[int]:
    possible_games = []
    games = games_input.strip().splitlines()
    for game in games:
        game_record = game[game.find(':') + 1:].strip().split(';')
        if _is_game_possible(game_record, bag):
            game_id = re.compile(r'[0-9]+').search(game[:game.find(':')]).group()
            possible_games.append(int(game_id))
    return possible_games


if __name__ == '__main__':
    with open('day_2_input.txt', 'r') as file:
        bag = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }

        possible_games_ids = find_possible_games(file.read(), bag)

        print(possible_games_ids)
        print(sum(possible_games_ids))
