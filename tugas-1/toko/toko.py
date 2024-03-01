import re
observed = 1
queue = []
stores = [[],[]]

while True:
    inp = input()
    if "tutup" in inp.lower(): break
    queue.append(re.split(" +", inp))

for item in queue:
    match item[0].lower():
        case "pesan":
            args = list(map(int, item[1:]))
            stores[observed].append(args)
        case "tukar":
            observed = 0 if observed else 1
        case "curi":
            if not stores[observed]: 
                print(f"TOKO {observed+1} KOSONG")
                continue
            if observed:
                stores[observed].pop(0)
            else:
                stores[observed].pop()

for i, t in enumerate(stores):
    print(f"TOKO {i+1} :")
    t.reverse()
    if t: [print(" ".join(map(str, o))) for o in t]
    else: print(f"TOKO {i+1} SEPI :(")
    print(f"TOKO {i+1} UNTUNG : {sum(map(lambda x: x[1], t))}")
