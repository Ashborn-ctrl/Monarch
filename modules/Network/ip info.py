name = "IP Info"
author = "Monarch"
description = "Get public IP information"

requirements = ["requests"]

def run():

    import requests

    print("\n⚔ IP INFORMATION TOOL ⚔\n")

    ip = input("Enter IP (or press Enter for your IP): ")

    if ip == "":
        url = "https://ipinfo.io/json"
    else:
        url = f"https://ipinfo.io/{ip}/json"

    r = requests.get(url)

    data = r.json()

    print("\nIP:", data.get("ip"))
    print("City:", data.get("city"))
    print("Region:", data.get("region"))
    print("Country:", data.get("country"))
    print("Org:", data.get("org"))

    input("\nPress Enter to return")