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
        level_dict = dict()
        state = self.initial
        nodes_expanded = 0
        d[state] = -1
        explore = set()
        if state == self.goal:
            return True, d, nodes_expanded
        stack.append((state, 0))
        while stack:
            state, level = stack.pop()
            explore.add(state)
            level_dict[state] = level
            if state == self.goal:
                return True, d, nodes_expanded
            if level < depth:
                nodes_expanded += 1
                for child in Helper.get_children(state):
                    if child not in explore and all(child != s[0] for s in stack):
                        d[child] = state
                        stack.append((child, level + 1))
                    else:
                        if all(child == s[0] for s in stack):
                            child_level = level_dict[child]
                            if level + 1 < child_level:
                                d[child] = state
                                stack.append((child, level + 1))
                        if child in explore:
                            child_level = level_dict[child]
                            if level + 1 < child_level:
                                d[child] = state
                                level_dict[child] = level + 1
                                stack.append((child, level + 1))
        return False, d, nodes_expanded

