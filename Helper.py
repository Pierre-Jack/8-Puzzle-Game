class Helper:
    @staticmethod
    def get_children(state):
        children = []
        s = str(state)
        if len(s) < 9: s = "0" + s
        i = s.find("0")

        for j in [-3, -1, 1, 3]:
            ns = list(s)
            if 0 <= i + j < 9:
                if not (j == -1 and i % 3 == 0):
                    if not (j == 1 and i % 3 == 2):
                        ns[i], ns[i + j] = ns[i + j], ns[i]
                        children.append(int("".join(ns)))
        return children

    @staticmethod
    def get_path(parent_dict, goal):
        from collections import deque
        path = deque()
        node = goal
        if node not in parent_dict:
            return []
        while node != -1:
            path.appendleft(node)
            node = parent_dict[node]
        return list(path)

    @staticmethod
    def get_direction(state1, state2):
        val = {-3: "UP", -1: "LEFT", 1: "RIGHT", 3: "DOWN"}
        s = str(state1)
        if len(s) < 9: s = "0" + s
        i = s.find("0")

        for j in [-3, -1, 1, 3]:
            ns = list(s)
            if 0 <= i + j < 9:
                if not (j == -1 and i % 3 == 0):
                    if not (j == 1 and i % 3 == 2):
                        ns[i], ns[i + j] = ns[i + j], ns[i]
                        if state2 == int("".join(ns)):
                            return val[j]

    @staticmethod
    def get_directions(path):
        directions = []
        for i in range(len(path) - 1):
            directions.append(Helper.get_direction(path[i], path[i + 1]))
        return directions