import os
import json
from tabulate import tabulate
from time import perf_counter

debug = False

input_file = input("Input file: ")
if not os.path.exists(os.path.join(os.getcwd(), input_file)):
    print("File not found!")
    exit(1)
with open(os.path.join(os.getcwd(), input_file)) as f:
    graph = json.loads(f.read())

no_rank = input("Union By Rank? (Y/n) ").strip().lower() == "n"
print(["Using union by rank", "Using naive union"][int(no_rank)])

def find(parents, u):
    if parents[u] != u:
        parents[u] = find(parents, parents[u])
    return parents[u]


def union(parents, ranks, u, v):
    pu, pv = find(parents, u), find(parents, v)

    if debug or os.environ.get("debug"):
        print(f"[DEBUG] RANKS:\n{ranks}")
    
    if debug or os.environ.get("debug"):
        print(f"[DEBUG] PARENTS: {parents}")
        print(f"[DEBUG] UNION:\nNodes: ({u}, {v}) - Node Parents: ({pu}, {pv})")
    
    if pu == pv:
        return False
    if ranks[pu] > ranks[pv]:
        parents[pv] = pu
    elif ranks[pu] < ranks[pv]:
        parents[pu] = pv
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True

def nr_union(parents, u, v):
    pu, pv = find(parents, u), find(parents, v)

    if debug or os.environ.get("debug"):
            print(f"[DEBUG] PARENTS: {parents}")
            print(f"[DEBUG] UNION:\nNodes: ({u}, {v}) - Node Parents: ({pu}, {pv})")
    
    if pu == pv:
        return False
    
    parents[pu] = pv
    return True



def kruskal_mst(graph):
    edges = set()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edge = tuple(sorted([vertex, neighbor])) + (weight,)
            edges.add(edge)

    edges = list(edges)
    edges.sort(key=lambda x: x[2])
    parents = {node: node for node in graph}
    ranks = {node: 0 for node in graph}
    mst = []

    if debug or os.environ.get("debug"):
        print()
        print(f"[DEBUG] Sorted edges:\n{"\n".join(map(str,edges))}")
        print()

    if debug or os.environ.get("debug"):
        start_time = perf_counter()
        
    for u, v, weight in edges:
        if debug or os.environ.get("debug"):
            print(f"[DEBUG] MST: {mst}")

        if union(parents, ranks, u, v):
            mst.append((u, v, weight))
    
    if debug or os.environ.get("debug"):
        print(f"[DEBUG] Took {perf_counter() - start_time}s")

    return mst

def nr_kruskal_mst(graph):
    edges = set()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edge = tuple(sorted([vertex, neighbor])) + (weight,)
            edges.add(edge)

    edges = list(edges)
    edges.sort(key=lambda x: x[2])
    parents = {node: node for node in graph}
    ranks = {node: 0 for node in graph}
    mst = []

    if debug or os.environ.get("debug"):
        print()
        print(f"[DEBUG] Sorted edges:\n{"\n".join(map(str,edges))}")
        print()
        
    if debug or os.environ.get("debug"):
        start_time = perf_counter()

    for u, v, weight in edges:
        if debug or os.environ.get("debug"):
            print(f"[DEBUG] MST: {mst}")

        if nr_union(parents, u, v):
            mst.append((u, v, weight))
            
    if debug or os.environ.get("debug"):
        print(f"[DEBUG] Took {perf_counter() - start_time}s")

    return mst


edge_set = set()
for vertex, neighbors in graph.items():
    for neighbor, weight in neighbors:
        edge = tuple(sorted([vertex, neighbor])) + (weight,)
        edge_set.add(edge)
edge_list = list(edge_set)
print("Edge List:")
print(
    tabulate(
        [["U", "V", "Weight"], *list(map(list, edge_list))],
        tablefmt="rounded_grid",
        headers="firstrow",
    )
)
print(f"Weight sum: {sum(map(lambda e: e[2], edge_list))}")

if no_rank:
    mst = nr_kruskal_mst(graph)
else:
    mst = kruskal_mst(graph)

print()
print("Minimum Spanning Tree Edges:")
print(
    tabulate(
        [["U", "V", "Weight"], *list(map(list, mst))],
        tablefmt="rounded_grid",
        headers="firstrow",
    )
)
print(f"Weight sum: {sum(map(lambda e: e[2], mst))}")

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
    for node, neighbor, distance in edge_list:
        G.add_edge(node, neighbor, weight=distance)

    G_res = nx.Graph()
    for node, neighbor, distance in mst:
        G_res.add_edge(node, neighbor, weight=distance)

    nx.set_node_attributes(G, Style(color="white", bold=True), "$content-style")  # type: ignore
    nx.set_node_attributes(G, Style(color="white"), "$style")  # type: ignore

    nx.set_node_attributes(G_res, Style(color="white", bold=True), "$content-style")  # type: ignore
    nx.set_node_attributes(G_res, Style(color="white"), "$style")  # type: ignore

    nx.set_edge_attributes(G, EdgeRoutingMode.STRAIGHT, "$edge-routing-mode")  # type: ignore
    nx.set_edge_attributes(G, EdgeSegmentDrawingMode.SINGLE_CHARACTER, "$edge-segment-drawing-mode")  # type: ignore

    nx.set_edge_attributes(G_res, EdgeRoutingMode.STRAIGHT, "$edge-routing-mode")  # type: ignore
    nx.set_edge_attributes(G_res, EdgeSegmentDrawingMode.SINGLE_CHARACTER, "$edge-segment-drawing-mode")  # type: ignore

    nx.set_edge_attributes(G, Style(color="grey11"), "$style")  # type: ignore
    nx.set_edge_attributes(G_res, Style(color="plum1"), "$style")  # type: ignore

    for edge in G.edges:
        G.edges[edge]["$label"] = str(G.edges[edge]["weight"])
        if edge in G_res.edges:
            G.edges[edge]["$style"] = Style(color="plum1")

    for edge in G_res.edges:
        G_res.edges[edge]["$label"] = str(G_res.edges[edge]["weight"])

    print("Initial input:")
    print(ConsoleGraph(G))

    print()
    print("Result:")
    print(ConsoleGraph(G_res))
