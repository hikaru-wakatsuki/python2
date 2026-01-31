def check_temperature(temp_str: str) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")


def ft_first_exception():
    print("=== Garden Temperature Checker ===")
    print()
    check_temperature(25)
    print()
    check_temperature("abc")
    print()
    check_temperature(100)
    print()
    check_temperature(-50)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    ft_first_exception()
