from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    print()
    print("=== Circular Curse Breaking ===")
    print()
    print("=== Circular Curse Breaking ===")
    try:
        print("validate_ingredients('fire air'):",
              validate_ingredients("fire air"))
    except Exception as e:
        print("validate_ingredients('fire air'): Error -", e)
    try:
        print(
            "validate_ingredients('dragon scales'):",
            validate_ingredients("dragon scales")
        )
    except Exception as e:
        print("validate_ingredients('dragon scales'): Error -", e)
    print()
    print("Testing spell recording with validation:")
    try:
        print("record_spell('Fireball', 'fire air'):", record_spell("Fireball",
              "fire air"))
    except Exception as e:
        print("record_spell('Fireball', 'fire air'): Error -", e)
    try:
        print("record_spell('Dark Magic', 'shadow'):",
              record_spell("Dark Magic", "shadow"))
    except Exception as e:
        print("record_spell('Dark Magic', 'shadow'): Error -", e)
    print()
    print("Testing late import technique:")
    try:
        print("record_spell('Lightning', 'air'):", record_spell("Lightning",
              "air"))
    except Exception as e:
        print("record_spell('Lightning', 'air'): Error -", e)
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
