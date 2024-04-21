import json


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


def sumLeftLeaves(root, res=0):
    if not root:
        return res

    if root["left"] and root["left"]["left"] is None and root["left"]["right"] is None:
        res += root["left"]["val"]

    res = sumLeftLeaves(root["left"], res)
    res = sumLeftLeaves(root["right"], res)

    return res


if __name__ == "__main__":
    _ = input()
    inputs = list(map(int, input().split()))

    tree = make(inputs.pop(0))
    [insert(tree, make(e)) for e in inputs]

    # print(json.dumps(tree, indent=2))
    # print(sumLeft(tree))
    print(sumLeftLeaves(tree))
