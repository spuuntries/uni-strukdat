from lakanbut import revised_lakan
from tabulate import tabulate
from time import process_time
from lakan import lakan
from tqdm import tqdm
import random

# Generate samples
sample_size = 100
input_size = 10
max_case = 100
min_case = 4

print(
    f"Testing with {input_size} array pairs of size minimum {min_case} and maximum {max_case}"
)

for inputs in [
    [
        [
            [
                random.randint(0, 1000)
                for _ in range(random.randint(min_case, max_case))
            ],
            [
                random.randint(0, 1000)
                for _ in range(random.randint(min_case, max_case))
            ],
        ]
        for _ in range(input_size)
    ]
    for _ in tqdm(range(sample_size // 10), desc="Warming up...")
]:
    lakan(inputs)
    revised_lakan(inputs)

samples = [
    [
        [
            [
                random.randint(0, 1000)
                for _ in range(random.randint(min_case, max_case))
            ],
            [
                random.randint(0, 1000)
                for _ in range(random.randint(min_case, max_case))
            ],
        ]
        for _ in range(input_size)
    ]
    for _ in tqdm(range(sample_size), desc="Generating samples...")
]


old_time = []
old_reses = []
rev_time = []
rev_reses = []

pbar = tqdm(samples)
for inputs in pbar:
    old_start = process_time()
    old_res = lakan(inputs)
    old_reses.append(old_res)
    old_time.append(process_time() - old_start)

    rev_start = process_time()
    rev_res = revised_lakan(inputs)
    rev_reses.append(rev_res)
    rev_time.append(process_time() - rev_start)

    pbar.set_description(
        f"Old Avg: {sum(old_time)/len(old_time):.8f} || New Avg: {sum(rev_time)/len(rev_time):.8f}"
    )

print(samples[0])
print(old_reses[0])
print(rev_reses[0])

print(
    tabulate(
        [
            ["Algo", "Min", "Mean", "Max"],
            [
                "Old",
                f"{min(old_time):.8f}",
                f"{sum(old_time)/len(old_time):.8f}",
                f"{max(old_time):.8f}",
            ],
            [
                "Revised",
                f"{min(rev_time):.8f}",
                f"{sum(rev_time)/len(rev_time):.8f}",
                f"{max(rev_time):.8f}",
            ],
        ],
        tablefmt="rounded_grid",
    )
)
