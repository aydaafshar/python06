from alchemy.transmutation.basic import lead_to_gold, stone_to_gem

from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


import alchemy.transmutation


def main() -> None:
    def safe_call(label: str, func) -> None:
        try:
            print(f"{label}: ", func())
        except Exception as e:
            print(f"{label}: Error - {e}")
    print()
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")
    safe_call("lead_to_gold(): ", lead_to_gold)
    safe_call("stone_to_gem(): ", stone_to_gem)
    print()

    print("Testing Relative Imports (from advanced.py):")
    safe_call("philosophers_stone(): ", philosophers_stone)
    safe_call("elixir_of_life()", elixir_of_life)
    print()

    print("Testing Package Access:")
    safe_call("alchemy.transmutation.lead_to_gold(): ",
              alchemy.transmutation.lead_to_gold)
    safe_call(
        "alchemy.transmutation.philosophers_stone(): ",
        alchemy.transmutation.philosophers_stone,
    )
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
