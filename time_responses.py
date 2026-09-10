"""
run all the problems and time how long it takes to run
"""
import time
import importlib.util
import os
import sys
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed

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
    102: ["resources/triangles.txt"],
    105: ["resources/sets.txt"],
    107: ["resources/network.txt"]
}

TIMEOUT_SECONDS = 5



def get_mod_folder(p):
    """ get the folder that a problem solution is in """
    if 0 < p <= 100:
        return "p1to100"
    if 100 < p <= 200:
        return "p101to200"
    return None


def _worker(queue, module_name, module_path, args):
    """Run solve() in a child process and put (elapsed, result) on queue."""
    module_dir = os.path.dirname(os.path.abspath(module_path))
    if module_dir not in sys.path:
        sys.path.append(module_dir)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    start = time.perf_counter()
    result = module.solve(*args)
    elapsed = time.perf_counter() - start
    queue.put((elapsed, result))


def run_problem(n):
    """Run problem x and return a result string."""
    fmt_x = f"{n:04d}"
    module_folder = get_mod_folder(n)
    if not module_folder:
        return f"problem {n}: module folder not found"

    module_path = os.path.join(module_folder, f"eul_{fmt_x}.py")
    if not os.path.exists(module_path):
        return None

    args = ()
    if n in resource_files:
        full_file_paths = [module_folder + "/" + f for f in resource_files[n]]
        args = (full_file_paths,)

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=_worker, args=(
        queue, f"eul_{fmt_x}", module_path, args))
    p.start()
    p.join(timeout=TIMEOUT_SECONDS)

    if p.is_alive():
        p.terminate()
        p.join()
        return f"\033[31mproblem {n}: timed out (>{TIMEOUT_SECONDS}s)\033[0m"
    elapsed, result = queue.get()
    return f"problem {n}: {result} ({elapsed:.4f}s)"


if __name__ == '__main__':
    problems = range(1, 108)
    results = {}

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        future_to_x = {executor.submit(run_problem, p_x): p_x for p_x in problems}
        for future in as_completed(future_to_x):
            results[future_to_x[future]] = future.result()

    for x in sorted(results):
        if results[x]:
            print(results[x])
