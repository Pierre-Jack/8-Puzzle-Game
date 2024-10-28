from Helper import Helper

class DFS:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self):
        stack = []
        d = dict()
        explore = set()
        state = self.initial
        nodes_expanded = 0
        max_depth = 0
        d[state] = -1

        if state == self.goal:
            return True, d, nodes_expanded, max_depth
        stack.append((state, 0))

        while stack:
            state, level = stack.pop()
            max_depth = max(max_depth, level)
            if state == self.goal:
                return True, d, nodes_expanded, max_depth
            explore.add(state)
            nodes_expanded += 1
            for child in Helper.get_children(state):
                if child not in d and child not in stack and child not in explore:
                    d[child] = state
                    stack.append((child, level + 1))

        return False, d, nodes_expanded, max_depth