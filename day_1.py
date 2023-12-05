import re

# Part 1: Get calibration values from input file by extracting the first and last digit of a string.
def get_calibration_values_1() -> int:
    file = open('input.txt', 'r')
    list_of_digits = []

    for line in file.readlines():
        digits_in_line = re.findall('\d', line)
        number_result = int(digits_in_line[0]) * 10 + int(digits_in_line[-1])
        list_of_digits.append(number_result)

    file.close()
    return sum(list_of_digits)


# Part 2: Get calibration values from input file by extracting the first and last number(written or int) of a string.
def get_calibration_values_2() -> int:
    file = open('input.txt', 'r')
    list_of_digits = []
    raw_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    pattern = re.compile(raw_regex)
    dict_of_numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for line in file.readlines():
        digits_in_line = re.findall(pattern, line)

        for i, value in enumerate(digits_in_line):
            if value in dict_of_numbers:
                digits_in_line[i] = dict_of_numbers[value]

        number_result = int(digits_in_line[0]) * 10 + int(digits_in_line[-1])
        list_of_digits.append(number_result)

    file.close()
    return sum(list_of_digits)


# Main module
if __name__ == '__main__':
    
    print('Result for the first part of the task:', get_calibration_values_1())
    print('Result for the second part of the task:', get_calibration_values_2())
