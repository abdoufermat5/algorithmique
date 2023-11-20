import math

from algo_fermat_utils.helpers import measure_performance


@measure_performance
def HeldKarp(D):
    # D is a distance matrix representing the distances between each pair of cities
    n = len(D)
    # C is a cache for storing the intermediate results of the algorithm
    C = {}

    # Recursive function to compute the shortest Hamiltonian cycle
    def TSP(mask, pos):
        # If we have already visited all the cities, return the distance to go back to the starting city
        if mask == (1 << n) - 1:
            return D[pos][0]
        # If we have already computed the result for the given mask and starting position, return it
        if (mask, pos) in C:
            return C[mask, pos]
        ans = math.inf
        # Try all the cities that have not been visited yet
        for i in range(n):
            if mask & (1 << i) == 0:
                # Recursive call to TSP to compute the shortest path that visits city i and then the other cities
                ans = min(ans, D[pos][i] + TSP(mask | (1 << i), i))
        # Cache the result and return it
        C[mask, pos] = ans
        return ans

    # Call the recursive function to compute the shortest Hamiltonian cycle
    return TSP(1, 0)


if __name__ == '__main__':
    # Distance matrix for the 4 cities
    D = [[0, 20, 42, 35],
         [20, 0, 30, 34],
         [42, 30, 0, 12],
         [35, 34, 12, 0]]
    print(HeldKarp(D))
