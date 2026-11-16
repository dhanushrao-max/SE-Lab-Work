
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# PIZZA PRICE TESTS

def test_small_pizza():
    assert pizza_price("small", 0, False) == 200


def test_large_pizza_with_toppings():
    assert pizza_price("large", 5, False) == 680


def test_medium_pizza_with_three_toppings():
    assert pizza_price("medium", 3, False) == 470


def test_cheese_burst():
    assert pizza_price("medium", 0, True) == 450


def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra_large", 0, False)


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("small", -1, False)


def test_small_cheese_burst():
    with pytest.raises(ValueError):
        pizza_price("small", 0, True)


# ORDER DISCOUNT TESTS

def test_order_below_300():
    assert order_discount(250, "monday", False) == 0


def test_tuesday_discount():
    assert order_discount(500, "tuesday", False) == 250


def test_weekend_discount():
    assert order_discount(500, "saturday", False) == 0


def test_sunday_student_discount():
    assert order_discount(500, "sunday", True) == 50


def test_weekday_student_discount():
    assert order_discount(500, "monday", True) == 100


# DELIVERY STATUS TESTS

def test_not_deliverable():
    assert delivery_status(20, 11) == "not deliverable"


def test_on_time():
    assert delivery_status(30, 5) == "on time"


def test_late_delivery():
    assert delivery_status(40, 5) == "late"


def test_free_pizza():
    assert delivery_status(50, 5) == "free pizza"
