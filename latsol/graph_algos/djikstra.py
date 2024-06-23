import os
import json
from tabulate import tabulate

input_file = input("Input file: ")
if not os.path.exists(os.path.join(os.getcwd(), input_file)):
    print("File not found!")
    exit(1)
with open(os.path.join(os.getcwd(), input_file)) as f:
    graph = json.loads(f.read())

# Pseudocode taken from Wikipedia
# function Dijkstra(Graph, source):
#     create vertex priority queue Q
#
#     dist[source] ← 0                          // Initialization
#     Q.add_with_priority(source, 0)            // associated priority equals dist[·]
#
#     for each vertex v in Graph.Vertices:
#         if v ≠ source
#             prev[v] ← UNDEFINED               // Predecessor of v
#             dist[v] ← INFINITY                // Unknown distance from source to v
#
#
#
#     while Q is not empty:                     // The main loop
#         u ← Q.extract_min()                   // Remove and return best vertex
#         for each neighbor v of u:             // Go through all v neighbors of u
#             alt ← dist[u] + Graph.Edges(u, v)
#             if alt < dist[v]:
#                 prev[v] ← u
#                 dist[v] ← alt
#                 Q.decrease_priority(v, alt)
#
#     return dist, prev


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    # Inisialisasi tabel dengan semua node selain start sebagai inf [dist[v] ← INFINITY]
    distances[start] = 0  # [dist[source] ← 0]
    parents = {}  # Untuk tracking path
    table = []

    pq = [(0, start)]  # Inisialisasi priority queue (pq) [add_with_priority(source, 0)]

    while pq:
        print(pq)
        # 50-51 ambil elemen terkecil [extract_min]
        current_distance, current_node = pq.pop(0)  # FIFO
        if current_distance > distances[current_node]:
            # Jika tidak lebih pendek dari jarak terpendek saat ini, skip
            continue
        table.append(distances.copy())

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            # Jarak + jarak kandidat [alt ← dist[u] + Graph.Edges(u, v)]
            if distance < distances[neighbor]:  # Jika jarak lebih pendek
                distances[neighbor] = distance  # Update jarak terpendek
                # Tambahkan ke parents relasi neighbor -> node untuk tracking path
                parents[neighbor] = current_node  # [decrease_priority(v, alt)]
                # Append terhadap pq kemudian sort kembali berdasarkan jarak
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

    nx.set_node_attributes(G, Style(color="white", bold=True), "$content-style")  # type: ignore
    nx.set_node_attributes(G, Style(color="white"), "$style")  # type: ignore

    nx.set_edge_attributes(G, EdgeRoutingMode.STRAIGHT, "$edge-routing-mode")  # type: ignore
    nx.set_edge_attributes(G, EdgeSegmentDrawingMode.SINGLE_CHARACTER, "$edge-segment-drawing-mode")  # type: ignore

    for edge in G.edges:
        G.edges[edge]["$label"] = str(G.edges[edge]["weight"])
        if edge[0] in res_path and edge[1] in res_path:
            G.edges[edge]["$style"] = Style(color="plum1")
        else:
            G.edges[edge]["$style"] = Style(color="grey11")

    print(ConsoleGraph(G))
