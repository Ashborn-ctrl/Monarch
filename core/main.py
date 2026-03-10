import os
import sys
import random
import time
import subprocess
import importlib
import importlib.util

from interface import clear, show_banner, loading, typing
from menu import show_main_menu, show_modules, BASE_MODULE_DIR
from commands import search_module
from requirements import check_requirements


# Ensure project root is in Python path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


def quote():
    quotes = [
        "⚔ Rise... your army awaits.",
        "👑 A true king builds his throne in darkness.",
        "🛡 Power belongs to the one who dares to command.",
        "⚔ The shadows obey the one who rises.",
        "👑 Even kings must first conquer themselves."
    ]
    return random.choice(quotes)

def run_module(module_path):

    try:

        if not os.path.exists(module_path):
            print("Module file not found:", module_path)
            return

        print("Loading module:", module_path)

        spec = importlib.util.spec_from_file_location("monarch_module", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        check_requirements(module)

        if hasattr(module, "run"):
            module.run()
        else:
            print("Module missing run() function")

    except Exception as e:
        print("Error running module:", e)


def module_browser(start_path):

    current_path = start_path

    while True:

        clear()
        show_banner()

        modules = show_modules(current_path)

        choice = input("\nModules > ").strip()

        if choice == "0":
            return


        # help command
        if choice == "help":

            print("\nAvailable Commands:\n")
            print("help               Show help")
            print("search <keyword>   Search modules")
            print("info <number>      Show module info")
            print("update             Update Monarch")
            print("refresh            Reload modules")
            print("uninstall          Remove Monarch")
            print("exit               Return to main menu")

            input("\nPress Enter")
            continue


        # update command
        if choice == "update":

            subprocess.call(["bash", "/opt/Monarch/installer/update.sh"])
            input("\nPress Enter")
            continue


        # uninstall command
        if choice == "uninstall":

            subprocess.call(["bash", "/opt/Monarch/installer/uninstall.sh"])
            break


        # refresh command
        if choice == "refresh":

            print("\nRefreshing modules...\n")
            time.sleep(1)
            continue


        # exit command
        if choice == "exit":
            return


        # search command
        if choice.startswith("search"):

            try:

                keyword = choice.split(" ", 1)[1]

                results = search_module(
                    [m["name"] for m in modules if m["type"] == "module"],
                    keyword
                )

                print("\nResults:\n")

                for r in results:
                    print(r)

            except:
                print("Usage: search <keyword>")

            input("\nPress Enter")
            continue


        # module info command
        if choice.startswith("info"):

            try:

                index = int(choice.split()[1]) - 1
                mod = modules[index]

                if mod["type"] == "module":

                    module = importlib.import_module(f"modules.{mod['import']}")

                    print("\nName:", getattr(module, "name", "Unknown"))
                    print("Author:", getattr(module, "author", "Unknown"))
                    print("Description:", getattr(module, "description", "No description"))

            except:
                print("Usage: info <number>")

            input("\nPress Enter")
            continue


        # numeric navigation
        if choice.isdigit():

            index = int(choice) - 1

            if index < len(modules):

                mod = modules[index]

                if mod["type"] == "folder":

                    current_path = mod["path"]

                elif mod["type"] == "module":

                    run_module(mod["path"])
                    input("\nPress Enter to continue")


def main():

    clear()
    loading()

    typing("👑 Monarch Awakening...", 0.04)
    time.sleep(0.5)

    while True:

        clear()
        show_banner()

        print("\n" + quote() + "\n")

        show_main_menu()

        choice = input("\nMonarch > ").strip()

        if choice == "1":

            module_browser(BASE_MODULE_DIR)

        elif choice == "2":

            subprocess.call(["bash", "/opt/Monarch/installer/update.sh"])
            input("\nPress Enter")

        elif choice == "3":

            subprocess.call(["bash", "/opt/Monarch/installer/uninstall.sh"])
            break

        elif choice == "0":

            typing("\n👑 The throne rests... until you arise again.", 0.03)
            time.sleep(1)
            clear()
            break


if __name__ == "__main__":
    main()
