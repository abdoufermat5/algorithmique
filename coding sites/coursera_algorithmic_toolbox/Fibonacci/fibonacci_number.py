# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n
    a = 0
    b = 0
    c = 1
    for i in range(2, n+1):
        a, b = b, c
        c = a + b
    return c


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
