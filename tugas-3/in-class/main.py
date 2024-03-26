import json

def make(val):
    return {"val": val, "left": None, "right": None}

def insert(root, node):
    if not root:
        root = node
    elif node["val"] < root["val"]:
        if not root["left"]: root["left"] = node
        else: return insert(root["left"], node)
    elif node["val"] > root["val"]: 
        if not root["right"]: root["right"] = node
        else: return insert(root["right"], node)
    else: 
        return

def search(root, val):
    if not root: return None
    if root["val"] == val: return root
    if val < root["val"]:
       return search(root["left"], val)
    elif val > root["val"]:
       return search(root["right"], val)
    return None

def find(root, val):
    return [True, False][search(root, val) is None]

def findMin(root, current_min=None):
    # Do a DFS to the left-most path
    if not current_min: 
        current_min = root
    if not root: return current_min
    if root["val"] < current_min["val"]: 
        current_min = root
    return findMin(root["left"], current_min)

def findMax(root, current_max=None):
    # Do a DFS to the right-most path
    if not current_max: 
        current_max = root
    if not root: return current_max
    if root["val"] > current_max["val"]: 
        current_max = root
    return findMax(root["right"], current_max)

def remove(root, val):
    if not root: return root
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
    if not root: return
    print(root["val"], end=" ")
    preOrder(root["left"])
    preOrder(root["right"])

def inOrder(root):
    if not root: return
    inOrder(root["left"])
    print(root["val"], end=" ")
    inOrder(root["right"])

def postOrder(root):
    if not root: return
    postOrder(root["left"])
    postOrder(root["right"])
    print(root["val"], end=" ")

def levelOrder(root, queue=[]):
    if not root: return
    print(root["val"], end=" ")
    if root["left"]: 
        queue.append(root["left"])
    if root["right"]: 
        queue.append(root["right"])
    if not queue: return
    nextElem = queue.pop(0)
    return levelOrder(nextElem, queue)

root = None
while True:
    inp = input().strip()
    if inp.lower() == "stop": 
        print(json.dumps(root, indent=2, default=str))
        break
    if root is None: 
        root = make(int(inp))
    else:
        insert(root, make(int(inp)))

print(find(root, int(input("Find: ").strip())))
print(f"Minimum: {findMin(root)['val']}")
print(f"Maximum: {findMax(root)['val']}")
print(json.dumps(remove(root, int(input("Remove: ").strip())), indent=2, default=str))
print("Pre-order:")
preOrder(root)
print()
print("In-order:")
inOrder(root)
print()
print("Post-order:")
postOrder(root)
print()
print("Level-order:")
levelOrder(root)
print()
