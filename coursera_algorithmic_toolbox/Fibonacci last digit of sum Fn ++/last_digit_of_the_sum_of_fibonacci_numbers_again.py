# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    period = 60
    r1 = from_index % period
    r = to_index % period
    
    a, b = 0, 0
    c = 1
    last = 1 if r >= 1 else 0
    for _ in range(2, r+1):
        a, b = b, c
        c = a + b
        last += c

    last1 = 1 if r1 > 1 else 0
    a, b = 0, 0
    c = 1
    for _ in range(2, r1):
        a, b = b, c
        c = a + b
        last1 += c
    
    res = last - last1
    return res % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
