"""The root of the package."""


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def main() -> None:
    print("Hello from rf-metric!")
    print(f"1 + 2 = {add(1, 2)}")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum of {a} and {b} is {add(a, b)}.")
