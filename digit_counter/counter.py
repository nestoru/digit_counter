import argparse
import math
import sys
from fractions import Fraction
from decimal import Decimal
import numbers


def count_digits(number: numbers.Number) -> int:
    """
    Count the number of base-10 digits in the integer part of a number.

    Parameters
    ----------
    number : numbers.Number
        A numeric value (int, float, Decimal, Fraction, etc.).

    Returns
    -------
    int
        The number of digits in the integer part of the number.

    Raises
    ------
    TypeError
        If the input is a boolean or a complex number.
    """
    if isinstance(number, bool):
        raise TypeError("Boolean values are not supported.")
    if isinstance(number, complex):
        raise TypeError("Complex numbers are not supported.")
    if not isinstance(number, numbers.Number):
        raise TypeError("Input is not a valid number type.")
    if isinstance(number, float) and (math.isinf(number) or math.isnan(number)):
        return 1
    try:
        integer_part = abs(int(number))
    except (OverflowError, ValueError):
        return 1
    return len(str(integer_part)) if integer_part != 0 else 1


def main():
    """
    Command-line interface for the Digit Counter.

    Usage:
        python digit_counter/counter.py <number>
        digit-counter <number>
    """
    parser = argparse.ArgumentParser(
        description=(
            "Count the number of base-10 digits "
            "in the integer part of a number."
        )
    )
    parser.add_argument(
        "number",
        type=str,
        help=(
            "The number to count digits for. It can be an "
            "integer, float, Decimal, Fraction, etc."
        ),
    )
    args = parser.parse_args()
    number_str = args.number
    try:
        if '.' in number_str or '/' in number_str:
            try:
                number = float(number_str)
            except ValueError:
                try:
                    number = Fraction(number_str)
                except ValueError:
                    number = Decimal(number_str)
        else:
            number = int(number_str)
    except Exception as e:
        print(f"Error: Invalid number format. {e}")
        sys.exit(1)
    try:
        digit_count = count_digits(number)
        print(digit_count)
    except TypeError as te:
        print(f"Error: {te}")
        sys.exit(1)


if __name__ == "__main__":
    main()
