
import re

NUMBER_REGEX_OPTIMIZED = r'\b\d+(?:\.\d+)?\b'


def generator_numbers(text):
    for match in re.finditer(NUMBER_REGEX_OPTIMIZED, text):
        number_str = match.group(0)

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
