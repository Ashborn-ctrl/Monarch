import os
import random
import shutil
import time
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading():
    animation = ["⏳", "⌛", "⏳", "⌛"]
    for i in range(6):
        sys.stdout.write("\rLoading Monarch " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

def center_text(text):
    width = shutil.get_terminal_size().columns
    centered_lines = []
    for line in text.split("\n"):
        centered_lines.append(line.center(width))
    return "\n".join(centered_lines)

def show_banner():

    banners_dir = os.path.join(os.path.dirname(__file__), "..", "banners")

    banner_files = os.listdir(banners_dir)

    banner_path = os.path.join(banners_dir, random.choice(banner_files))

    with open(banner_path, "r") as f:
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

    banner = center_text(banner)

    print(color + banner + "\033[0m")