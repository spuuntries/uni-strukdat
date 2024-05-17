# NOTE: This is what the TA gave us, I just modified it a bit to conform to my input formatting.
import os

debug = True


def dfs(curVertex, max_vrtx, adjlist, visited, path):
    visited[curVertex] = True
    path.append(curVertex)
    global max_final, longest_path
    for i in adjlist[int(curVertex)]:
        if not visited[i]:
            dfs(i, max_vrtx + 1, adjlist, visited, path)
    if max_vrtx > max_final:
        max_final = max_vrtx
        longest_path = path.copy()
    visited[curVertex] = False
    path.pop()


max_final = 0
longest_path = []

graph_shape = input().strip().split()
n = int(graph_shape[1])
inputs = [input().strip().split() for _ in range(n)]
start = input().strip()

graph = {int(n): [] for n in range(int(graph_shape[0]))}
for inp in inputs:
    graph[int(inp[0])].append(int(inp[1]))

visited = {node: False for node in graph.keys()}

dfs(start, 0, graph, visited, [])
print(max_final)

if ("DEBUG" in os.environ and os.environ["DEBUG"]) or debug:
    print(f'Longest path: {" -> ".join(map(str, longest_path))}')
