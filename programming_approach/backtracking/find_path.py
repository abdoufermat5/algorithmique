from algo_fermat_utils.helpers import measure_performance


def find_path(maze, start, end):
    if start == end:
        return [start]
    for next in maze.get_neighbors(start):
        path = find_path(maze, next, end)
        if path:
            return [start] + path
    return None
