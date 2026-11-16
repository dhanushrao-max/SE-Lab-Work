
TOPPINGS = {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}
SIZES = {"S": 8, "M": 10, "L": 12}


def toppings_price(toppings_csv):
    if not isinstance(toppings_csv, str):
        raise ValueError("Toppings must be a string")

    if not toppings_csv.strip():
        raise ValueError("Toppings cannot be empty")

    total = 0

    for t in toppings_csv.split(','):
        topping = t.strip().lower()

        if not topping:
            raise ValueError("Empty topping is not allowed")

        if topping not in TOPPINGS:
            raise ValueError("Invalid topping: " + topping)

        total += TOPPINGS[topping]

    return total


def pizza_inches(size):
    if not isinstance(size, str):
        raise ValueError("Size must be a string")

    size = size.strip().upper()

    if size not in SIZES:
        raise ValueError("Invalid pizza size")

    return SIZES[size]


def split_bill(text):
    if not isinstance(text, str):
        raise ValueError("Bill input must be a string")

    if text.count('/') != 1:
        raise ValueError("Enter bill in total/people format")

    total, people = text.split('/')

    try:
        total = int(total.strip())
        people = int(people.strip())
    except ValueError:
        raise ValueError("Total and people must be integers")

    if total < 0:
        raise ValueError("Total cannot be negative")

    if people <= 0:
        raise ValueError("People must be greater than zero")

    return round(total / people, 2)


def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)
    print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)
    print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)
    print("Per Person:", result)


if __name__ == "__main__":
    main()
