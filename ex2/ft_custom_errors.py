class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class GardenError(Exception):
    def __init__(self, message: str = "Caught a garden error:") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Caught PlantError:") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Caught WaterError:") -> None:
        super().__init__(message)


def garden_operations() -> None:
    print("Testing PlantError...")
    try:
        plant: Plant = Plant("tomato", 50, 1000)
        if plant.age > 365:
            raise PlantError()
    except PlantError as e:
        print(f"{e} The {plant.name} plant is wilting!")
    print()
    print("Testing WaterError...")
    try:
        water_in_tank: int = 0
        if water_in_tank < 1:
            raise WaterError()
    except WaterError as e:
        print(f"{e} Not enough water in the tank!")
    print()
    print("Testing catching all garden errors...")
    try:
        plant: Plant = Plant("tomato", 50, 1000)
        if plant.age > 365:
            raise PlantError()
    except GardenError:
        print(f"Caught a garden error: The {plant.name} plant is wilting!")
    try:
        water_in_tank: int = 0
        if water_in_tank < 1:
            raise WaterError()
    except GardenError:
        print("Caught a garden error: Not enough water in the tank!")


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()
    garden_operations()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
