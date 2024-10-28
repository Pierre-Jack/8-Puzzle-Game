from unittest import TestCase
from algorithms.DFS import DFS
from Helper import Helper

class TestDFS(TestCase):
    def test_solve(self):
        initial_state = 603247851
        goal_state = 12345678
        solver = DFS(initial_state, goal_state)
        solvable, parent_dict, nodes_expanded, max_depth = solver.solve()
        self.assertTrue(solvable)
        self.assertGreater(nodes_expanded, 0)
        self.assertGreater(max_depth, 0)
        path = Helper.get_path(parent_dict, goal_state)
        self.assertEqual(path[-1], goal_state)

    def test_solve_unsolvable(self):
        initial_state = 987654321
        goal_state = 12345678
        solver = DFS(initial_state, goal_state)
        solvable, parent_dict, nodes_expanded, max_depth = solver.solve()
        self.assertFalse(solvable)
        self.assertEqual(nodes_expanded, 0)
        self.assertEqual(max_depth, 0)
        path = Helper.get_path(parent_dict, goal_state)
        self.assertEqual(path, [])



def dfs(self, limit: int):
    stack = [(self.initial_State, 0)]
    max_depth = 0
    while stack:
        current, level = stack.pop()
        max_depth = max(max_depth, level)
        self.explored.add(current)
        self.level[current] = level
        if current == self.goal:
            self.get_path(current)
            return self.path, len(self.path), len(self.explored), max_depth
        if level < limit:
            for child in self.get_children(current):
                if (child[0] not in self.explored or (child[0]  in self.explored and self.level[child[0]] > level + 1 )) and (self.not_in_stack(child[0], stack, level)):
                    stack.append((child[0], level + 1))
                    self.level[child[0]] = level + 1
                    self.parent[child[0]] = (current, child[1])
    return None, None, len(self.explored), max_depth
