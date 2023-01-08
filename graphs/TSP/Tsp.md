# TSP Problem

## Problem Description

The traveling salesman problem (TSP) is a well-known problem in computer science. It involves finding the shortest
possible route that visits a given set of cities and returns to the starting city. The goal is to minimize the total
distance traveled. The TSP has many practical applications, such as planning the most efficient delivery routes for a
delivery company or finding the shortest route for a salesman to visit a set of clients. The TSP is a classic example of
a combinatorial optimization problem, which means that it involves finding an optimal solution from a large set of
possible solutions. It is an NP-hard problem, which means that there is no known algorithm that can solve it efficiently
for large instances. However, there are approximate algorithms that can find good solutions for small to medium-sized
instances of the TSP.

## Example

Imagine that a salesman needs to visit a set of cities in order to make sales calls. The cities are:

- Los Angeles
- San Francisco
- Denver
- Chicago
- New York

The salesman must start in one of the cities, visit each of the other cities exactly once, and then return to the
starting city. The distance between each pair of cities is given in the table below:

|               | Los Angeles | San Francisco | Denver | Chicago | New York |
|---------------|-------------|---------------|--------|---------|----------|
| Los Angeles   | 0           | 380           | 710    | 1730    | 2700     |
| San Francisco | 380         | 0             | 960    | 2070    | 3150     |
| Denver        | 710         | 960           | 0      | 1320    | 2390     |
| Chicago       | 1730        | 2070          | 1320   | 0       | 1710     |
| New York      | 2700        | 3150          | 2390   | 1710    | 0        |

One possible solution to this TSP could be:

Start in Los Angeles.

- Go to San Francisco (distance = 380).
- Go to Denver (distance = 960).
- Go to Chicago (distance = 1320).
- Go to New York (distance = 1710).
- Go back to Los Angeles (distance = 2700).
  The total distance traveled in this solution is 860. This solution is not necessarily the optimal solution,
  as there may be other routes that have a shorter total distance.

![TSP](https://miro.medium.com/max/992/1*3Ct_bqpIsDVnMEJh6R29Hw.png)