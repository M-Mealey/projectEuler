import time
import importlib.util
import os
import multiprocessing

resource_files = {
    22: ["resources/names.txt"],
    42: ["resources/words.txt"],
    54: ["resources/poker.txt"],
    59: ["resources/cipher1.txt", "resources/wordlist.txt"],
    67: ["resources/triangle.txt"],
    79: ["resources/keylog.txt"],
    81: ["resources/matrix.txt"],
    82: ["resources/matrix.txt"],
    83: ["resources/matrix.txt"],
    89: ["resources/roman.txt"],
    96: ["resources/sudoku.txt"],
    98: ["resources/words.txt"],
    99: ["resources/base_exp.txt"],
}

TIMEOUT_SECONDS = 1


def load_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_mod_folder(x):
    if 0 < x <= 100:
        return "p1to100"
    if 100 < x <= 200:
        return "p101to200"
    return None


def _worker(queue, module_name, module_path, args):
    """Run solve() in a child process and put (elapsed, result) on queue."""
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    start = time.perf_counter()
    result = module.solve(*args)
    elapsed = time.perf_counter() - start
    queue.put((elapsed, result))


def import_and_run(x):
    """ Import and run problem x, printing elapsed time. Times out after 1 second. """
    fmt_x = f"{x:04d}"
    module_folder = get_mod_folder(x)
    if not module_folder:
        print(f"module folder could not be found for problem {x}")
        return

    module_path = os.path.join(module_folder, f"eul_{fmt_x}.py")
    if not os.path.exists(module_path):
        print(f"file not found at {module_path}")
        return

    args = ()
    if x in resource_files:
        full_file_paths = [module_folder + "/" + f for f in resource_files[x]]
        args = (full_file_paths,)

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=_worker, args=(
        queue, f"eul_{fmt_x}", module_path, args))
    p.start()
    p.join(timeout=TIMEOUT_SECONDS)

    if p.is_alive():
        p.terminate()
        p.join()
        print(f"\033[31mproblem {x}: timed out (>{TIMEOUT_SECONDS}s)\033[0m")
    else:
        elapsed, result = queue.get()
        print(f"problem {x}: {result} ({elapsed:.4f}s)")


if __name__ == '__main__':
    for i in range(101):
        import_and_run(i)
