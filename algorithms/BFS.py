from collections import deque
from Helper import Helper

class BFS:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self):
        q = deque()
        d = dict()
        state = self.initial
        nodes_expanded = 0
        d[state] = -1
        if state == self.goal:
            return True, d, nodes_expanded
        q.append(state)

        while q:
            nodes_expanded += 1
            for child in Helper.get_children(state):
                if child not in d:
                    d[child] = state
                    q.append(child)
            state = q.popleft()
            if state == self.goal:
                return True, d, nodes_expanded
        return False, d, nodes_expanded