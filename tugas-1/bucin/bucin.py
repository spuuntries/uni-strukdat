import re

nstuff = int(input())
stuff = [list(map(int, filter(lambda x: len(x), re.split(" +", input())))) for _ in range(nstuff)]
tolook = int(input())

for i, e in enumerate(stuff, 1):
    if e[0] == tolook:
        print(i)
        break
    if i == len(stuff):
        print("Barangnya gak ada beb")