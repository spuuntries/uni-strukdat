import os
import json
from tabulate import tabulate

input_file = input("Input file: ")
if not os.path.exists(os.path.join(os.getcwd(), input_file)):
    print("File not found!")
    exit(1)
with open(os.path.join(os.getcwd(), input_file)) as f:
    graph = json.loads(f.read())


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    parents = {}
    table = []

    pq = [(0, start)]

    while pq:
        current_distance, current_node = pq.pop(0)
        if current_distance > distances[current_node]:
            continue
        table.append(distances.copy())

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                pq = sorted(pq + [(distance, neighbor)], key=lambda x: x[0])

    return distances, pq, parents, table


start_node = input("Starting node: ")
target_node = input("End node: ")
res = dijkstra(graph, start_node)
print(res[2])
found = ["No", "Yes"][res[0][target_node] != float("inf")]

print()
print(f"Path found? {found}")
print("Resulting table:")
print(tabulate(res[3], headers="keys", tablefmt="rounded_grid"))

if found:
    res_path = []
    backtrack = target_node
    while backtrack != start_node:
        res_path.insert(0, backtrack)
        backtrack = res[2][backtrack]
    res_path.insert(0, backtrack)
print(" -> ".join(res_path))

# NOTE: Graph Visualization, non-crucial
print()
if input("Visualize (Y/n)? ").strip().lower() != "n":
    from netext import ConsoleGraph
    from netext.edge_rendering.arrow_tips import ArrowTip
    from netext.edge_routing.modes import EdgeRoutingMode
    from netext.edge_rendering.modes import EdgeSegmentDrawingMode
    from rich.style import Style
    import networkx as nx

    from rich import print

    G = nx.Graph()
    for node in graph:
        G.add_node(node)
        for neighbor, distance in graph[node]:
            G.add_edge(node, neighbor, weight=distance)

    nx.set_node_attributes(G, Style(color="blue", bold=True), "$content-style")  # type: ignore
    nx.set_node_attributes(G, Style(color="green"), "$style")  # type: ignore

    nx.set_edge_attributes(G, EdgeRoutingMode.ORTHOGONAL, "$edge-routing-mode")  # type: ignore
    nx.set_edge_attributes(G, EdgeSegmentDrawingMode.BOX, "$edge-segment-drawing-mode")  # type: ignore

    for edge in G.edges:
        if edge[0] in res_path and edge[1] in res_path:
            G.edges[edge]["$style"] = Style(color="blue")
        else:
            G.edges[edge]["$style"] = Style(color="white")

    print(ConsoleGraph(G))
