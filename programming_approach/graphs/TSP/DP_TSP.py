import itertools
import numpy as np
import networkx as nx
from typing import List

from algo_fermat_utils.helpers import measure_performance


class TSPSolver:
    @measure_performance
    def lol_dp_solve(self, distance_matrix: np.ndarray) -> List[int]:
        """
        Solve the TSP problem using dynamic programming and a distance matrix.

        Parameters:
        - distance_matrix: a 2D NumPy array containing the distances between the cities. distance_matrix[i, j]
            represents the distance between city i and city j.

        Returns:
        - A list of integers representing the order in which the cities should be visited.
        """

        # Get the number of cities
        num_cities = distance_matrix.shape[0]

        # Initialize the memoization array
        memo = np.full((1 << num_cities, num_cities), np.inf)
        memo[1, 0] = 0

        # Iterate through all possible subsets of cities
        for subset in range(1, 1 << num_cities):
            # Iterate through all cities in the current subset
            for current_city in range(num_cities):
                if subset & (1 << current_city) == 0:
                    continue
                # Iterate through all cities in the current subset that come before the current city
                for previous_city in range(num_cities):
                    if current_city == previous_city or subset & (1 << previous_city) == 0:
                        continue
                    # Update the minimum distance to reach the current city from the previous city
                    memo[subset, current_city] = min(memo[subset, current_city],
                                                     memo[subset ^ (1 << current_city), previous_city] +
                                                     distance_matrix[previous_city, current_city])

        # Initialize the list of city orders to the first possible order
        best_order = list(range(num_cities))

        # Initialize the shortest distance to the distance of the first possible order
        shortest_distance = memo[(1 << num_cities) - 1, 0]

        # Iterate through all possible permutations of the city order
        for order in itertools.permutations(range(num_cities)):
            # Calculate the total distance of the current order
            distance = 0
            for i in range(num_cities - 1):
                distance += distance_matrix[order[i]][order[i + 1]]
            distance += distance_matrix[order[-1]][order[0]]

            # Update the shortest distance and best order if necessary
            if distance < shortest_distance:
                shortest_distance = distance
                best_order = order

        return best_order

    @measure_performance
    def graph_dp_solve(self, G: nx.Graph) -> List[int]:
        """
        Solve the TSP problem using dynamic programming and a NetworkX Graph object.

        Parameters:
        - G: a NetworkX Graph object representing the cities and distances between them. The nodes of the graph
            represent the cities, and the edges represent the distances between the cities.

        Returns:
        - A list of integers representing the order in which the cities should be visited.
        """

        # Get the number of cities
        num_cities = G.number_of_nodes()

        # Initialize the memoization array
        # here the 1 << num_cities is the number of subsets of cities
        # and the num_cities is the number of cities
        memo = np.full((1 << num_cities, num_cities), np.inf)
        memo[1, 0] = 0

        # Iterate through all possible subsets of cities
        for subset in range(1, 1 << num_cities):
            # Iterate through all cities in the current subset
            for current_city in range(num_cities):
                if subset & (1 << current_city) == 0:
                    continue
                # Iterate through all cities in the current subset that come before the current city
                for previous_city in range(num_cities):
                    if current_city == previous_city or subset & (1 << previous_city) == 0:
                        continue
                    # Update the minimum distance to reach the current city from the previous city
                    memo[subset, current_city] = min(memo[subset, current_city],
                                                     memo[subset ^ (1 << current_city), previous_city] +
                                                     G[previous_city][current_city]['weight'])

        # Initialize the list of city orders to the first possible order
        best_order = list(range(num_cities))

        # Initialize the shortest distance to the distance of the first possible order
        shortest_distance = memo[(1 << num_cities) - 1, 0]

        # Iterate through all possible permutations of the city order
        for order in itertools.permutations(range(num_cities)):
            # Calculate the total distance of the current order
            distance = 0
            for i in range(num_cities - 1):
                distance += G[order[i]][order[i + 1]]['weight']
            distance += G[order[-1]][order[0]]['weight']

            # Update the shortest distance and best order if necessary
            if distance < shortest_distance:
                shortest_distance = distance
                best_order = order

        return best_order


if __name__ == '__main__':
    # Create a graph
    G = nx.Graph()
    G.add_edge(0, 1, weight=1)
    G.add_edge(0, 2, weight=2)
    G.add_edge(0, 3, weight=3)
    G.add_edge(1, 2, weight=4)
    G.add_edge(1, 3, weight=5)
    G.add_edge(2, 3, weight=6)

    # Create a distance matrix
    distance_matrix = np.array([[0, 1, 2, 3],
                                [1, 0, 4, 5],
                                [2, 4, 0, 6],
                                [3, 5, 6, 0]])

    # Solve the TSP problem using dynamic programming and a distance matrix
    solver = TSPSolver()
    order = solver.lol_dp_solve(distance_matrix)
    print(order)

    # Solve the TSP problem using dynamic programming and a NetworkX Graph object
    order = solver.graph_dp_solve(G)
    print(order)
