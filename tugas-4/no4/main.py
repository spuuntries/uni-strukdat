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


def findHeight(root, queue=[], level=0) -> int:
    if not root:
        return level
    queue.append(root)
    while queue:
        current_level_size = len(queue)
        for _ in range(current_level_size):
            node = queue.pop(0)
            if node["left"]:
                queue.append(node["left"])
            if node["right"]:
                queue.append(node["right"])
        level += 1
    return level


inputs = list(map(int, input().split()))
tree = make(inputs.pop(0))
[insert(tree, make(e)) for e in filter(lambda x: bool(x), inputs)]


print(findHeight(tree))
