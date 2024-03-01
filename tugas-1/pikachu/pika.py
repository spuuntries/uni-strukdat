import re

ntest = int(input())
cases = []

for _ in range(ntest):
    case = {}
    case["entry"], case["ncap"] = map(int, re.split(" +", input()))
    case["usage"] = []
    nuse = int(input())
    for _ci in range(nuse):
        bc = list(map(int, re.split(" +", input())))
        case["usage"].append({"entry": bc[0], "exit": bc[1]})
    cases.append(case)

for case in cases:
    lot = []
    for h in range(case["entry"]+1):
        for use in case["usage"]:
            if use["entry"] == h: lot.append(1)
            if use["exit"] == h: lot.pop()
    if len(lot) < case["ncap"]: 
        print("Pika Pika!")
    else:
        print("Pika Zzz")