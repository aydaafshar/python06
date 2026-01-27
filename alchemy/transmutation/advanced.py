from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    gold_result = lead_to_gold()
    heal_result = healing_potion()
    return f"Philosopher’s stone createdusing {gold_result} {heal_result}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
