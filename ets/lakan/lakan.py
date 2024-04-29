import copy

if __name__ == "__main__":
    inputs = [
        [
            list(filter(lambda x: x > 0, list(map(int, input().split())))),
            list(filter(lambda x: x > 0, list(map(int, input().split())))),
        ]
        for _ in range(int(input()))
    ]


def lakan(inputs, v=False):
    totals = []

    for case in inputs:
        currmax = {}
        case11 = copy.deepcopy(case[1])
        case12 = copy.deepcopy(case[1])

        for n in case[0]:
            currmax[n] = n
            for d in case11:
                if abs(n - d) >= abs(n - currmax[n]):
                    currmax[n] = d
            if currmax[n] in case11:
                case11.remove(currmax[n])

        for n in reversed(case[0]):
            currmax[n] = n
            for d in case12:
                if abs(n - d) >= abs(n - currmax[n]):
                    currmax[n] = d
            if currmax[n] in case12:
                case12.remove(currmax[n])

        if v:
            print(
                f"Maksimum total selisihnya {sum([abs(n-currmax[n]) for n in case[0]])} poin."
            )

        totals.append(sum([abs(n - currmax[n]) for n in case[0]]))

    return totals


if __name__ == "__main__":
    lakan(inputs, True)
