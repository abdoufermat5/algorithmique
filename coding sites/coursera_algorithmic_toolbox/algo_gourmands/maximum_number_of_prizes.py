# python3
import operator
from functools import reduce
from itertools import combinations, accumulate


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    k = n
    l = 1
    while k > 0:
        if k <= 2 * l:
            summands.append(k)
            k -= k
        else:
            summands.append(l)
            k -= l
        l += 1
    print(summands)
    
    # def sum_i(l):
    #     return l
    # if n <= 2:
    #     return [n]
    # l = list(range(1, n))
    # r_n = range(n)
    # f = lambda i: sum(l[:i+1]) <= n
    # num_com = sum(list(map(f, r_n)))
    # print(num_com)
    # r = range(1, n-num_com+1)
    # c = combinations(r, num_com)
    # l = list(map(sum_i, c))
    # if len(l) > 0:
    #     combs.append(l)
    #
    # print(combs)
    # return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
