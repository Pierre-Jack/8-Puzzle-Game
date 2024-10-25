from collections import deque

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

        # response array
        response_array = []
        init = int(''.join(map(str, received_array)))
        solvable, m = solve_dfs(init)
        if solvable:
            response_array = get_directions(get_path(m))
        print(f'Response array: {response_array}')
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

