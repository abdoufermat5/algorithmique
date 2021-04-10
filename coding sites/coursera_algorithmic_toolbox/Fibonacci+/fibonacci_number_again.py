# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    period = 0
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
    
        if previous == 0 and current == 1:
            period = i + 1
            break
    r = n % period
    if r <= 1:
        return r
    a, b = 0, 1
    for _ in range(2, r + 1):
        a, b = b, (a + b)

    return b % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
