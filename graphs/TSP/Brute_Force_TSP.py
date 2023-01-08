import itertools
from typing import List

import networkx as nx

from algo_fermat_utils.helpers import measure_performance


class TSPSolver:
    def __init__(self):
        pass

    def __call__(self, data):
        if isinstance(data, list):
            return self.lol_brute_force_solve(data)
        elif isinstance(data, nx.Graph):
            return self.graph_brute_force_solve(data)
        else:
            raise TypeError("Invalid data type")

    # LOL = List of Lists
    @measure_performance
    def lol_brute_force_solve(self, distance_matrix: List[List[int]]) -> List[int]:
        """
        Given a distance matrix for a set of cities, find the shortest possible route that visits each
        city exactly once and returns to the starting city using a brute force approach.

        Parameters:
        - distance_matrix: a list of lists containing the distances between the cities. distance_matrix[i][j]
                          represents the distance between city i and city j.

        Returns:
        - A list of integers representing the order in which the cities should be visited.
        """

        # Get the number of cities
        num_cities = len(distance_matrix)

        # Initialize the list of city orders to the first possible order
        best_order = list(range(num_cities))

        # Initialize the shortest distance to the distance of the first possible order
        shortest_distance = self._calculate_total_distance1(best_order, distance_matrix)

        # Iterate through all possible permutations of the city order
        for order in itertools.permutations(range(num_cities)):
            # Calculate the total distance of the current order
            distance = self._calculate_total_distance1(order, distance_matrix)

            # If the current order is shorter than the current shortest order, update the shortest order
            if distance < shortest_distance:
                shortest_distance = distance
                best_order = list(order)

        # Return the shortest order
        return best_order

    @measure_performance
    def graph_brute_force_solve(self, G: nx.Graph) -> List[int]:
        """
        Given a weighted graph representing the distances between a set of cities, find the shortest possible
        route that visits each city exactly once and returns to the starting city using a brute force approach.

        Parameters:
        - G: a NetworkX Graph object representing the cities and distances between them. The nodes of the graph
            represent the cities, and the edges represent the distances between the cities.

        Returns:
        - A list of integers representing the order in which the cities should be visited.
        """

        # Get the number of cities
        num_cities = G.number_of_nodes()

        # Initialize the list of city orders to the first possible order
        best_order = list(range(num_cities))

        # Initialize the shortest distance to the distance of the first possible order
        shortest_distance = self._calculate_total_distance2(best_order, G)

        # Iterate through all possible permutations of the city order
        for order in itertools.permutations(range(num_cities)):
            # Calculate the total distance of the current order
            distance = self._calculate_total_distance2(order, G)

            # Update the shortest distance and best order if necessary
            if distance < shortest_distance:
                shortest_distance = distance
                best_order = order

        return best_order

    def _calculate_total_distance1(self, order: List[int], distance_matrix: List[List[int]]) -> int:
        """
        Calculate the total distance of a given order of cities using a distance matrix.

        Parameters:
        - order: a list of integers representing the order in which the cities should be visited.
        - distance_matrix: a list of lists containing the distances between the cities. distance_matrix[i][j]
            represents the distance between city i and city j.

        Returns:
        - The total distance of the given order of cities.
        """

        # Initialize the total distance to the distance between the starting city and the first city in the order
        total_distance = distance_matrix[order[0]][order[1]]

        # Iterate through the pairs of cities in the order
        for i in range(len(order) - 1):
            # Add the distance between the current city and the next city to the total distance
            total_distance += distance_matrix[order[i]][order[i + 1]]

        # Add the distance between the last city and the starting city to the total distance
        total_distance += distance_matrix[order[-1]][order[0]]

        return total_distance

    def _calculate_total_distance2(self, order: List[int], G: nx.Graph) -> int:
        """
        Calculate the total distance of a given order of cities using a NetworkX Graph object.

        Parameters:
        - order: a list of integers representing the order in which the cities should be visited.
        - G: a NetworkX Graph object representing the cities and distances between them. The nodes of the graph
            represent the cities, and the edges represent the distances between the cities.

        Returns:
        - The total distance of the given order of cities.
        """

        # Initialize the total distance to the distance between the starting city and the first city in the order
        total_distance = G[order[0]][order[1]]['weight']

        # Iterate through the pairs of cities in the order
        for i in range(len(order) - 1):
            # Add the distance between the current city and the next city to the total distance
            total_distance += G[order[i]][order[i+1]]['weight']

        # Add the distance between the last city and the starting city to the total distance
        total_distance += G[order[-1]][order[0]]['weight']

        return total_distance


if __name__ == "__main__":
    print("------------------> TSP problem with brute force approach <------------------")
    solver = TSPSolver()
    distance_matrix = [[0, 1, 2, 3],
                       [1, 0, 4, 5],
                       [2, 4, 0, 6],
                       [3, 5, 6, 0]]
    print("RESULT USING LIST OF LIST: ", solver(distance_matrix))
    print("-" * 50)
    G = nx.Graph()
    G.add_nodes_from(range(4))
    G.add_edge(0, 1, weight=1)
    G.add_edge(0, 2, weight=2)
    G.add_edge(0, 3, weight=3)
    G.add_edge(1, 2, weight=4)
    G.add_edge(1, 3, weight=5)
    G.add_edge(2, 3, weight=6)
    print("RESULT USING USING GRAPH", solver(G))


