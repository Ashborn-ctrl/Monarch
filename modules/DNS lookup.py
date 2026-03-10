name = "DNS Lookup"
author = "Monarch"
description = "Resolve domain to IP"

def run():

    import socket

    print("\n⚔ DNS LOOKUP ⚔\n")

    domain = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(domain)
        print("\nIP Address:", ip)

    except:
        print("\nCould not resolve domain")

    input("\nPress Enter to return")