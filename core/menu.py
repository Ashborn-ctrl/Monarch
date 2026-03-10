import os

BASE_MODULE_DIR = os.path.join(os.path.dirname(__file__), "..", "modules")


def discover_modules(path):

    modules = []

    for item in sorted(os.listdir(path)):

        if item.startswith("__"):
            continue

        full = os.path.join(path, item)

        if os.path.isdir(full):

            modules.append({
                "type": "folder",
                "name": item,
                "path": full
            })

        elif item.endswith(".py"):

            display_name = item[:-3].replace("_"," ").title()

            modules.append({
                "type": "module",
                "name": display_name,
                "file": item,
                "path": full
            })

    return modules


def show_modules(path):

    modules = discover_modules(path)

    print("⚔ MODULES ⚔\n")

    for i, mod in enumerate(modules,1):

        print(f"[{i}] {mod['name']}")

    print("\n[0] Back")

    return modules


def show_main_menu():

    print("⚔ MONARCH ⚔\n")

    print("[1] Modules")
    print("[2] Update")
    print("[3] Uninstall")
    print("[0] Exit")
