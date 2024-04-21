from main import sumLeft
from mainbut import sumLeftLeaves
from time import process_time
from tabulate import tabulate
from tqdm import tqdm
import json
import sys
import random

sys.setrecursionlimit(999999999)


def make(val):
    return {"val": val, "left": None, "right": None}


def insert(root, node):
    if not root:
        root = node
    elif node["val"] < root["val"]:
        if not root["left"]:
            root["left"] = node
        else:
            return insert(root["left"], node)
    elif node["val"] > root["val"]:
        if not root["right"]:
            root["right"] = node
        else:
            return insert(root["right"], node)
    else:
        return


perf_1 = []
perf_2 = []

tree_size = 300
inputs = [random.randint(1, 100000) for _ in range(tree_size)]
tree = make(inputs.pop(0))
[insert(tree, make(e)) for e in inputs]

# Warm-up
for _ in tqdm(range(10), desc="Warm-up"):
    sumLeft(tree)
    sumLeftLeaves(tree)

pbar = tqdm(range(100000))
for _ in pbar:
    start_1 = process_time()
    start_1_res = sum([e["val"] for e in sumLeft(tree)])
    perf_1.append(process_time() - start_1)

    start_2 = process_time()
    start_2_res = sumLeftLeaves(tree)
    perf_2.append(process_time() - start_2)

    mean_perf_1 = sum(perf_1) / len(perf_1)
    mean_perf_2 = sum(perf_2) / len(perf_2)

    if mean_perf_1 and mean_perf_2:
        ratio = mean_perf_2 / mean_perf_1
        if ratio < 1:
            diff_desc_1 = f"{ratio*100:.2f}% slower"
            diff_desc_2 = f"{ratio*100:.2f}% faster"
        else:
            diff_desc_1 = f"{ratio*100:.2f}% slower"
            diff_desc_2 = f"{ratio*100:.2f}% faster"
        pbar.set_description(
            f"Initial: {diff_desc_1} ({mean_perf_1:.5f}) || Revised: {diff_desc_2} ({mean_perf_2:.5f})"
        )

    if start_1_res != start_2_res:
        print()
        print(" ".join(map(str, inputs)))
        print(
            f"""Dissonance found for the above tree! 
{start_1_res} != {start_2_res}        
Breaking."""
        )
        break

mean_perf_1 = sum(perf_1) / len(perf_1)
mean_perf_2 = sum(perf_2) / len(perf_2)

ratio = mean_perf_2 / mean_perf_1
if ratio < 1:
    diff_desc_1 = f"{ratio*100:.2f}% slower"
    diff_desc_2 = f"{ratio*100:.2f}% faster"
else:
    diff_desc_1 = f"{ratio*100:.2f}% slower"
    diff_desc_2 = f"{ratio*100:.2f}% faster"

print(
    tabulate(
        [
            ["Algo", "Min", "Mean", "Max", "Diff"],
            [
                "Intial",
                f"{min(perf_1):.5f}",
                mean_perf_1,
                f"{max(perf_1):.5f}",
                diff_desc_1,
            ],
            [
                "Revised",
                f"{min(perf_2):.5f}",
                mean_perf_2,
                f"{max(perf_2):.5f}",
                diff_desc_2,
            ],
        ],
        tablefmt="rounded_grid",
    )
)
