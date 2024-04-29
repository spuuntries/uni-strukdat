if __name__ == "__main__":
    inputs = [
        [
            list(filter(lambda x: x > 0, list(map(int, input().split())))),
            list(filter(lambda x: x > 0, list(map(int, input().split())))),
        ]
        for _ in range(int(input()))
    ]


def revised_lakan(inputs: list[list[list[int]]], v=False):
    # Adapted Tio's solution + Revisions from Farhan, credit to Tio & Farhan
    totals = []

    for case in inputs:
        case[0].sort()
        case[1].sort()
        total = 0

        while case[0] and case[1]:
            x = case[0][0]
            y = case[1][-1]
            toadd = abs(x - y)

            topopx = 0
            topopy = -1

            if toadd < abs(case[0][-1] - case[1][0]):
                x = case[0][-1]
                y = case[1][0]

                toadd = abs(x - y)

                topopx = -1
                topopy = 0

            case[0].pop(topopx)
            case[1].pop(topopy)
            total += toadd
        if v:
            print(f"Maksimum total selisihnya {total} poin.")

        totals.append(total)

    return totals


if __name__ == "__main__":
    revised_lakan(inputs, True)
