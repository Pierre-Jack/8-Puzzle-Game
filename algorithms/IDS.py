from Helper import Helper

class IDS:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self):
        depth = 0
        nodes_expanded = 0
        while depth < 32:
            solvable, m, n = self.solve_dls(depth)
            nodes_expanded += n
            if solvable:
                return True, m, nodes_expanded
            depth += 1
        return False, {}, nodes_expanded

    def solve_dls(self, depth):
        stack = []
        stack_set = set()
        parent_dict = dict()
        level_dict = dict()
        state = self.initial
        nodes_expanded = 0
        parent_dict[state] = -1
        explore_set = set()

        if state == self.goal:
            return True, parent_dict, nodes_expanded

        stack.append((state, 0))
        stack_set.add(state)

        while stack:
            state, level = stack.pop()
            explore_set.add(state)
            level_dict[state] = level
            if state == self.goal:
                return True, parent_dict, nodes_expanded
            if level < depth:
                nodes_expanded += 1
                for child in Helper.get_children(state):
                    if child not in explore_set and child not in stack_set:
                        parent_dict[child] = state
                        stack.append((child, level + 1))
                        stack_set.add(child)
                    else:
                        child_level = level_dict.get(child, 0)
                        if level + 1 < child_level:
                            parent_dict[child] = state
                            level_dict[child] = level + 1
                            stack.append((child, level + 1))
                            stack_set.add(child)
        return False, parent_dict, nodes_expanded

