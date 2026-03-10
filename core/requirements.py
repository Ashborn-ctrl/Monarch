import subprocess
import sys
import importlib

def check_requirements(module):

    reqs = getattr(module, "requirements", [])

    for r in reqs:

        try:
            importlib.import_module(r)

        except ImportError:

            print(f"\nInstalling missing dependency: {r}\n")

            subprocess.check_call([sys.executable, "-m", "pip", "install", r])