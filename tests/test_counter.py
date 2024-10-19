import pytest
from digit_counter import count_digits
from fractions import Fraction
from decimal import Decimal


def test_integers():
    assert count_digits(0) == 1
    assert count_digits(100) == 3
    assert count_digits(-999) == 3
    assert count_digits(123456789) == 9


def test_floats():
    assert count_digits(3.1415) == 1
    assert count_digits(-10.5) == 2
    assert count_digits(0.0) == 1
    assert count_digits(-0.001) == 1


def test_other_number_types():
    assert count_digits(Decimal('123.456')) == 3
    assert count_digits(Fraction(50, 3)) == 2
    assert count_digits(Fraction(-1000, 1)) == 4


def test_edge_cases():
    assert count_digits(float('inf')) == 1  # Treat infinity as having 1 digit
    assert count_digits(float('-inf')) == 1
    assert count_digits(float('nan')) == 1    # Treat NaN as having 1 digit


def test_boolean():
    with pytest.raises(TypeError, match="Boolean values are not supported."):
        count_digits(True)
    with pytest.raises(TypeError, match="Boolean values are not supported."):
        count_digits(False)


def test_complex_numbers():
    with pytest.raises(TypeError, match="Complex numbers are not supported."):
        count_digits(3 + 4j)
    with pytest.raises(TypeError, match="Complex numbers are not supported."):
        count_digits(-5j)


def test_large_integers():
    assert count_digits(10**100) == 101  # 1 followed by 100 zeros
    assert count_digits(-10**100) == 101


def test_small_fractions_and_decimals():
    assert count_digits(Fraction(1, 10**100)) == 1
    assert count_digits(Decimal('0.0000000001')) == 1


def test_non_numeric_inputs():
    with pytest.raises(TypeError, match="Input is not a valid number type."):
        count_digits("123")
    with pytest.raises(TypeError, match="Input is not a valid number type."):
        count_digits(None)
    with pytest.raises(TypeError, match="Input is not a valid number type."):
        count_digits([1, 2, 3])

