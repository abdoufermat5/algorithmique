from algo_fermat_utils.helpers import measure_performance


def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive call to compute the (n-1)th and (n-2)th Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)


@measure_performance
def execute_fibo_recursion(n):
    return fibonacci(n)


if __name__ == '__main__':
    print(execute_fibo_recursion(40))
