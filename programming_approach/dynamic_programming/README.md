# Dynamic Programming

![Dynamic Programming](https://avikdas.com/assets/images/2019-04-15-visual-introduction-to-dynamic-programming/fibonacci-naive.png)

Dynamic programming is a technique for solving problems by breaking them down into smaller subproblems, solving each
subproblem, and then combining the solutions to the subproblems to solve the original problem. The key idea behind
dynamic programming is to store the solutions to the subproblems so that they can be reused (instead of recomputing
them) when needed. This can lead to significant time savings, especially for problems with overlapping subproblems.

Here is an example of how to use dynamic programming to solve the Fibonacci sequence problem in python:

```python
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
```

In this implementation, the fibonacci function uses a recursive function **fib** to compute the nth Fibonacci number. The
**fib** function takes as input an integer **n** and returns the nth Fibonacci number. The fib function uses dynamic programming
to store the solutions to the subproblems in a cache, so that they can be reused instead of recomputing them. This leads
to significant time savings, especially for large values of n.