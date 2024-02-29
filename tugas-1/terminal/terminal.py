import re

inps = []

while True:
    split = re.split(" +", input())
    if any(map(lambda x: "stop" in x.lower(), split)):
        break
    inps.append(split)

store = []

for inp in inps:
    inst = inp.pop(0)
    match inst.lower():
        case "append":
            store.append(inp[0])
        case "prepend":
            store.insert(0, inp[0])
        case "cp":
            store.insert(int(inp[1]), store[int(inp[0])])
        case "mv":
            tm = store.pop(int(inp[0]))
            store.insert(int(inp[1]), tm)
        case "rm":
            if len(inps) - 1 > int(inp[0]):
                store.pop(int(inp[0]))
        case _:
            print("Bukan perintah valid")

print(len(store))
[print(i) for i in store]
