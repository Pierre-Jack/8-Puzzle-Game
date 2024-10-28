from Helper import Helper

class DFS:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def solve(self):
        stack = []
        stack_set = set()
        parent_dict = dict()
        explore_set = set()
        state = self.initial
        nodes_expanded = 0
        max_depth = 0
        parent_dict[state] = -1


        if state == self.goal:
            return True, parent_dict, nodes_expanded, max_depth
        stack.append((state, 0))
        stack_set.add(state)
        while stack:
            state, level = stack.pop()
            explore_set.add(state)
            max_depth = max(max_depth, level)
            if state == self.goal:
                return True, parent_dict, nodes_expanded, max_depth
            nodes_expanded += 1
            for child in Helper.get_children(state):
                if child not in stack_set and child not in explore_set:
                    parent_dict[child] = state
                    stack.append((child, level + 1))
                    stack_set.add(state)

        return False, parent_dict, nodes_expanded, max_depth