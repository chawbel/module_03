import sys


def parse_args(args: list[str]) -> dict:
    inventory = dict()
    for arg in args[1:]:
        if ":" not in arg:
            print("Invalid argument")
            continue
        key, value = arg.split(":")
        inventory[key] = int(value)
    return inventory


def count_items(inventory: dict) -> int:
    count = 0
    for nb in inventory.values():
        count += nb
    return count


def current_inventory(inventory: dict) -> None:
    count = count_items(inventory)
    for key, value in inventory.items():
        print(f"{key}: {value} units"
            f"({(value * count) / 100:.1f})%")


def inventory_statistics(inventory: dict) -> None:
    min_key = None
    max_key = None
    min = float("inf")
    max = float("-inf")
    for key, value in inventory.items():
        if value > max:
            max = value
            max_key = key
        elif value < min:
            min = value
            min_key = key
    print(f"Most abundant: {max_key} ({max} units)")
    print(f"Least abundant: {min_key} ({min} units)")


def check_availability(inventory: dict) -> None:
    moderate = dict()
    scarce = dict()
    for key, value in inventory.items():
        if value < 4:
            scarce.update({key:value})
        elif value >= 4:
            moderate.update({key:value})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def check_restock(inventory: dict) -> None:
    items = []
    for key, value in inventory.items():
        if value < 2:
            items.append(key)
    print(f"Restock needed: {items}")


def lookup(inventory: dict, name: str) -> None:
    if name in inventory:
        print(f"Sample lookup - '{name}' in inventory: True")
    else:
        print(f"Sample lookup - '{name}' in inventory: False")


def display_all(inventory: dict) -> None:

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {count_items(inventory)}")
    print(f"Unique item types: {len(inventory)}")
    print("")

    print("=== Current Inventory ===")
    current_inventory(inventory)
    print("")

    print("=== Inventory Statistics ===")
    inventory_statistics(inventory)
    print("")

    print("=== Item Category ===")
    check_availability(inventory)
    print("")

    print("=== Management Suggesstions ===")
    check_restock(inventory)
    print("")


    print("=== Dictionary Properties Demo ===")
    keys = list(inventory.keys())
    values = list(inventory.values())
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    lookup(inventory, "sword")


if __name__ == "__main__":
    display_all(parse_args(sys.argv))
