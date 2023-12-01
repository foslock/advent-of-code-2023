INPUT_FILE = "input.txt"
CHAR_DIGITS = "0123456789"
TEXT_DIGITS = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
STARTING_LETTERS = set(n[0] for n in TEXT_DIGITS)


def get_digits_from_line(line: str) -> tuple[int, int]:
    """ Part one """
    digits: list[int] = []
    for char in line:
        if char in CHAR_DIGITS:
            digits.append(int(char))

    if len(digits) < 1:
        raise ValueError("Invalid input given (no digits found)")
    elif len(digits) == 1:
        return digits[0], digits[0]
    else:
        return digits[0], digits[-1]


def get_digits_from_line_v2(line: str) -> tuple[int, int]:
    """ Part two """
    digits: list[int] = []
    for i, char in enumerate(line):
        if char in CHAR_DIGITS:
            digits.append(int(char))
        elif char in STARTING_LETTERS:
            for j, text_digit in enumerate(TEXT_DIGITS):
                if line[i:i+len(text_digit)].lower() == text_digit.lower():
                    digits.append(j)

    if len(digits) < 1:
        raise ValueError("Invalid input given (no digits found)")
    elif len(digits) == 1:
        return digits[0], digits[0]
    else:
        return digits[0], digits[-1]



def main():
    total = 0
    with open(INPUT_FILE, "rt") as f:
        for line in f.readlines():
            first, second = get_digits_from_line(line)
            total += int(f"{first}{second}")

    print(total)
    # 56108

    total = 0
    with open(INPUT_FILE, "rt") as f:
        for line in f.readlines():
            first, second = get_digits_from_line_v2(line)
            print(f"{line} got {first}, {second}")
            total += int(f"{first}{second}")

    print(total)
    # 55652


if __name__ == "__main__":
    main()