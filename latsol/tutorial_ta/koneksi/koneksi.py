import os

debug = True


def iddfs_longest_path(graph, start, max_depth=100):
    def dfs(
        node, depth, visited, path, longest_path
    ):  # NOTE: This is a DLS technically
        if depth > max_depth:
            return
        visited.add(node)
        path.append(node)

        if len(path) > len(longest_path):
            longest_path[:] = path.copy()

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, depth + 1, visited, path, longest_path)

        path.pop()
        visited.remove(node)

    longest_path = []
    for depth in range(max_depth):
        dfs(start, 0, set(), [], longest_path)
    return longest_path


graph_shape = input().strip().split()
n = int(graph_shape[1])
inputs = [input().strip().split() for _ in range(n)]
start = input().strip()

graph = {str(n): [] for n in range(int(graph_shape[0]))}
for inp in inputs:
    graph[inp[0]].append(inp[1])

# NOTE: Arbitrary max depth estimator, I honestly was unsure regarding this.
longest_path = iddfs_longest_path(graph, start, int(graph_shape[0]) * 100)
print(len(longest_path) - 1)  # NOTE: Exclude source node in resulting length
if ("DEBUG" in os.environ and os.environ["DEBUG"]) or debug:
    print(f'Longest path: {" -> ".join(longest_path)}')


# A bit unrelated of a discussion, (but regardless an imho important one at that) this is an NP-Hard problem,
# and this would only be easy to do for acyclics,
# i.e. see: https://en.wikipedia.org/wiki/Longest_path_problem#Approximation
#
# Ideally, the solution is probably a DFS, as a BFS has one too many pitfalls for this
# (e.g., one off the top of my head would be the size of the queue for something with a high branching factor).
#
# However, a justification of my IDDFS approach includes (but isn't limited to) the better worst-case depth handling:
# Since I terminate on max_depth, we won't be recursing until a stack overflow for a graph with a deep/possibly infinite depth path.
#
# Ofc, this assumes that the DFS is implemented w/o an explicit stack for a recursion elimination (i.e. see: https://github.com/spuuntries/uni-daspro/blob/master/tlx-problems/gunung/gunungbut.py)
# and no cycle-detection is done.
