# method 1
import alchemy.elements

# method 2
from alchemy.elements import create_water

# method 3
from alchemy.potions import healing_potion as heal

# method 4
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strength_potion


def main() -> None:
    def safe_call(label: str, func) -> None:
        try:
            print(f"{label}: ", func())
        except Exception as e:
            print(f"{label}: Error - {e}")
    print("=== Import Transmutation Mastery ===")
    print()
    print("Method 1 - Full module import:")
    safe_call("alchemy.elements.create_fire():", alchemy.elements.create_fire)
    print()

    print("Method 2 - Specific function import:")
    safe_call("create_water():", create_water)
    print()

    print("Method 3 - Aliased import:")
    safe_call("heal()", heal)
    print()

    print("Method 4 - Multiple imports:")
    safe_call("create_earth():", create_earth)
    safe_call("create_fire(): ", create_fire)
    safe_call("strength_potion():", strength_potion)
    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
