import heapq
from Helper import Helper

class AStar:
    class AStarState:
        def __init__(self, state, g, h):
            self.state = state
            self.g = g
            self.h = h
            self.f = g + h

        def __repr__(self):
            return f'State: {self.state}, G(n)= {self.g}, H(n)= {self.h}'

        def __lt__(self, other):
            return self.f < other.f

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

    @staticmethod
    def get_cost_to_state(state, parent_dict):
        cost = 0
        node = state
        while parent_dict[node] != -1:
            cost += 1
            node = parent_dict[node]
        return cost

    @staticmethod
    def state_heuristic(state, heuristic):
        if heuristic == 0:
            return AStar.manhattan_distance(state)
        elif heuristic == 1:
            return AStar.euclidean_distance(state)

    # @staticmethod
    # def update_state_indices(frontier, state_indices):
    #     for i in range(len(frontier)):
    #         state_indices[frontier[i].state] = i

    def __init__(self, initial, goal, heuristic):
        self.initial = initial
        self.goal = goal
        self.heuristic = heuristic

    def solve(self):
        frontier = []
        d = dict()
        state_costs = dict()
        # state_indices = dict()
        explored = set()
        states_in_frontier = set()
        nodes_expanded = 0
        state = self.initial
        d[state] = -1

        if state == self.goal:
            return True, d, nodes_expanded

        initial_state = AStar.AStarState(state, 0, AStar.state_heuristic(state, self.heuristic))
        frontier.append(initial_state)
        heapq.heapify(frontier)
        states_in_frontier.add(state)
        state_costs[state] = initial_state.f
        # state_indices[state] = 0

        while frontier:
            current_state = heapq.heappop(frontier)
            states_in_frontier.remove(current_state.state)
            if current_state.state == self.goal:
                return True, d, nodes_expanded
            explored.add(current_state.state)
            nodes_expanded += 1

            for child in Helper.get_children(current_state.state):
                # temp = AStar.AStarState(child, 0, 0)
                if not (child in explored.union(states_in_frontier)):
                    d[child] = current_state.state
                    child_state = AStar.AStarState(child, current_state.g + 1, AStar.state_heuristic(child, self.heuristic))
                    heapq.heappush(frontier, child_state)
                    # self.update_state_indices(frontier, state_indices)
                    states_in_frontier.add(child)
                    state_costs[child] = child_state.f
                elif child in states_in_frontier:
                    potential_g = current_state.g + 1
                    potential_h = AStar.state_heuristic(child, self.heuristic)
                    # current_state.f - AStar.state_heuristic(state, self.heuristic) + 1
                    if state_costs[child] > potential_g + potential_h:
                        frontier = [AStar.AStarState(s.state, s.g, s.h) for s in frontier if s.state != child]
                        state_costs[child] = potential_g + potential_h
                        heapq.heappush(frontier, AStar.AStarState(child, potential_g, potential_h))

                        # new_frontier = []
                        # heapq.heapify(new_frontier)
                        # for s in states_in_frontier:
                        #     heapq.heappush(new_frontier, AStar.AStarState(s, state_costs[s] - AStar.state_heuristic(s, self.heuristic), AStar.state_heuristic(s, self.heuristic)))
                        # frontier = new_frontier

        print("No solution found")
        return False, d, nodes_expanded