import os

MODULE_DIR = os.path.join(os.path.dirname(__file__), "..", "modules")

def get_modules():

    modules = []

    for file in os.listdir(MODULE_DIR):
        if file.endswith(".py") and not file.startswith("_"):
            modules.append(file[:-3])

    return modules


def show_menu():

    modules = get_modules()

    print("⚔ MONARCH MODULES ⚔\n")

    for i, module in enumerate(modules, 1):
        print(f"[{i}] {module}")

    print("\n[S] Update Monarch")
    print("[U] Uninstall Monarch")
    print("[0] Exit")

    return modules