import pytest


def test_greater():
    num = 100
    assert num > 100


def test_greater_equal():
    num = 100
    assert num >= 100


def test_less():
    num = 100
    assert num < 200


@pytest.fixture
def input_value():
    input = 40
    return input


def test_divisible_by_3(input_value):
    assert input_value % 4 == 0


def test_divisible_by_6(input_value):
    assert input_value % 5 == 0
