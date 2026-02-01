class Plant:
    def __init__(self, name: str) -> None:
        self.name: str = name


class GardenError(Exception):
    def __init__(self, message: str = "Caught a garden error:") -> None:
        super().__init__(message)


def check_plants(plant: Plant) -> None:
    garden_plants: list[Plant] = [
        Plant("tomato"),
        Plant("lettuce"),
        Plant("carrots"),
        ]
    for garden_plant in garden_plants:
        if plant.name == garden_plant.name:
            return
    raise GardenError("Error: Cannot water None - invalid plant!")


def water_plants(plant_list: list[Plant]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_list:
            check_plants(plant)
            print(f"Watering {plant.name}")
    except GardenError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("Testing normal watering...")
    plant_list: list[Plant] = [
        Plant("tomato"),
        Plant("lettuce"),
        Plant("carrots"),
    ]
    water_plants(plant_list)
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    plant_list: list[Plant] = [
        Plant("tomato"),
        Plant("potato"),
        Plant("carrots")
    ]
    water_plants(plant_list)


def ft_finally_block():
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    ft_finally_block()
