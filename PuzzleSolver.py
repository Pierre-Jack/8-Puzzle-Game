from sympy.series.limits import heuristics

from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.IDS import IDS
from algorithms.AStar import AStar
from Helper import Helper

class PuzzleSolver:
    def __init__(self, initial):
        self.initial = initial
        self.goal = 12345678


    def solve_bfs(self):
        solver = BFS(self.initial, self.goal)
        return solver.solve()

    def solve_dfs(self):
        solver = DFS(self.initial, self.goal)
        return solver.solve()

    def solve_ids(self):
        solver = IDS(self.initial, self.goal)
        return solver.solve()

    def solve_astar(self, heuristic):
        solver = AStar(self.initial, self.goal,heuristic)
        return solver.solve()

    def get_path(self, parent_dict):
        return Helper.get_path(parent_dict, self.goal)

    def get_directions(self, path):
        return Helper.get_directions(path)