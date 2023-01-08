class Maze:
    def __init__(self, edges):
        self.edges = edges

    def get_neighbors(self, node):
        return self.edges[node]