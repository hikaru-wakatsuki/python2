def garden_operations() -> None:
    try:
        int("abc")
    except ValueError:
        test_error_types("ValueError")
    print()
    try:
        2 // 0
    except ZeroDivisionError:
        test_error_types("ZeroDivisionError")
    print()
    try:
        f: object = open("missing.txt")
        f.close()
    except FileNotFoundError:
        test_error_types("FileNotFoundError")
    print()
    try:
        plant: dict = {"rose": "red"}
        plant["missing_plant"]
    except KeyError:
        test_error_types("KeyError")
    print()
    try:
        int("abc")
        2 // 0
        f: object = open("missing.txt")
        f.close()
        plant: dict = {"rose": "red"}
        plant["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        test_error_types("multiple errors together")
    print()


def test_error_types(Error: str) -> None:
    print(f"Testing {Error}...")
    if Error == "ValueError":
        print("Caught ValueError: invalid literal for int()")
    elif Error == "ZeroDivisionError":
        print("Caught ZeroDivisionError: division by zero")
    elif Error == "FileNotFoundError":
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    elif Error == "KeyError":
        print("Caught KeyError: 'missing_plant'")
    elif Error == "multiple errors together":
        print("Caught an error, but program continues!")


def ft_different_errors():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")

if __name__ == "__main__":
    ft_different_errors()
