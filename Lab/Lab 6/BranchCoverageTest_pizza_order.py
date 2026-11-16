
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# PIZZA PRICE - BRANCH TESTS

def test_valid_small_pizza():
    assert pizza_price("small", 0, False) == 200


def test_valid_medium_pizza():
    assert pizza_price("medium", 2, False) == 430


def test_valid_large_pizza():
    assert pizza_price("large", 5, False) == 680


def test_invalid_pizza_size():
    with pytest.raises(ValueError):
        pizza_price("extra_large", 0, False)


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("small", -1, False)


def test_three_toppings():
    assert pizza_price("medium", 3, False) == 470


def test_more_than_three_toppings():
    assert pizza_price("medium", 5, False) == 530


def test_cheese_burst_available():
    assert pizza_price("large", 0, True) == 600


def test_cheese_burst_unavailable():
    with pytest.raises(ValueError):
        pizza_price("small", 0, True)


def test_cheese_burst_disabled():
    assert pizza_price("small", 1, False) == 240


# ORDER DISCOUNT - BRANCH TESTS

def test_order_below_300():
    assert order_discount(299, "monday", False) == 0


def test_order_exactly_300():
    assert order_discount(300, "monday", False) == 30


def test_tuesday_discount():
    assert order_discount(500, "tuesday", False) == 250


def test_saturday_discount():
    assert order_discount(500, "saturday", False) == 0


def test_sunday_discount():
    assert order_discount(500, "sunday", False) == 0


def test_regular_weekday_discount():
    assert order_discount(500, "monday", False) == 50


def test_student_discount():
    assert order_discount(500, "monday", True) == 100


def test_tuesday_student_discount():
    assert order_discount(500, "tuesday", True) == 300


# DELIVERY STATUS - BRANCH TESTS

def test_distance_over_10():
    assert delivery_status(20, 11) == "not deliverable"


def test_distance_exactly_10():
    assert delivery_status(20, 10) == "on time"


def test_delivery_within_30_minutes():
    assert delivery_status(30, 5) == "on time"


def test_delivery_between_31_and_45_minutes():
    assert delivery_status(40, 5) == "late"


def test_delivery_exactly_45_minutes():
    assert delivery_status(45, 5) == "late"


def test_delivery_over_45_minutes():
    assert delivery_status(46, 5) == "free pizza"
