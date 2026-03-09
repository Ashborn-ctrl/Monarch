import os
import random
import shutil
from interface import show_banner
from menu import show_menu

def clear():
    os.system("clear")

def quote():
    quotes = [
        "⚔️ Rise, for a king bows to none.",
        "👑 Power belongs to those who dare to command it.",
        "🛡 A ruler sharpens the mind before the sword.",
        "⚔️ A true monarch builds empires from discipline.",
        "👑 Even shadows kneel before a determined king."
    ]
    return random.choice(quotes)

def main():
    while True:
        clear()
        show_banner()

        print("\n" + quote())
        print("\n")

        show_menu()

        choice = input("\nMonarch > ")

        if choice == "1":
            print("\nModules system coming soon...")
            input("\nPress Enter to continue")

        elif choice == "2":
            print("\nUpdating toolkit...")
            input("\nPress Enter")

        elif choice == "3":
            print("\nUninstall option selected...")
            input("\nPress Enter")

        elif choice == "0":
            print("\n👑 Farewell, Monarch.")
            break

        else:
            print("\nInvalid option")
            input("\nPress Enter")

if __name__ == "__main__":
    main()