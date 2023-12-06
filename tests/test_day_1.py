import unittest

from src.day_1.day_1 import calibrate, find_number_part_1, find_number_part_2


class TestDay1(unittest.TestCase):
    def test_part_1(self):
        text = """1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet"""
        self.assertEqual(calibrate(text, find_number_part_1), 142)

    def test_part_2(self):
        text = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"""

        self.assertEqual(calibrate(text, find_number_part_2), 281)
