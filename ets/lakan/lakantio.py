f = int(input())
a_list = []
b_list = []
for i in range(f):
    a = list(map(int, input().split()))
    a.pop()
    a_list.append(a)
    b = list(map(int, input().split()))
    b.pop()
    b_list.append(b)

for i in range(f):
    x = a_list[i]
    y = b_list[i]
    x.sort()
    y.sort()
    ntah = 0
    while y and x:
        ntah += abs(x.pop(0) - y.pop())
        if x and y:
            ntah += abs(x.pop() - y.pop(0))
    print(f"Maksimum total selisihnya {ntah} poin.")
