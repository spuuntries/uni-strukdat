import re

nimp = int(input())
inps = [re.split(" +", input()) for _ in range(nimp)]
plates = []

for inp in inps:
    inst = inp.pop(0)
    inp = list(map(int, inp))
    match inst:
        case "add":
            [plates.append(inp[0]) for _ in range(inp[1])]
            print(len(plates))
        case "del":
            lp = plates[-1]
            [plates.pop() for _ in range(inp[0])]
            print(lp)
        case "adx":
            plates = [p + inp[0] for p in plates]
        case "dex":
            plates = [p - inp[0] for p in plates]
        case "mux":
            plates = [p * inp[0] for p in plates]
