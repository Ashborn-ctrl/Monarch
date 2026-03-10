import importlib

def run_module(modules, index):

    if index < len(modules):

        module_name = modules[index]

        module = importlib.import_module(f"modules.{module_name}")

        if hasattr(module,"run"):
            module.run()
        else:
            print("Module missing run() function")

    else:
        print("Invalid module")


def search_module(modules, keyword):

    results = []

    for module in modules:

        if keyword.lower() in module.lower():
            results.append(module)

    return results