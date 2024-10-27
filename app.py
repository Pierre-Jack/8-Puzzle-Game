from collections import deque
import heapq
import time
# from sympy.strategies.core import switch


def get_children(state):  #missing number is 0
    children = []
    s = str(state)
    if len(s) < 9: s = "0" + s
    i = s.find("0")

    for j in [-3, -1, 1, 3]:
        ns = list(s)

        if 0 <= i+j < 9:
            if not (j == -1 and i%3 == 0):
                if not (j == 1 and i%3 == 2):
                    tmp = ns[i]
                    ns[i] = ns[i+j]
                    ns[i+j] = tmp
                    children.append(int("".join(ns)))
    return children

def solve_bfs(initial):   #missing number is 0
    q = deque()
    goal = 12345678
    #s = set()
    d = dict()
    state = initial
    nodes_expanded = 0
    d[state] = -1
    if state == goal:
        return True, d, nodes_expanded
    q.append(state)

    while q:
        nodes_expanded = nodes_expanded + 1
        for child in get_children(state):
            if not child in d:
                d[child] = state
                q.append(child)
        state = q.popleft()
        if state == goal:
            return True, d, nodes_expanded
    return False, d, nodes_expanded

def solve_dfs(initial):   #missing number is 0
    stack = []
    goal = 12345678
    d = dict()
    explore = set()
    state = initial
    nodes_expanded = 0
    d[state] = -1
    max_depth = 0

    if state == goal:
        return True, d, nodes_expanded, max_depth
    stack.append((state,0))

    while stack:
        state, level= stack.pop()
        max_depth = max(max_depth, level)
        if state == goal:
            return True, d,nodes_expanded, max_depth
        explore.add(state)
        nodes_expanded = nodes_expanded + 1
        for child in get_children(state):
            if not child in d and not child in stack and not child in explore:
                d[child] = state
                stack.append((child, level+1))

    return False, d, nodes_expanded, max_depth

def solve_ids(initial):   #missing number is 0
    depth = 0
    nodes_expanded = 0
    while depth < 2e5:
        solvable, m, n = solve_dls(initial, depth)
        nodes_expanded = nodes_expanded + n
        if solvable:
            return True, m, nodes_expanded
        depth += 1
    return False, {}, nodes_expanded

def solve_dls(initial, depth):   #missing number is 0
    stack = []
    goal = 12345678
    d = dict()
    state = initial
    nodes_expanded = 0
    d[state] = -1

    if state == goal:
        return True, d, nodes_expanded

    stack.append((state, 0))

    while stack:
        state, level = stack.pop()
        if state == goal:
            return True, d, nodes_expanded
        if level < depth:
            nodes_expanded = nodes_expanded + 1
            for child in get_children(state):
                if not child in d:
                    d[child] = state
                    stack.append((child, level+1))
    return False, d, nodes_expanded

class AStarState(object):
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

def manhattan_distance(state):
    s = str(state)
    if len(s) < 9: s = "0" + s
    i = s.find("0")
    # ns = list(s)
    x, y = i%3, i//3
    return x+y

def euclidean_distance(state):
    s = str(state)
    if len(s) < 9: s = "0" + s
    i = s.find("0")
    x, y = i%3, i//3
    return (x**2 + y**2)**0.5

def get_cost_to_state(state, parent_dict):  #gets the cost to reach the state from the initial state
    cost = 0
    node = state
    while parent_dict[node] != -1:
        cost += 1
        node = parent_dict[node]
    return cost

def state_heuristic(state, heuristic):
    if heuristic == 0:
        return manhattan_distance(state)
    elif heuristic == 1:
        return euclidean_distance(state)


def solve_astar(initial, heuristic):   #missing number is 0
    frontier = []
    goal = 12345678
    d = dict()
    explored = []
    nodes_expanded = 0
    state = initial
    d[state] = -1

    if state == goal:
        return True, d, nodes_expanded

    frontier.append(AStarState(state, 0, state_heuristic(state, heuristic)))
    heapq.heapify(frontier)

    while frontier:         #while frontier is not empty
        current_state = heapq.heappop(frontier)
        if current_state.state == goal:
            return True, d, nodes_expanded
        explored.append(current_state)
        nodes_expanded += 1

        for child in get_children(current_state.state):
            temp = AStarState(child, 0, 0)
            if not (temp in explored or temp in frontier):
                d[child] = current_state.state
                child_state = AStarState(child, get_cost_to_state(child, d), state_heuristic(child, heuristic))
                heapq.heappush(frontier, child_state)
                # heapq.heapify(frontier)
            elif temp in frontier:          #update the cost if the new cost is less
                for i in range(len(frontier)):
                    if frontier[i].state == temp.state:
                        if get_cost_to_state(child, d) < frontier[i].g:
                            frontier[i].g = get_cost_to_state(child, d)
                        if state_heuristic(child, heuristic) < frontier[i].h:
                            frontier[i].h = state_heuristic(child, heuristic)
                        heapq.heapify(frontier)

    print("No solution found")      #for debugging purposes
    return False, d, nodes_expanded

def get_path(parent_dict):  #gets the path from the dict of states -- (node, parent) is stored as (key, value) in the dict
    path = deque()
    node = 12345678
    if node not in parent_dict: #for debugging purposes
        return []
    while node != -1:
        path.appendleft(node)
        node = parent_dict[node]
    path = list(path)
    return path

def get_direction(state1, state2):
    val = {-3: "UP", -1: "LEFT", 1: "RIGHT", 3: "DOWN",}
    s = str(state1)
    if len(s) < 9: s = "0" + s
    i = s.find("0")

    for j in [-3, -1, 1, 3]:
        ns = list(s)
        if 0 <= i+j < 9:
            if not (j == -1 and i%3 == 0):
                if not (j == 1 and i%3 == 2):
                    tmp = ns[i]
                    ns[i] = ns[i+j]
                    ns[i+j] = tmp
                    if state2 == (int("".join(ns))):
                        return val[j]

def get_directions(path):
    directions = []
    for i in range(len(path)-1):
        directions.append(get_direction(path[i], path[i+1]))
    return directions

init = 603247851



from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        received_array = json.loads(post_data)
        print(f'Received array: {received_array}')
        init = int(''.join(map(str, received_array)))
        path = self.path.strip('/')

        start_time = time.time()

        if path == 'bfs':
            solvable, m, nodes_expanded = solve_bfs(init)
        elif path == 'dfs':
            solvable, m, nodes_expanded, maxdepth = solve_dfs(init)
        elif path == 'ids':
            solvable, m, nodes_expanded = solve_ids(init)
        elif path == 'astar_manhattan':
            solvable, m, nodes_expanded = solve_astar(init, 0)
            # solvable, m = solve_astar(init, 0)
        elif path == 'astar_euclidean':
            solvable, m, nodes_expanded = solve_astar(init, 1)
        else:
            self.send_response(404)
            self.end_headers()
            return

        end_time = time.time()
        total_time = end_time - start_time
        response_array = get_directions(get_path(m)) if solvable else []
        print(f'Response array: {response_array}')
        print(f'Cost: {len(response_array)}')


        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = {
            'array': response_array,
            'nodes_expanded': nodes_expanded,
            'solvable': solvable,
            'totaltime': f"{int(total_time*1000)} ms",
            'cost': len(response_array),
            'maxdepth': maxdepth if path == 'dfs' else len(response_array)
        }
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

