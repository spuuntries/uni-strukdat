_ = input()
initial = input().split()
secondary = []
inputs = [input().split() for _ in range(int(input()))]

for i, inp in enumerate(inputs):
    cmd = inp.pop(0)
    if cmd == "PULL":
        if int(inp[0]) > len(initial):
            print("Macaron Furina tidak sebanyak itu pls!")
        else:
            to_insert = initial[-int(inp[0]) :]
            [initial.pop() for _ in range(int(inp[0]))]
            secondary.append(to_insert.pop(0))
            initial += reversed(to_insert)
    elif cmd == "PUT":
        initial += reversed(secondary)
        secondary = []
    else:
        print("Apa itu? Furina tidak paham!")
print(" ".join(initial))
print(" ".join(secondary))
