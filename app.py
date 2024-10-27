from collections import deque
import heapq

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

def solve_bfs(initial):   #missing number is 0 #
    q = deque()
    goal = 12345678
    #s = set()
    d = dict()
    state = initial

    d[state] = -1
    if state == goal:
        return True, d
    q.append(state)

    while q:
        for child in get_children(state):
            if not child in d:
                d[child] = state
                if child == goal: return True, d
                q.append(child)
        state = q.popleft()
    return False, d

def solve_dfs(initial):   #missing number is 0
    stack = []
    goal = 12345678
    d = dict()
    explore = set()
    state = initial

    d[state] = -1

    if state == goal:
        return True, d
    stack.append(state)

    while stack:
        state = stack.pop()
        explore.add(state)
        for child in get_children(state):
            if not child in d and not child in stack and not child in explore:
                d[child] = state
                if child == goal:
                    return True, d
                stack.append(child)
    return False, d

def solve_ids(initial):   #missing number is 0
    depth = 0
    while depth < 1e15:
        solvable, m = solve_dls(initial, depth)
        if solvable:
            return True, m
        depth += 1
    return False, {}

def solve_dls(initial, depth):   #missing number is 0
    stack = []
    goal = 12345678
    d = dict()
    state = initial

    d[state] = -1

    if state == goal:
        return True, d

    stack.append((state, 0))

    while stack:
        state, level = stack.pop()
        if level < depth:
            for child in get_children(state):
                if not child in d:
                    d[child] = state
                    if child == goal:
                        return True, d
                    stack.append((child, level+1))
    return False, d

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


def solve_astar(initial):   #missing number is 0
    frontier = []
    goal = 12345678
    d = dict()
    explored = []
    state = initial
    d[state] = -1

    if state == goal:
        return True, d

    frontier.append(AStarState(state, 0, manhattan_distance(state)))
    heapq.heapify(frontier)

    while frontier:         #while frontier is not empty
        current_state = heapq.heappop(frontier)
        if current_state.state == goal:
            return True, d
        explored.append(current_state)

        for child in get_children(current_state.state):
            temp = AStarState(child, 0, 0)
            if not (temp in explored or temp in frontier):
                d[child] = current_state.state
                child_state = AStarState(child, get_cost_to_state(child, d), manhattan_distance(child))
                heapq.heappush(frontier, child_state)
                # heapq.heapify(frontier)
            elif temp in frontier:          #update the cost if the new cost is less
                for i in range(len(frontier)):
                    if frontier[i].state == temp.state:
                        if get_cost_to_state(child, d) < frontier[i].g:
                            frontier[i].g = get_cost_to_state(child, d)
                        if manhattan_distance(child) < frontier[i].h:
                            frontier[i].h = manhattan_distance(child)
                        heapq.heapify(frontier)

    print("No solution found")      #for debugging purposes
    return False, d

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


        if path == 'bfs':
            solvable, m = solve_bfs(init)
        elif path == 'dfs':
            solvable, m = solve_dfs(init)
        elif path == 'ids':
            solvable, m = solve_ids(init)
        elif path == 'astar':
            solvable, m = solve_astar(init)
        else:
            self.send_response(404)
            self.end_headers()
            return
        response_array = get_directions(get_path(m)) if solvable else []
        print(f'Response array: {response_array}')
        print(f'Cost: {len(response_array)}')


        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = {'array': response_array}
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

