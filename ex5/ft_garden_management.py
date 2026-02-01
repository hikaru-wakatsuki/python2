class GardenError(Exception):
    def __init__(self, message: str = "Caught a garden error:") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Caught PlantError:") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Caught WaterError:") -> None:
        super().__init__(message)


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[dict] = []
        self.water_tank: int = 0

    def add_plants(self, plant_name: str, water_level: int,
                   sunlight_hours: int) -> None:
        try:
            if not plant_name:
                raise PlantError("Error adding plant: "
                                 "Plant name cannot be empty!")
            self.plants += [{
                "name": plant_name,
                "water_level": water_level,
                "sunlight_hours": sunlight_hours
                }]
        except PlantError as e:
            print(e)

    def water_plants(self, water_tank: int) -> None:
        try:
            self.water_tank += water_tank
            for plant in self.plants:
                if self.water_tank < 1:
                    raise WaterError()
                print(f"Watering {plant['name']} - success")
                self.water_tank -= 1
                plant["water_level"] += 5
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plants:
                check_plant_health(
                    plant["name"],
                    plant["water_level"],
                    plant["sunlight_hours"]
                )
        except ValueError as e:
            print(e)

    def check_water_tank(self) -> None:
        try:
            if self.water_tank < 1:
                raise GardenError("Caught GardenError: "
                                  "Not enough water in tank")
        except GardenError as e:
            print(e)
            self.water_tank += 5
        finally:
            print("System recovered and continuing...")


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    print(f"{plant_name}: healthy (water: {water_level}, "
          f"sun: {sunlight_hours})")


def test_garden_management() -> None:
    print("Adding plants to garden...")
    gm: GardenManager = GardenManager()
    gm.add_plants("tomato", 0, 8)
    gm.add_plants("lettuce", 10, 8)
    gm.add_plants("", 10, 8)
    print()
    print("Watering plants...")
    plus_water: int = 2
    gm.water_plants(plus_water)
    print()
    print("Checking plant health...")
    gm.check_plant_health()
    print()
    print("Testing error recovery...")
    gm.check_water_tank()


def ft_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    test_garden_management()
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    ft_garden_management()
