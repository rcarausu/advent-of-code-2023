import unittest

from day_2.day_2 import find_possible_games


class TestDay2(unittest.TestCase):
    text = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
    bag = {
        'red': 12,
        'blue': 13,
        'green': 14
    }

    def test_part_1(self):
        possible_games, ignore = find_possible_games(self.text, self.bag)
        self.assertEqual(sum(possible_games), 8)

    def test_part_2(self):
        ignore, power_per_game = find_possible_games(self.text, self.bag)
        self.assertEqual(sum(power_per_game), 2286)
