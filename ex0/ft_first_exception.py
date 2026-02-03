def check_temperature(temp_str: str) -> int:
    try:
        print(f"Testing temperature: {temp_str}")
        temp_int: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return -1
    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        return -1
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        return -1
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int


def test_temperature_input() -> None:
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")


def ft_first_exception() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature_input()
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
