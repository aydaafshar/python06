import alchemy.elements
import alchemy


def main() -> None:
    def safe_call(label: str, func) -> None:
        try:
            print(f"{label}:", func())
        except Exception as e:
            print(f"{label}: Error - {e}")

    print()
    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")

    safe_call("alchemy.elements.create_fire():",
              alchemy.elements.create_fire)
    safe_call("alchemy.elements.create_air():", alchemy.elements.create_air)
    safe_call("alchemy.elements.create_earth():",
              alchemy.elements.create_earth)
    safe_call("alchemy.elements.create_water():",
              alchemy.elements.create_water)
    print()

    print("Testing package-level access (controlled by __init__.py):")
    safe_call("alchemy.create_fire():", alchemy.create_fire)
    safe_call("alchemy.create_water():", alchemy.create_water)
    try:
        safe_call("alchemy.create_earth()", alchemy.create_earth)
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        safe_call("alchemy.create_air()", alchemy.create_air)
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print()
    print("Package metadata:")
    print("Version: ", alchemy.__version__)
    print("Author: ", alchemy.__author__)


if __name__ == "__main__":
    main()
