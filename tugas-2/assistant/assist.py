inputs = []
results = []
while True:
    inp = input().strip()
    if "stop" in inp:
        break
    inputs.append(list(filter(lambda x: len(x) and "." != x, inp.split("/"))))

for stack in inputs:
    res = []
    while len(stack):
        current = stack.pop()
        if current == "..":
            if len(stack) > 2:
                while stack.pop() == "..":
                    stack.pop()
            elif len(stack):
                stack.pop()
            continue
        else:
            res.append(current)
    results.append(res)

[
    print("/".join(reversed(r)))
    if "/".join(r).startswith("/")
    else print("/" + "/".join(reversed(r)))
    for r in results
]
