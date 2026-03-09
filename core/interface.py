import os
import random

def show_banner():
    banners_dir = os.path.join(os.path.dirname(__file__), "..", "banners")

    banners = [
        "banner1.txt",
        "banner2.txt",
        "banner3.txt"
    ]

    banner_file = random.choice(banners)

    with open(os.path.join(banners_dir, banner_file), "r") as f:
        banner = f.read()

    colors = [
        "\033[91m",
        "\033[92m",
        "\033[93m",
        "\033[94m",
        "\033[95m",
        "\033[96m"
    ]

    color = random.choice(colors)

    print(color + banner + "\033[0m")