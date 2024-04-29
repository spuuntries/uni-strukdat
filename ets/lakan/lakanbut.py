if __name__ == "__main__":
    inputs = [
        [
            list(filter(lambda x: x > 0, list(map(int, input().split())))),
            list(filter(lambda x: x > 0, list(map(int, input().split())))),
        ]
        for _ in range(int(input()))
    ]


def revised_lakan(inputs: list[list[list[int]]], v=False):
    # Adapted Tio's solution, credit to Tio
    totals = []

    for case in inputs:
        case[0].sort()
        case[1].sort()
        total = 0

        while case[0] and case[1]:
            total += abs(case[0].pop(0) - case[1].pop())
            if case[0] and case[1]:
                total += abs(case[0].pop() - case[1].pop(0))
        if v:
            print(f"Maksimum total selisihnya {total} poin.")

        totals.append(total)

    return totals


if __name__ == "__main__":
    revised_lakan(inputs, True)
