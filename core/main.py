import os
import random
import time
import subprocess
from interface import clear, show_banner, loading, typing
from menu import show_menu
from commands import run_module, search_module

def quote():
    quotes = [
        "⚔ Rise... your army awaits.",
        "👑 A true king builds his throne in darkness.",
        "🛡 Power belongs to the one who dares to command.",
        "⚔ The shadows obey the one who rises.",
        "👑 Even kings must first conquer themselves."
    ]
    return random.choice(quotes)

def main():

    clear()
    loading()

    typing("👑 Monarch Awakening...",0.04)
    time.sleep(0.5)

    while True:

        clear()
        show_banner()

        print("\n" + quote())
        print("\n")

        modules = show_menu()

        command = input("\nMonarch > ").strip()

        if command == "0" or command.lower() == "exit":

            typing("\n👑 The throne rests... until you arise again.",0.03)
            time.sleep(1)
            clear()
            break


        elif command.lower() == "help":

            print("\nAvailable Commands:\n")
            print("run <number>      Run a module")
            print("search <keyword>  Search modules")
            print("help              Show commands")
            print("exit              Exit Monarch")
            print("S                 Update Monarch")
            print("U                 Uninstall Monarch")


        elif command.lower().startswith("run"):

            try:
                index = int(command.split()[1]) - 1
                run_module(modules, index)
            except:
                print("Usage: run <module_number>")


        elif command.lower().startswith("search"):

            try:
                keyword = command.split()[1]
                results = search_module(modules, keyword)

                print("\nSearch Results:\n")

                for r in results:
                    print(r)

            except:
                print("Usage: search <keyword>")


        elif command.lower() == "s":

            subprocess.call(["bash","/opt/Monarch/installer/update.sh"])


        elif command.lower() == "u":

            subprocess.call(["bash","/opt/Monarch/installer/uninstall.sh"])
            break


        else:
            print("Unknown command. Type 'help' to see commands.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()