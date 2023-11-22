from typing import List


def diagonalTRaverse(a: List[List[int]]) -> List[int]:
    from collections import defaultdict
    diag_dict = defaultdict(list)
    num_rows = len(a)
    num_cols = max(map(len, a))
    res = []

    for i in range(num_rows):
        for j in range(len(a[i])):
            diag_dict[i + j].append(a[i][j])
    for i in range(num_rows + num_cols - 1):
        res += reversed(diag_dict[i])

    return res


if __name__ == "__main__":
    test_a = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    res = diagonalTRaverse(test_a)

    print(res)
