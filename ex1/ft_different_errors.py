def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()
    print("Testing ZeroDivisionError...")
    try:
        2 // 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        f: object = open("missing.txt")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()
    print("Testing KeyError...")
    try:
        plant: dict = {"rose": "red"}
        plant["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()
    print("Testing multiple errors together...")
    try:
        int("abc")
        2 // 0
        f: object = open("missing.txt")
        f.close()
        plant: dict = {"rose": "red"}
        plant["missing_plant"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()


def test_error_types() -> None:
    print()
    garden_operations()
    print()


def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    ft_different_errors()
