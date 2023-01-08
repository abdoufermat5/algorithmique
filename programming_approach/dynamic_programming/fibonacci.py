from algo_fermat_utils.helpers import measure_performance


@measure_performance
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Create a cache to store the solutions to the subproblems
    cache = [None] * (n + 1)

    # Recursive function to compute the nth Fibonacci number
    def fib(n):
        # If we have already computed the nth Fibonacci number, return it
        if cache[n] is not None:
            return cache[n]
        # If not, compute it and store it in the cache
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result

    # Call the recursive function to compute the nth Fibonacci number
    return fib(n)


if __name__ == '__main__':
    # avec 16Go de ram, ça calcule jusqu'au terme 996
    print(fibonacci(996))
