
import re

NUMBER_REGEX = r"(?<=\s)\d+(?:\.\d+)?(?=\s)"


def generator_numbers(text):
    for number_str in re.findall(NUMBER_REGEX, text):
        yield float(number_str)


def sum_profit(text, func):
    number_generator = func(text)

    total_sum = sum(number_generator)

    return total_sum


text = """Загальний дохід працівника складається з \
декількох частин: 1000.01 як основний дохід, \
доповнений додатковими надходженнями 27.45 і 324.00 доларів."""

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
