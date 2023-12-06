from typing import Optional


def find_number_part_1(line: str, ignore=0) -> Optional[str]:
    for c in line:
        if c.isnumeric():
            return c
    return None


def find_number_part_2(line: str, is_reversed: bool = False) -> str:
    numbers_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    digit_option = find_number_part_1(line)
    index_digit_option = len(line) if digit_option is None else line.index(digit_option)
    text_option = None
    index_text_option = len(line)

    for text_number in numbers_map.keys():
        aux_text_number = text_number
        if is_reversed:
            aux_text_number = text_number[::-1]
        aux_index = line.find(aux_text_number)
        if aux_index != -1 and aux_index < index_text_option:
            index_text_option = aux_index
            text_option = numbers_map[text_number]
    if text_option is None or index_digit_option <= index_text_option:
        return digit_option
    return text_option


def calibrate(calibration_document: str, find_number) -> int:
    values = []
    for line in calibration_document.splitlines():
        first = find_number(line.strip())
        last = find_number(line.strip()[::-1], True)
        values.append(int(f"{first}{last}"))
    return sum(values)


if __name__ == '__main__':
    with open("input.txt", 'r') as file:
        text = file.read()
        print(calibrate(text, find_number_part_1))
        print(calibrate(text, find_number_part_2))
