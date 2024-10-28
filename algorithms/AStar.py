import heapq
from Helper import Helper

class AStar:
    class AStarState:               #Class to store the state, g(n), h(n) and f(n) values
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
    def manhattan_distance(state):          #Find the manhattan distance of the state for all points except 0
        s = str(state)
        if len(s) < 9: s = "0" + s
        m_distance = 0
        for i in range(9):
            if s[i] != "0":
                x, y = i % 3, i // 3
                x_goal, y_goal = int(s[i]) % 3, int(s[i]) // 3
                m_distance += abs(x - x_goal) + abs(y - y_goal)
        return m_distance

    @staticmethod
    def euclidean_distance(state):          #Find the Euclidean distance of the state for all points except 0
        s = str(state)
        if len(s) < 9: s = "0" + s
        e_distance = 0
        for i in range(9):
            if s[i] != "0":
                x, y = i % 3, i // 3
                x_goal, y_goal = int(s[i]) % 3, int(s[i]) // 3
                e_distance += ((x - x_goal)**2 + (y - y_goal)**2)**0.5
        return e_distance

    @staticmethod
    def state_heuristic(state, heuristic):      #Return the heuristic value of the state based on the heuristic chosen
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
        parent_dict = dict()
        state_costs = dict()
        explored = set()
        states_in_frontier = set()
        nodes_expanded = 0
        state = self.initial
        parent_dict[state] = -1

        if state == self.goal:          #Goal Test
            return True, parent_dict, nodes_expanded

        #Push the initial state into the frontier
        initial_state = AStar.AStarState(state, 0, AStar.state_heuristic(state, self.heuristic))
        frontier.append(initial_state)
        heapq.heapify(frontier)
        states_in_frontier.add(state)
        state_costs[state] = initial_state.f


        while frontier:
            current_state = heapq.heappop(frontier)
            states_in_frontier.remove(current_state.state)
            if current_state.state == self.goal:            #Goal Test
                return True, parent_dict, nodes_expanded
            explored.add(current_state.state)
            nodes_expanded += 1

            for child in Helper.get_children(current_state.state):
                if not ((child in explored) or (child in states_in_frontier)):      #If the child is not in explored or frontier, add it to the frontier
                    parent_dict[child] = current_state.state
                    child_state = AStar.AStarState(child, current_state.g + 1, AStar.state_heuristic(child, self.heuristic))
                    heapq.heappush(frontier, child_state)
                    states_in_frontier.add(child)
                    state_costs[child] = child_state.f
                elif child in states_in_frontier:                                   #If the child is in the frontier, update the cost if the new cost is less
                    potential_g = current_state.g + 1
                    potential_h = AStar.state_heuristic(child, self.heuristic)
                    if state_costs[child] > potential_g + potential_h:
                        frontier = [AStar.AStarState(s.state, s.g, s.h) for s in frontier if s.state != child]          #Make a new frontier without the child
                        state_costs[child] = potential_g + potential_h
                        parent_dict[child] = current_state.state
                        heapq.heappush(frontier, AStar.AStarState(child, potential_g, potential_h))             #Push the child with the new cost into the frontier

        #If no solution is found
        return False, parent_dict, nodes_expanded