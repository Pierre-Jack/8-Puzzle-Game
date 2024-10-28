from unittest import TestCase
from algorithms.IDS import IDS
from Helper import Helper

class TestIDS(TestCase):
    def test_solve_dls(self):
        initial_state = 603247851
        goal_state = 12345678
        solver = IDS(initial_state, goal_state)
        solvable, parent_dict, nodes_expanded = solver.solve_dls(10)
        self.assertTrue(solvable)
        self.assertGreater(nodes_expanded, 0)
        path = Helper.get_path(parent_dict, goal_state)
        self.assertEqual(path[-1], goal_state)

    def test_solve_dls_unsolvable(self):
        initial_state = 987654321
        goal_state = 12345678
        solver = IDS(initial_state, goal_state)
        solvable, parent_dict, nodes_expanded = solver.solve_dls(10)
        self.assertFalse(solvable)
        self.assertEqual(nodes_expanded, 0)
        path = Helper.get_path(parent_dict, goal_state)
        self.assertEqual(path, [])

    def test_solve(self):
        initial_state = 603247851
        goal_state = 12345678
        solver = IDS(initial_state, goal_state)
        solvable, parent_dict, nodes_expanded = solver.solve()
        self.assertTrue(solvable)
        self.assertGreater(nodes_expanded, 0)
        path = Helper.get_path(parent_dict, goal_state)
        self.assertEqual(path[-1], goal_state)

    def test_solve_unsolvable(self):
        initial_state = 987654321
        goal_state = 12345678
        solver = IDS(initial_state, goal_state)
        solvable, parent_dict, nodes_expanded = solver.solve()
        self.assertFalse(solvable)
        self.assertEqual(nodes_expanded, 0)
        path = Helper.get_path(parent_dict, goal_state)
        self.assertEqual(path, [])