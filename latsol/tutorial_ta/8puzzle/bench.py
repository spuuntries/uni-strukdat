from mainheap import main as mainstarheap
from main import main as mainstar
from reference import main as mainmain
from time import process_time
from tabulate import tabulate

"""
Benchmarking code, results I got:
╭────────────────────────────────┬────────────────────┬────────────────┬────────────────┬──────────────────╮
│ Function (repeated 10 times)   │   Average Time (s) │   Min Time (s) │   Max Time (s) │   Total Time (s) │
├────────────────────────────────┼────────────────────┼────────────────┼────────────────┼──────────────────┤
│ A* (with heapq)                │            0.00625 │       0        │       0.015625 │           0.0625 │
├────────────────────────────────┼────────────────────┼────────────────┼────────────────┼──────────────────┤
│ A*                             │            0.0125  │       0        │       0.03125  │           0.125  │
├────────────────────────────────┼────────────────────┼────────────────┼────────────────┼──────────────────┤
│ BFS                            │            1.15156 │       0.796875 │       1.84375  │          11.5156 │
╰────────────────────────────────┴────────────────────┴────────────────┴────────────────┴──────────────────╯
"""

repeat = 10


def run_and_measure(func, num_runs=10, *args, **kwargs):
    timings = []
    for _ in range(num_runs):
        start_time = process_time()
        result = func(*args, **kwargs)
        end_time = process_time()
        timings.append(end_time - start_time)
    avg_time = sum(timings) / len(timings)
    min_time = min(timings)
    max_time = max(timings)
    total_time = sum(timings)
    return avg_time, min_time, max_time, total_time


times = []
for func in [mainstarheap, mainstar, mainmain]:
    avg_time, min_time, max_time, total_time = run_and_measure(func, num_runs=repeat)
    times.append((avg_time, min_time, max_time, total_time))

data = [
    [
        f"Function (repeated {repeat} times)",
        "Average Time (s)",
        "Min Time (s)",
        "Max Time (s)",
        "Total Time (s)",
    ]
]
for i, func_name in enumerate(["A* (with heapq)", "A*", "BFS"]):
    avg_time, min_time, max_time, total_time = times[i]
    data.append([func_name, avg_time, min_time, max_time, total_time])

# Tabulate and print the results
print(tabulate(data, headers="firstrow", tablefmt="rounded_grid"))
