import json
from typing import Any


class Solution:
    def make(self, val):
        return {"val": val, "left": None, "right": None}

    def dfsum(self, target_sum, queue: list[tuple[dict[str, Any], int, set]]) -> bool:
        if not queue:
            return False

        current_node, current_sum, visited = queue.pop(0)

        current_sum += int(current_node["val"])
        visited.add(str(current_node))

        if current_sum == target_sum:
            if not (current_node["left"] or current_node["right"]):  # NOTE: Leaf check
                return True

        if current_node["left"] and str(current_node["left"]) not in visited:
            queue.append((current_node["left"], current_sum, visited.copy()))
        if current_node["right"] and str(current_node["right"]) not in visited:
            queue.append((current_node["right"], current_sum, visited.copy()))

        return self.dfsum(target_sum, queue)


if __name__ == "__main__":
    import colorama
    colorama.init()

    solution = Solution()
    print("Testing leaf sum solution...")

    # Format it as (graph nodes array, target sum, expected output)
    inputs = [
     ([5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", "null", 1], 22, True),
     ([5, 4, 8, 11, "null", 13, 4, 7, 2, "null", "null", "null", 1], 21, False),
     ([1,2,3], 5, False),
     ([1,2,3], 4, True)
    ]
    results = []

    for nodes, target_sum, expected in inputs:
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
        res = solution.dfsum(target_sum, queue)
        results.append((nodes, res, target_sum, expected))
    
    for i, (nodes, res, target_sum, expected) in enumerate(results):
        print(f"=== Test case #{i+1} ===")
        print(f"Input: {[root["val"]] + nodes} with target of {target_sum}")
        print(f"Expected: {expected}")
        print(f"Received: {res}")
        print(f"Passing: {[f"{colorama.Fore.RED}No{colorama.Style.RESET_ALL}", 
        f"{colorama.Fore.GREEN}Yes{colorama.Style.RESET_ALL}"][int(res == expected)]}")
