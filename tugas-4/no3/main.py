_ = input()
inputs = list(map(int, input().split()))


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


tree = make(inputs.pop(0))
minimum = int(input())
maximum = int(input())
[insert(tree, make(e)) for e in inputs]


def rangeSum(root, mini, maxi, queue=[], suma=0):
    if not root:
        return
    if mini <= root["val"] <= maxi:
        suma += root["val"]
    if root["left"]:
        queue.append(root["left"])
    if root["right"]:
        queue.append(root["right"])
    if not queue:
        return suma
    nextElem = queue.pop(0)
    return rangeSum(nextElem, mini, maxi, queue, suma)


print(rangeSum(tree, minimum, maximum))
