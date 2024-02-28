from src.modules import TheOne

theOne = TheOne()


def test_add_one():
    assert theOne.add_one(7) == 8


def test_minus_one():
    assert theOne.minus_one(7) == 6


def test_multiple_one():
    assert theOne.multiple_one(7) == 7


def test_divide_one():
    assert theOne.divide_one(7) == 7


def test_even_plus_one():
    assert theOne.even_plus_one(8) == 9
    # assert theOne.even_plus_one(9) is None
