import time
import importlib
import importlib.util
import os


def load_module_from_path(module_name, file_path):
    """
    This function was written by google AI :/
    Loads a Python module dynamically from a given file path.
    """
    # Create a module specification
    spec = importlib.util.spec_from_file_location(module_name, file_path)

    # Create a new module object from the specification
    module = importlib.util.module_from_spec(spec)

    # Register the module in sys.modules (optional, but allows normal imports to work later)
    # sys.modules[module_name] = module

    # Execute the module's code in its own namespace
    spec.loader.exec_module(module)

    return module


def get_mod_folder(x):
    if 0 < x <= 100:
        return "p1to100"
    if 100 < x <= 200:
        return "p101to200"
    return


def import_and_run(x):
    """ Import and run problem x """
    fmt_x = f"{x:04d}"
    module_folder = get_mod_folder(x)
    if not module_folder:
        print(f"module folder could not be found for problem {x}")
        return  # @TODO: error handling

    module_path = os.path.join(module_folder, f"eul_{fmt_x}.py")
    try:
        eul_prob = load_module_from_path(f"eul_{fmt_x}", module_path)
        start_time = time.perf_counter()
        eul_prob.solve()
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"problem {x}: {elapsed_time} seconds")
    except FileNotFoundError:
        print(f"file not found at {module_path}")


for i in range(11):
    import_and_run(i)
