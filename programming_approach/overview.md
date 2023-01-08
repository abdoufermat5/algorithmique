# Brief overview of the programming approach

## Dynamic Programming vs Recursion

Recursion and dynamic programming are two techniques that can be used to solve problems by breaking them down into
smaller subproblems. Both techniques involve recursion, which is the process of defining a function in terms of itself.
However, they differ in how they handle the subproblems.

Recursion is a technique that solves a problem by breaking it down into smaller subproblems and calling itself
recursively to solve those subproblems. It is a simple and intuitive technique, but it can be inefficient because it may
recompute the same subproblems multiple times. The time complexity of a recursive algorithm is often expressed using
the "big O" notation and is typically at least O(2^n) for a problem with n subproblems. The space complexity is
typically O(n), which is the space required to store the recursive calls on the call stack.

Dynamic programming is a technique that solves a problem by breaking it down into smaller subproblems and storing the
solutions to the subproblems in a cache (usually an array) so that they can be reused when needed. This can lead to
significant time savings, especially for problems with overlapping subproblems. The time complexity of a dynamic
programming algorithm is often O(n^2) or O(n^3) for a problem with n subproblems, and the space complexity is O(n).

In general, dynamic programming is more efficient than recursion, but it may be more difficult to implement and may
require more space. Which technique is best depends on the specific problem and the desired time and space trade-offs.

I hope this helps! Let me know if you have any questions.

|                        | Recursion                                                                                                              | Dynamic Programming                                                                                                                                         |
|------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition             | Solve a problem by breaking it down into smaller subproblems and calling itself recursively to solve those subproblems | Solve a problem by breaking it down into smaller subproblems and storing the solutions to the subproblems in a cache so that they can be reused when needed |
| Time complexity        | O(2^n) or higher                                                                                                       | O(n^2) or O(n^3)                                                                                                                                            |
| Space complexity       | O(n)                                                                                                                   | O(n)                                                                                                                                                        |
| Ease of implementation | Simple                                                                                                                 | More complex                                                                                                                                                |
| Efficiency             | Less efficient                                                                                                         | More efficient                                                                                                                                              |
| Usefulness             | Useful for problems with few subproblems                                                                               | Useful for problems with many overlapping subproblems                                                                                                       |


## Dynamic Programming vs Brute Force

|                        | Dynamic Programming                                                                                                                                         | Brute Force                                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Definition             | Solve a problem by breaking it down into smaller subproblems and storing the solutions to the subproblems in a cache so that they can be reused when needed | Try all possible combinations of solutions and select the best one |
| Time complexity        | O(n^2) or O(n^3)                                                                                                                                            | O(n!) or higher                                                    |
| Space complexity       | O(n)                                                                                                                                                        | O(n) or higher                                                     |
| Ease of implementation | More complex                                                                                                                                                | Simple                                                             |
| Efficiency             | More efficient                                                                                                                                              | Less efficient                                                     |
| Usefulness             | Useful for problems with many overlapping subproblems                                                                                                       | Useful for small or simple problems                                |

## Dynamic Programming vs Greedy

|                        | Dynamic Programming                                                                                                                                         | Greedy Algorithm                                                                        |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Definition             | Solve a problem by breaking it down into smaller subproblems and storing the solutions to the subproblems in a cache so that they can be reused when needed | Make the locally optimal choice at each step, with the hope of finding a global optimum |
| Time complexity        | O(n^2) or O(n^3)                                                                                                                                            | O(n log n) or O(n)                                                                      |
| Space complexity       | O(n)                                                                                                                                                        | O(1) or O(n)                                                                            |
| Ease of implementation | More complex                                                                                                                                                | Simple                                                                                  |
| Efficiency             | More efficient                                                                                                                                              | Faster than dynamic programming but may not always find the optimal solution            |
| Usefulness             | Useful for problems with many overlapping subproblems                                                                                                       | Useful for problems where the locally optimal choice leads to a global optimum          |

## Dynamic Programming vs Divide and Conquer

|                        | Dynamic Programming                                                                                                                                         | Divide and Conquer                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition             | Solve a problem by breaking it down into smaller subproblems and storing the solutions to the subproblems in a cache so that they can be reused when needed | Divide the problem into smaller subproblems, solve each subproblem independently, and then combine the solutions to the subproblems to solve the original problem |
| Time complexity        | O(n^2) or O(n^3)                                                                                                                                            | O(n log n) or O(n^2)                                                                                                                                              |
| Space complexity       | O(n)                                                                                                                                                        | O(n) or O(log n)                                                                                                                                                  |
| Ease of implementation | More complex                                                                                                                                                | Simple                                                                                                                                                            |
| Efficiency             | More efficient for problems with many overlapping subproblems                                                                                               | More efficient for some problems but may require more space                                                                                                       |
| Usefulness             | Useful for problems with many overlapping subproblems                                                                                                       | Useful for problems that can be divided into smaller independent subproblems                                                                                      |

## Dynamic Programming vs Randomized Algorithms

|                        | Dynamic Programming                                                                                                                                         | Randomized Algorithm                                                          |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Definition             | Solve a problem by breaking it down into smaller subproblems and storing the solutions to the subproblems in a cache so that they can be reused when needed | Use randomness to solve a problem                                             |
| Time complexity        | O(n^2) or O(n^3)                                                                                                                                            | O(n log n) or O(n)                                                            |
| Space complexity       | O(n)                                                                                                                                                        | O(1) or O(n)                                                                  |
| Ease of implementation | More complex                                                                                                                                                | Simple                                                                        |
| Efficiency             | More efficient                                                                                                                                              | Faster than dynamic programming but may not always find the optimal solution  |
| Usefulness             | Useful for problems with many overlapping subproblems                                                                                                       | Useful for problems where the use of randomness can lead to faster algorithms |


## Dynamic Programming vs Backtracking

|                        | Dynamic Programming                                                                                                                                         | Backtracking                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Definition             | Solve a problem by breaking it down into smaller subproblems and storing the solutions to the subproblems in a cache so that they can be reused when needed | Search for a solution by exploring all possible paths and backtracking when a path leads to a dead end |
| Time complexity        | O(n^2) or O(n^3)                                                                                                                                            | O(b^d) or O(n!)                                                                                        |
| Space complexity       | O(n)                                                                                                                                                        | O(b^d) or O(n!)                                                                                        |
| Ease of implementation | More complex                                                                                                                                                | Simple                                                                                                 |
| Efficiency             | More efficient                                                                                                                                              | Less efficient                                                                                         |
| Usefulness             | Useful for problems with many overlapping subproblems                                                                                                       | Useful for problems with a large or infinite space of possible solutions                               |

**Note:** In the time and space complexity rows, `b` is the branching factor (the average number of children of each node in the search tree) and `d` is the depth of the solution (the distance from the root of the tree to the solution). `n` is the size of the input.
