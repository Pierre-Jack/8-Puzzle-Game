from Helper import Helper

class IDS:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self):
        depth = 0
        nodes_expanded = 0
        while depth < 2e5:
            solvable, m, n = self.solve_dls(depth)
            nodes_expanded += n
            if solvable:
                return True, m, nodes_expanded
            depth += 1
        return False, {}, nodes_expanded

    def solve_dls(self, depth):
        stack = []
        d = dict()
        state = self.initial
        nodes_expanded = 0
        d[state] = -1

        if state == self.goal:
            return True, d, nodes_expanded

        stack.append((state, 0))

        while stack:
            state, level = stack.pop()
            if state == self.goal:
                return True, d, nodes_expanded
            if level < depth:
                nodes_expanded += 1
                for child in Helper.get_children(state):
                    if child not in d:
                        d[child] = state
                        stack.append((child, level + 1))
        return False, d, nodes_expanded