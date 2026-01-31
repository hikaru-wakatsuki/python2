def test_temperature_input(temp_str: str) -> None:
    try:
        print(f"Testing temperature: {temp_str}")
        temp_int: int = int(temp_str)
        check_temperature(temp_int)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return


def check_temperature(temp_int: int) -> int:
    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        return -1
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        return -1
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int


def ft_first_exception():
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature_input("25")
    print()
    test_temperature_input("abc")
    print()
    test_temperature_input("100")
    print()
    test_temperature_input("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
