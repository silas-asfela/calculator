def divide(a, b):
    """Return the result of dividing a by b.

    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    print(divide(12, 4))   # 3.0
    print(divide(-10, 4))  # -2.5
    print(divide(7, 2))    # 3.5
