from calculator.basic import a, multiply, circle_area
from calculator.stats import process_data


def test_add():
    assert a(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_circle_area():
    assert round(circle_area(1), 2) == 3.14


def test_process_data():
    r = process_data([1, 2, 3, 4])
    assert r["mean"] == 2.5
    assert r["max"] == 4
    assert r["min"] == 1
