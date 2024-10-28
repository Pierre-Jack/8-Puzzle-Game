import heapq
from Helper import Helper

class AStar:
    class AStarState:
        def __init__(self, state, g, h):
            self.state = state
            self.g = g
            self.h = h

        def __repr__(self):
            return f'State: {self.state}, G(n)= {self.g}, H(n)= {self.h}'

        def __lt__(self, other):
            return (self.h + self.g) < (other.h + other.g)

        def __eq__(self, other):
            return self.state == other.state

        def __hash__(self):
            return hash(self.state)

    @staticmethod
    def manhattan_distance(state):
        s = str(state)
        if len(s) < 9: s = "0" + s
        i = s.find("0")
        x, y = i % 3, i // 3
        return x + y

    @staticmethod
    def euclidean_distance(state):
        s = str(state)
        if len(s) < 9: s = "0" + s
        i = s.find("0")
        x, y = i % 3, i // 3
        return (x**2 + y**2)**0.5

    # @staticmethod
    # def get_cost_to_state(state, parent_dict):
    #     cost = 0
    #     node = state
    #     while parent_dict[node] != -1:
    #         cost += 1
    #         node = parent_dict[node]
    #     return cost

    @staticmethod
    def state_heuristic(state, heuristic):
        if heuristic == 0:
            return AStar.manhattan_distance(state)
        elif heuristic == 1:
            return AStar.euclidean_distance(state)

    def __init__(self, initial, goal, heuristic):
        self.initial = initial
        self.goal = goal
        self.heuristic = heuristic

    def solve(self):
        frontier = []
        d = dict()
        explored = set()
        states_in_frontier = set()
        nodes_expanded = 0
        state = self.initial
        d[state] = -1
        if state == self.goal:
            return True, d, nodes_expanded

        frontier.append(AStar.AStarState(state, 0, AStar.state_heuristic(state, self.heuristic)))
        heapq.heapify(frontier)
        states_in_frontier.add((state,0))

        while frontier:
            current_state, i = heapq.heappop(frontier)
            states_in_frontier.remove((current_state.state, i))
            if current_state.state == self.goal:
                return True, d, nodes_expanded
            explored.add(current_state.state)

            nodes_expanded += 1

            for child in Helper.get_children(current_state.state):
                #temp = AStar.AStarState(child, 0, 0)
                # if not (child in explored.union(states_in_frontier)):
                if not child in explored and not child in states_in_frontier:
                    d[child] = current_state.state
                    child_state = AStar.AStarState(child, current_state.g + 1, AStar.state_heuristic(child, self.heuristic))
                    heapq.heappush(frontier, child_state)
                    states_in_frontier.add(child)
                elif child in states_in_frontier:
                    for i in range(len(frontier)):
                        if frontier[i].state == child:
                            potential_g = current_state.g + 1
                            potential_h = self.state_heuristic(child, self.heuristic)
                            if potential_g < frontier[i].g:
                                frontier[i].g = potential_g
                            if potential_h < frontier[i].h:
                                frontier[i].h = potential_g
                            heapq.heapify(frontier)


        print("No solution found")
        return False, d, nodes_expanded