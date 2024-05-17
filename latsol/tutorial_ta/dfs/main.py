from dfs import Solution
from typing import Any

if __name__ == "__main__":
    print("Running custom input testing for DFS sum...")
    print("(Run dfs.py instead to test w/ sample case)")
    solution = Solution()

    nodes = list(
        map(
            lambda x: x.strip(),
            input(
                "Graph (Format it like this `5,4,8,11,null,...` per-level with null as no branch):\n"
            )
            .replace("[", "")
            .replace("]", "")
            .strip()
            .split(","),
        )
    )
    target_sum = int(input("Target sum: ").strip())
    root = solution.make(int(nodes.pop(0)))
    node_pairs = [
        list(
            map(
                lambda x: solution.make(x) if x and x != "null" else None,
                [nodes[i], nodes[i + 1]],
            )
        )
        for i in range(0, len(nodes), 2)
    ]

    g_queue = [root]
    while g_queue:  # NOTE: Graph construction via a BFS manner
        curr = g_queue.pop(0)
        if not node_pairs:
            break
        pair = node_pairs.pop(0)
        curr["left"] = pair[0]
        curr["right"] = pair[1]
        if curr["left"]:
            g_queue.append(curr["left"])
        if curr["right"]:
            g_queue.append(curr["right"])

    queue = [(root, 0, set())]  # type: list[tuple[dict[str, Any], int, set]]
    print(solution.dfsum(target_sum, queue))
