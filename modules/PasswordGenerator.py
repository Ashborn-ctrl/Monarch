name = "Password Generator"
author = "Monarch"
description = "Generate secure passwords"

def run():

    import random
    import string

    print("\n⚔ PASSWORD GENERATOR ⚔\n")

    length = int(input("Password length: "))

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = "".join(random.choice(chars) for _ in range(length))

    print("\nGenerated Password:\n")
    print(password)

    input("\nPress Enter to return")