WORD_TO_DIGIT_MAP = {
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


def calibrate_value_for_words(line: str) -> int:
    positions = [
        (idx, digit)
        for word, digit in WORD_TO_DIGIT_MAP.items()
        for idx in range(len(line)) if line.startswith(word, idx)
    ]
    positions.extend((idx, ch) for idx, ch in enumerate(line) if ch.isdigit())
    if not positions:
        return 0
    positions.sort(key=lambda x: x[0])
    first, last = positions[0][1], positions[-1][1] if len(positions) > 1 else positions[0][1]
    return int(first + last)


def sum_calibration_values_for_words(lines) -> int:
    return sum(calibrate_value_for_words(line) for line in lines)


def calibrate_value(line: str) -> int:
    digits = [ch for ch in line if ch.isdigit()]
    if not digits:
        return 0
    first, last = digits[0], digits[-1] if len(digits) > 1 else digits[0]
    return int(first + last)


def sum_calibration_values(lines) -> int:
    return sum(calibrate_value(line) for line in lines)


def test_cases():
    part1_input = [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77)]

    for line, expected in part1_input:
        assert calibrate_value(line) == expected, f"Test case failed for {line}"

    assert sum_calibration_values([line for line, _ in part1_input]) == 142, f"Test case failed for sum"

    part2_input = [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("no_digits", 0)]
    for line, expected in part2_input:
        assert calibrate_value_for_words(line) == expected, f"Test case failed for line: {line}"

    assert sum_calibration_values_for_words([line for line, _ in part2_input]) == 281, f"Test case failed for sum"

    print("All tests passed successfully")


def main():
    input_file = "input.txt"
    with open(input_file, 'r') as input_file:
        content = input_file.read()
        lines = content.splitlines()
        print(f"Sum: {sum_calibration_values_for_words(lines)}")


if __name__ == '__main__':
    test_cases()
    main()
