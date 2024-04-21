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


def findMin(root, current_min=None):
    # Do a DFS to the left-most path
    if not current_min:
        current_min = root
    if not root:
        return current_min
    if root["val"] < current_min["val"]:
        current_min = root
    return findMin(root["left"], current_min)


def sumLeft(root, queue=[], res=[]):
    if root["left"]:
        leftLeafCand = findMin(root)
    else:
        leftLeafCand = None
    if leftLeafCand and not leftLeafCand["right"] and leftLeafCand not in res:
        res.append(leftLeafCand)
    if root["left"]:
        queue.append(root["left"])
    if root["right"]:
        queue.append(root["right"])
    if not queue:
        return res
    nextElem = queue.pop(0)
    return sumLeft(nextElem, queue, res)


if __name__ == "__main__":
    _ = input()
    inputs = list(map(int, input().split()))

    tree = make(inputs.pop(0))
    [insert(tree, make(e)) for e in inputs]

    # print(json.dumps(tree, indent=2))
    # print(sumLeft(tree))
    print(sum([e["val"] for e in sumLeft(tree)]))
