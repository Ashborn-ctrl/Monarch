name = "Ping Host"
author = "Monarch"
description = "Ping a host to test connectivity"

def run():

    import os

    print("\n⚔ PING TOOL ⚔\n")

    host = input("Enter host: ")

    os.system(f"ping -c 4 {host}")

    input("\nPress Enter to return")