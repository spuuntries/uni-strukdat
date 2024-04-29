inputs = [input().split() for _ in range(int(input()))]
buku = []

for inp in inputs:
    inst = inp.pop(0)
    if inst == "BELI":
        buku.append(inp[0])
    elif inst == "JUAL":
        buku.remove(inp[0])
    elif inst == "PRINT":
        print("\n".join(buku) + "\n---")
