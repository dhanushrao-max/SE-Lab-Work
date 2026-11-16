
from hypothesis import given, strategies as st
from pizza_order import toppings_price, pizza_inches, split_bill


# TEST 1: TOPPINGS PRICE
def test_toppings_price_valid():
    assert toppings_price("cheese,olives") == 70
    assert toppings_price(" CHEESE , ONION ") == 60


@given(st.text() | st.none())
def test_toppings_price_no_crash(s):
    try:
        toppings_price(s)
    except ValueError:
        pass


# TEST 2: PIZZA INCHES
def test_pizza_inches_valid():
    assert pizza_inches("S") == 8
    assert pizza_inches("M") == 10
    assert pizza_inches("L") == 12


@given(st.text() | st.none())
def test_pizza_inches_no_crash(s):
    try:
        pizza_inches(s)
    except ValueError:
        pass


# TEST 3: SPLIT BILL
def test_split_bill_valid():
    assert split_bill("900/3") == 300.0
    assert split_bill("1000/4") == 250.0


@given(st.text() | st.none())
def test_split_bill_no_crash(s):
    try:
        split_bill(s)
    except ValueError:
        pass
