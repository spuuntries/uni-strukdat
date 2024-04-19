_ = int(input())
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
        print("Duplicate Value!")


def findMin(root, current_min=None):
    # Do a DFS to the left-most path
    if not current_min:
        current_min = root
    if not root:
        return current_min
    if root["val"] < current_min["val"]:
        current_min = root
    return findMin(root["left"], current_min)


def remove(root, val):
    if not root:
        return root
    if val < root["val"]:
        root["left"] = remove(root["left"], val)
    elif val > root["val"]:
        root["right"] = remove(root["right"], val)
    else:
        if root["left"] is None and root["right"] is None:
            root = None
        elif root["left"] is None:
            root = root["right"]
        elif root["right"] is None:
            root = root["left"]
        else:
            replacement = findMin(root["right"])
            root["val"] = replacement["val"]
            root["right"] = remove(root["right"], replacement["val"])
    return root


def preOrder(root):
    if not root:
        return
    print(root["val"], end=" ")
    preOrder(root["left"])
    preOrder(root["right"])


def inOrder(root):
    if not root:
        return
    inOrder(root["left"])
    print(root["val"], end=" ")
    inOrder(root["right"])


def postOrder(root):
    if not root:
        return
    postOrder(root["left"])
    postOrder(root["right"])
    print(root["val"], end=" ")


def search(root, val):
    if not root:
        return None
    if root["val"] == val:
        return root
    if val < root["val"]:
        return search(root["left"], val)
    elif val > root["val"]:
        return search(root["right"], val)
    return None


def find(root, val):
    return [True, False][search(root, val) is None]


tree = make(inputs.pop(0))
[insert(tree, make(e)) for e in inputs]

instructions = [input().split() for _ in range(int(input()))]
for inst in instructions:
    cmd = inst.pop(0)
    match cmd:
        case "insert":
            insert(tree, make(int(inst[0])))
        case "remove":
            if search(tree, int(inst[0])):
                remove(tree, int(inst[0]))
            else:
                print("Cannot Find the Value!")
        case "inorder":
            inOrder(tree)
            print()
        case "postorder":
            postOrder(tree)
            print()
        case "preorder":
            preOrder(tree)
            print()
